# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license
"""Programmatically create and sync Replicate model metadata so deployment is no longer a manual web-UI process.

For each model directory (discovered from its ``cog.yaml`` ``image:`` target) this script:

1. ``GET``s the model on Replicate and, if it does not exist, ``POST``s it into existence with the fields that are
   only settable at creation time (``visibility``, ``hardware``, ``cover_image_url``). Creating the model up front is
   what lets the subsequent ``cog push`` succeed without a manual "create model" click.
2. ``PATCH``es the always-updatable fields (``description``, ``readme``, ``github_url``, ``paper_url``,
   ``license_url``) so the page stays in sync with the repo on every deploy.

The Replicate API splits writable fields between the two endpoints (see https://replicate.com/docs/reference/http):

- create-only: ``visibility``, ``hardware`` (docs also list ``cover_image_url`` here, but we additionally re-attempt it
  on update via a separate best-effort PATCH so the logo stays enforced on existing models too)
- update-only: ``readme``, ``weights_url``
- either:      ``description``, ``github_url``, ``paper_url``, ``license_url``

Usage:
    REPLICATE_API_TOKEN=... python replicate_metadata.py                 # sync every model in the repo
    REPLICATE_API_TOKEN=... python replicate_metadata.py --dir yolo26/seg  # sync a single model
    python replicate_metadata.py --dry-run                               # print the payloads, call nothing
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

API_BASE = "https://api.replicate.com/v1"
# The default urllib User-Agent is blocked (HTTP 403) by Replicate's CDN from datacenter IPs (e.g. CI runners).
USER_AGENT = "ultralytics-replicate-metadata/1.0 (+https://github.com/ultralytics/replicate)"

# Fields shared by every model in this repo.
GITHUB_URL = "https://github.com/ultralytics/ultralytics"
LICENSE_URL = "https://www.ultralytics.com/license"
VISIBILITY = "public"
HARDWARE = "cpu"  # all predictors run gpu: false; see each cog.yaml

# All YOLO26 task models point their Replicate "weights" link at the shared Ultralytics Platform page (update-only).
YOLO26_PLATFORM_URL = "https://platform.ultralytics.com/ultralytics/yolo26"

# Default cover image for newly created model pages. ``cover_image_url`` takes a URL (Replicate fetches it), not a file
# upload, so we point at the Ultralytics logo hosted in the public ultralytics/assets repo (stable raw URL, verified
# HTTP 200 image/png). Set on create AND re-attempted on every update (see sync), so all models — including existing
# ones and any whose cover drifted to a prediction output — converge on this logo. Per-model SPECS may override.
COVER_IMAGE_URL = (
    "https://raw.githubusercontent.com/ultralytics/assets/main/yolo/ultralytics_yolo_logomark_blue_512_512.png"
)

# Per-model copy keyed by the Replicate model slug (the name after the owner in the cog.yaml image: target).
# ``description`` is the one-line page summary; ``paper_url`` points at the canonical Ultralytics docs reference.
# ``cover_image_url`` is create-only: fill in a hosted image URL to brand a *new* model's page (existing models must
# be updated via the Replicate web UI). Leave it out to keep Replicate's default.
SPECS: dict[str, dict[str, str]] = {
    "yolo11n": {
        "description": "Ultralytics YOLO11n object detection (COCO) — fast CPU PyTorch inference.",
        "paper_url": "https://docs.ultralytics.com/models/yolo11/",
        "weights_url": "https://platform.ultralytics.com/ultralytics/yolo11",
    },
    "yolov8s-worldv2": {
        "description": "Open-vocabulary YOLOv8s-WorldV2 detection — detect any classes you name.",
        "paper_url": "https://docs.ultralytics.com/models/yolo-world/",
        "weights_url": "https://platform.ultralytics.com/ultralytics/yolov8",
    },
    "yoloe-11s": {
        "description": "YOLOE-11S open-vocabulary segmentation with text class prompts.",
        "paper_url": "https://docs.ultralytics.com/models/yoloe/",
    },
    "yolo26": {
        "description": "Ultralytics YOLO26 object detection (COCO), selectable size n/s/m/l/x.",
        "paper_url": "https://docs.ultralytics.com/models/yolo26/",
    },
    "yolo26-seg": {
        "description": "Ultralytics YOLO26 instance segmentation (COCO-Seg), selectable size n/s/m/l/x.",
        "paper_url": "https://docs.ultralytics.com/tasks/segment/",
    },
    "yolo26-sem": {
        "description": "Ultralytics YOLO26 semantic segmentation (Cityscapes), selectable size n/s/m/l/x.",
        "paper_url": "https://docs.ultralytics.com/tasks/semantic/",
    },
    "yolo26-cls": {
        "description": "Ultralytics YOLO26 image classification (ImageNet), selectable size n/s/m/l/x.",
        "paper_url": "https://docs.ultralytics.com/tasks/classify/",
    },
    "yolo26-pose": {
        "description": "Ultralytics YOLO26 pose estimation (COCO-Pose), selectable size n/s/m/l/x.",
        "paper_url": "https://docs.ultralytics.com/tasks/pose/",
    },
    "yolo26-obb": {
        "description": "Ultralytics YOLO26 oriented bounding box detection (DOTAv1), selectable size n/s/m/l/x.",
        "paper_url": "https://docs.ultralytics.com/tasks/obb/",
    },
}


def parse_image(cog_yaml: Path) -> tuple[str, str]:
    """Return ``(owner, name)`` parsed from a cog.yaml ``image: r8.im/<owner>/<name>`` line."""
    for line in cog_yaml.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("image:"):
            ref = line.split(":", 1)[1].strip().strip("\"'")  # e.g. r8.im/ultralytics/yolo26-seg
            owner, name = ref.split("/")[-2:]
            return owner, name
    raise ValueError(f"No 'image:' target found in {cog_yaml}")


def discover_models(root: Path, only_dir: str | None = None) -> list[tuple[str, str, Path]]:
    """Return ``(owner, name, model_dir)`` for every model, or just ``only_dir`` if given."""
    if only_dir:
        dirs = [root / only_dir]
    else:
        dirs = sorted({p.parent for p in root.glob("**/cog.yaml")})
    models = []
    for d in dirs:
        cog = d / "cog.yaml"
        if not cog.exists():
            raise FileNotFoundError(f"{cog} not found")
        owner, name = parse_image(cog)
        models.append((owner, name, d))
    return models


def _parse(raw: bytes) -> dict:
    """Parse a response body as JSON, degrading to ``{'_raw': ...}`` for empty/non-JSON bodies.

    Replicate sits behind proxies/CDNs that return HTML or plain text (not JSON) on 5xx errors, so the error path must
    not assume a JSON body — otherwise the very failures this script tries to report gracefully would crash it.
    """
    try:
        return json.loads(raw or b"{}")
    except json.JSONDecodeError:
        return {"_raw": raw.decode(errors="replace").strip()}


def api(method: str, path: str, token: str, body: dict | None = None) -> tuple[int, dict]:
    """Make a Replicate API request and return ``(status_code, parsed_json)``."""
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(f"{API_BASE}{path}", data=data, method=method)
    req.add_header("Authorization", f"Bearer {token}")
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", USER_AGENT)
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, _parse(resp.read())
    except urllib.error.HTTPError as e:
        return e.code, _parse(e.read())


def build_payloads(owner: str, name: str, model_dir: Path) -> tuple[dict, dict]:
    """Return ``(create_payload, update_payload)`` for one model from its README and SPECS entry."""
    spec = SPECS.get(name, {})
    readme = (model_dir / "README.md").read_text(encoding="utf-8")
    description = spec.get("description") or next(
        (ln.lstrip("# ").strip() for ln in readme.splitlines() if ln.strip() and not ln.startswith("#")),
        f"Ultralytics {name} on Replicate.",
    )
    shared = {
        "description": description,
        "github_url": GITHUB_URL,
        "license_url": LICENSE_URL,
        **({"paper_url": spec["paper_url"]} if spec.get("paper_url") else {}),
    }
    create = {
        "owner": owner,
        "name": name,
        "visibility": VISIBILITY,
        "hardware": HARDWARE,
        "cover_image_url": spec.get("cover_image_url", COVER_IMAGE_URL),
        **shared,
    }
    update = {**shared, "readme": readme}  # readme is update-only
    is_yolo26 = name == "yolo26" or name.startswith("yolo26-")
    weights_url = spec.get("weights_url") or (YOLO26_PLATFORM_URL if is_yolo26 else None)
    if weights_url:  # weights_url is update-only
        update["weights_url"] = weights_url
    return create, update


def ensure_created(slug: str, create_payload: dict, token: str) -> bool:
    """Create the model; treat an 'already exists' conflict as success. Return False only on a real create error."""
    status, body = api("POST", "/models", token, create_payload)
    if status in (200, 201):
        print(f"✓ {slug}: created (visibility={VISIBILITY}, hardware={HARDWARE})")
        return True
    if status == 409 or "already exists" in json.dumps(body).lower():
        print(f"• {slug}: exists")
        return True
    print(f"✗ {slug}: create failed ({status}): {body}", file=sys.stderr)
    return False


def sync(owner: str, name: str, model_dir: Path, token: str, dry_run: bool) -> bool:
    """Create the model if missing, then patch its metadata. Return False on a fatal (create/get) error."""
    slug = f"{owner}/{name}"
    create_payload, update_payload = build_payloads(owner, name, model_dir)

    if dry_run:
        upd = {k: (f"<{len(v)} chars>" if k == "readme" else v) for k, v in update_payload.items()}
        cover = create_payload.get("cover_image_url")
        print(f"[dry-run] {slug}\n  create: {json.dumps(create_payload)}\n  update: {json.dumps(upd)}")
        print(f"  cover-patch: {json.dumps({'cover_image_url': cover})}")
        return True

    status, _ = api("GET", f"/models/{slug}", token)
    if status == 200:
        print(f"• {slug}: exists")
    elif status == 404:
        if not ensure_created(slug, create_payload, token):
            return False
    else:
        # GET can be unreliable for some tokens/CDN paths (e.g. 403); fall back to create-or-conflict.
        print(f"… {slug}: GET returned {status}; attempting create-or-update", file=sys.stderr)
        if not ensure_created(slug, create_payload, token):
            return False

    u_status, u_body = api("PATCH", f"/models/{slug}", token, update_payload)
    if u_status == 200:
        print(f"✓ {slug}: metadata synced (description, readme, urls)")
    else:  # non-fatal: the model exists/pushes fine even if the page text lagged
        print(f"⚠ {slug}: metadata PATCH failed ({u_status}): {u_body}", file=sys.stderr)

    # cover_image_url is documented as create-only; attempt it on update too as a SEPARATE best-effort request so a
    # rejection can't block the metadata sync above. Re-asserts the logo on every model each run (resetting a cover that
    # drifted to a prediction output, and migrating already-existing models to the current logo).
    cover = create_payload.get("cover_image_url")
    if cover:
        c_status, _ = api("PATCH", f"/models/{slug}", token, {"cover_image_url": cover})
        if c_status == 200:
            print(f"✓ {slug}: cover_image_url update accepted")
        else:
            print(f"⚠ {slug}: cover_image_url update not accepted ({c_status}); set cover in web UI", file=sys.stderr)
    return True


def main() -> int:
    """Parse args and sync Replicate metadata for one or all models."""
    parser = argparse.ArgumentParser(description="Create and sync Replicate model metadata.")
    parser.add_argument("--dir", help="Sync a single model directory (e.g. 'yolo26/seg'); default syncs all.")
    parser.add_argument("--dry-run", action="store_true", help="Print payloads without calling the API.")
    args = parser.parse_args()

    root = Path(__file__).parent
    token = os.environ.get("REPLICATE_API_TOKEN", "")
    if not token and not args.dry_run:
        print("REPLICATE_API_TOKEN is not set", file=sys.stderr)
        return 1

    try:
        models = discover_models(root, args.dir)
    except (FileNotFoundError, ValueError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 1
    print(f"Syncing {len(models)} model(s): {', '.join(f'{o}/{n}' for o, n, _ in models)}")
    ok = all(sync(owner, name, d, token, args.dry_run) for owner, name, d in models)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
