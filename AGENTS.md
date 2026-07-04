# AGENTS.md

This file provides guidance to AI coding agents (Claude Code, etc.) when working with code in this repository. CLAUDE.md is a symlink to this file.

## Core Principles (CRITICAL)

Respecting these principles is critical for every PR.

**Less is more. The simplest solution is the best solution.**

The action hierarchy for every change: **Delete > Replace > Add**. The best code change is a deletion. The second best is modifying what exists. Adding new code is the last resort.

1. **Minimal**: The simplest solution that works. Do not over-engineer, over-abstract, or add code just in case. Three similar lines beat a premature abstraction. Avoid error handling for impossible states, feature flags, compatibility shims, or policy scaffolding unless they are truly required.
2. **Solve at the source**: Do not hack fixes. Solve problems at their root. If something is broken, fix or remove the broken thing. Never patch over a broken abstraction, add workarounds, or add synchronization code for state that should not be duplicated.
3. **Delete ruthlessly**: When replacing code, delete what it replaced. Remove unused imports, functions, types, files, and commented-out code. Git preserves history. Run the repo's relevant dead-code or cleanup check when available.
4. **Replace > Add**: Modify existing code over adding new code. Edit existing files, extend existing components or functions with minimal parameters, and reuse existing utilities. If creating a new file, first prove it cannot fit cleanly in an existing file.
5. **Check existing**: Search the entire repo before creating anything new. If a feature, component, helper, responder, workflow, or utility already solves a similar problem, reuse or adapt it and delete the duplicate path.
6. **Deduplicate**: Do not duplicate existing code when updating the repo. Consolidate or refactor duplicates you find when it is in scope and low risk.
7. **Zero Regression**: Do not break existing features or workflows unless the PR intentionally removes them with evidence.
8. **Production ready**: All changes must be thoroughly debugged, validated, and production ready.

**When fixing bugs, ask: "What can I delete?" before "What can I replace?" before "What should I add?"**

## PR Workflow

After opening a PR:

1. Wait for the automated PR review and auto-format commit from Ultralytics Actions (`format.yml`), then pull and address every finding.
2. Launch an independent adversarial review agent with cold context (just the PR diff and this file) to hunt for bugs, regressions, and Core Principles violations — use the Codex CLI, one fresh `codex exec` run per round. Fix, push, and repeat until a fresh run reports LGTM.
3. Never fight other commits: Ultralytics Actions pushes auto-format and header commits, and multiple users may work on the same PR. `git pull --rebase` before pushing; never force-push, reset, or revert commits you did not author.
4. After the PR merges, clean up: remove local worktrees and branches for it, then `git checkout main && git pull`.

## Commands

```bash
# Install local script dependencies (CPU-only torch; never bare pip install)
uv pip install -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

# Local smoke test (test_prediction.py supports only yolo11n and custom)
python yolo11n/download.py
python test_prediction.py --model yolo11n --image assets/bus.jpg

# Build, test, and deploy one model — run from inside the leaf model dir, weights first
cd yolo11n && python download.py && cog build
cog predict -i image=@../assets/bus.jpg -i conf=0.25 -i iou=0.45 -i return_json=true # ../../assets from yolo26/<task>/
cog push                                                                             # pushes to the image: target in cog.yaml; needs cog login / REPLICATE_API_TOKEN

# CI-equivalent checks (mirrors .github/workflows/ci.yml)
python -m py_compile test_prediction.py && python test_prediction.py --help
python -m py_compile replicate_metadata.py && python replicate_metadata.py --dry-run
python -c "from yolo11n.predict import Predictor"
python -c "import glob, yaml; [yaml.safe_load(open(f)) for f in sorted(glob.glob('**/cog.yaml', recursive=True))]"
```

- CI (`ci.yml`) runs the checks above on a matrix of ubuntu/macos/windows × Python 3.11/3.12; the deploy pipeline (`push.yml`) uses Python 3.12.
- There is no pytest suite, no coverage upload, and no local formatter config — formatting is applied to PRs in CI by Ultralytics Actions.

## Architecture

