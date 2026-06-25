# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repo packages Ultralytics YOLO models for deployment to [Replicate](https://replicate.com) using [Cog](https://github.com/replicate/cog). It is a deployment/packaging repo, not a library — there is no installable package and no application code beyond the per-model Cog predictors.

## Architecture

Each model lives in its own self-contained directory with an identical four-file layout. The singleton models are top-level (`yolo11n/`, `yolov8s-worldv2/`, `yoloe11s/`); the YOLO26 task family is grouped one level deeper under `yolo26/` — `yolo26/detect/`, `yolo26/seg/`, `yolo26/sem/`, `yolo26/cls/`, `yolo26/pose/`, `yolo26/obb/`. The four files in every leaf dir:

- `cog.yaml` — Cog build config: Python version, system/python packages, and the `image:` target (e.g. `r8.im/ultralytics/yolo11n`). All run CPU-only (`gpu: false`).
- `predict.py` — the Cog `Predictor`. `setup()` loads weights into memory once; `predict()` runs inference per request.
- `download.py` — run **before** `cog build`. It instantiates the model class with a path inside the directory, which triggers Ultralytics to auto-download the `.pt` weights there so Cog bundles them into the image. Weights are gitignored, never committed.
- `README.md` — Replicate model card.

All predictors share the same `Output` model (`image: Path`, `json_str: str`) and a common `predict()` signature (`image`, `conf`, `iou`, `imgsz`, `return_json`; open-vocab models add `class_names`; the YOLO26 family adds `model_size`). Inference always saves an annotated `output.png` and optionally attaches `result.to_json()`.

Key difference between models:

- **`yolo11n`** (`YOLO`) — fixed COCO classes. Model loaded once in `setup()`.
- **`yolov8s-worldv2`** (`YOLOWorld`) and **`yoloe11s`** (`YOLOE`) — open-vocabulary. They define `re_init_model(class_names)`, which **rebuilds the model on every prediction request** to apply the requested classes via `set_classes(...)`. `yoloe11s` additionally falls back to the prompt-free weights (`yoloe-11s-seg-pf.pt`) when `class_names` is empty, so it downloads two `.pt` files.
- **`yolo26/<task>`** (`YOLO`) — one deployment per task (detect/seg/sem/cls/pose/obb), all using the unified `YOLO` class with the task auto-inferred from the weight suffix (`yolo26n-seg.pt`, `yolo26n-cls.pt`, …). Each exposes runtime size selection via `model_size` (n/s/m/l/x) and defines `re_init_model(model_size)`, which reloads weights only when the requested size changes; `download.py` stages all five sizes for that task. `conf`/`iou` are accepted but ignored by the `cls`/`sem` tasks — kept so the signature and the CI smoke-test command stay uniform across all models. Per-task `imgsz` defaults differ (detect/seg/pose 640, obb 1024, cls 224, sem 640).

Got you: directory names and Replicate image names don't always match — `yoloe11s/` deploys to `r8.im/ultralytics/yoloe-11s`; `yolo26/detect/` to `r8.im/ultralytics/yolo26` and `yolo26/seg/` to `r8.im/ultralytics/yolo26-seg`. `cog push` with no argument uses the `image:` field in that directory's `cog.yaml`, so always run cog commands from inside the leaf model directory.

## Commands

Local test (only `yolo11n` and `custom` are supported by this script):

```bash
python yolo11n/download.py
python test_prediction.py --model yolo11n --image assets/bus.jpg
```

Build, test, and deploy a single model (run from inside the model dir):

```bash
cd yolo11n
python download.py # fetch weights first — build will not download them
cog build
cog predict -i image=@../assets/bus.jpg -i conf=0.25 -i iou=0.45
cog login # one-time, needs REPLICATE_API_TOKEN
cog push  # pushes to the image: target in cog.yaml
```

Install Cog itself (see README for the OS-specific download line). Python deps for local scripts: `pip install -r requirements.txt`.

## CI/CD

- `.github/workflows/push.yml` — the deployment pipeline. Runs a matrix over `[yolo11n, yolov8s-worldv2, yoloe11s, yolo26/detect, yolo26/seg, yolo26/sem, yolo26/cls, yolo26/pose, yolo26/obb]`: for each, downloads weights, `cog build`, `cog predict` smoke test against `$GITHUB_WORKSPACE/assets/bus.jpg` (absolute path, so it resolves from both top-level and nested model dirs), then `cog push` **only on `main`** (PRs build and test but do not push). Requires the `REPLICATE_API_TOKEN` secret.
- `.github/workflows/ci.yml` — lightweight checks across OSes/Python versions: compiles `test_prediction.py`, imports the yolo11n predictor, validates every `cog.yaml` (recursive glob).
- `.github/workflows/format.yml` — Ultralytics Actions auto-formats PRs (Ruff + docformatter for Python; Prettier for YAML/JSON/Markdown) and runs codespell. Formatting is applied in CI, so match existing style rather than configuring a local formatter.

## Conventions

- Every source file starts with the header comment `# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license`.
- When adding a new model, copy an existing model directory (for a new YOLO26 task, copy a `yolo26/<task>/` sibling), then update `cog.yaml` (`image:` and any extra `python_packages`), `predict.py` (model class and weights filename), and `download.py` — and add the directory path to the matrix in `push.yml` (use the full nested path, e.g. `yolo26/seg`).
- CI smoke tests reference the sample image by absolute path (`$GITHUB_WORKSPACE/assets/bus.jpg`) so the same command works regardless of model-dir depth. Running `cog predict` by hand from a nested `yolo26/<task>/` dir needs `../../assets/bus.jpg` (top-level dirs use `../assets/bus.jpg`).