This repo packages Ultralytics YOLO models for deployment to [Replicate](https://replicate.com) using [Cog](https://github.com/replicate/cog). It is a deployment/packaging repo, not a library — there is no installable package and no application code beyond the per-model Cog predictors plus two top-level scripts (`test_prediction.py`, `replicate_metadata.py`).

Each model lives in a self-contained directory with an identical four-file layout: `cog.yaml` (build config and `image:` push target; all models run CPU-only with `gpu: false`), `predict.py` (the Cog `Predictor`), `download.py` (run **before** `cog build` — instantiates the model class with a path inside the directory so Ultralytics auto-downloads the gitignored `.pt` weights there for Cog to bundle), and `README.md` (the Replicate model card). Singletons are top-level (`yolo11n/`, `yolov8s-worldv2/`, `yoloe11s/`); the YOLO26 task family is nested under `yolo26/` (`detect`, `seg`, `sem`, `cls`, `pose`, `obb`).

All predictors share the same `Output` model (`image`, `json_str`) and `predict()` signature (`image`, `conf`, `iou`, `imgsz`, `return_json`); open-vocab models add `class_names`, the YOLO26 family adds `model_size`. Key per-model differences:

- **`yolo11n`** (`YOLO`) — fixed COCO classes, model loaded once in `setup()`.
- **`yolov8s-worldv2`** (`YOLOWorld`) and **`yoloe11s`** (`YOLOE`) — open-vocabulary; `re_init_model(class_names)` rebuilds the model on **every** request to apply `set_classes(...)`. `yoloe11s` falls back to prompt-free weights (`yoloe-11s-seg-pf.pt`) when `class_names` is empty, so it stages two `.pt` files. Both need the extra `clip` git package in `cog.yaml`.
- **`yolo26/<task>`** (`YOLO`) — one deployment per task; `re_init_model(model_size)` reloads weights only when the requested size (n/s/m/l/x) changes, and `download.py` stages all five sizes. `conf`/`iou` are accepted but ignored by `cls`/`sem` — kept so the signature and CI smoke test stay uniform. Per-task `imgsz` defaults: detect/seg/sem/pose 640, obb 1024, cls 224.

Directory names and Replicate image names don't always match — `yoloe11s/` → `r8.im/ultralytics/yoloe-11s`, `yolo26/detect/` → `r8.im/ultralytics/yolo26`. `cog push` with no argument uses the `image:` field in that directory's `cog.yaml`, so run cog commands from inside the leaf model dir.

Deploy pipeline (`push.yml`): triggers on push/PR to `main` and `workflow_dispatch`, with a fail-fast-disabled matrix over all nine model dirs. Every run downloads weights, `cog build`s, and smoke-tests `cog predict` against `$GITHUB_WORKSPACE/assets/bus.jpg`; because `cog predict` exits 0 even when the prediction raises, the test step greps the log for a traceback and fails on it. Two steps are gated on `github.ref == 'refs/heads/main'` (PRs build and test but never publish): `replicate_metadata.py --dir <model>` (creates the Replicate model if missing so `cog push` succeeds, then PATCHes description/readme/links) and `cog push`. The metadata script must send a custom `User-Agent` (Replicate's CDN 403s the default urllib UA from CI IPs), and `cover_image_url` is create-only — PATCH returns 200 but silently ignores it.

## Conventions

- Every source file starts with `# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license` — Ultralytics Actions adds it automatically; don't add or revert it manually.
- Formatting is applied to PRs in CI by `format.yml` (Ultralytics Actions: Ruff + docformatter for Python, Prettier for YAML/JSON/Markdown, codespell) — match existing style rather than configuring a local formatter.
- Predictors use `from __future__ import annotations`, which breaks Cog's pydantic schema for `Output` unless `Output.update_forward_refs(Path=Path)` follows the class — keep that line when copying a predictor.
- New model: copy an existing model dir (for a YOLO26 task, a `yolo26/<task>/` sibling), update `cog.yaml` (`image:`, extra `python_packages`), `predict.py`, and `download.py`, add the dir path to the `push.yml` matrix (full nested path, e.g. `yolo26/seg`), and add a `SPECS` entry in `replicate_metadata.py`.
- No versioned releases — merging to `main` is the release: every merge builds, tests, and pushes all nine images to Replicate (requires the `REPLICATE_API_TOKEN` secret).
- `download.py` and `cog predict`/`cog build` hit the live network (weight downloads, Docker); `replicate_metadata.py` without `--dry-run` calls the live Replicate API.
