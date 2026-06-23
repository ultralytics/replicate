# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

This repo packages Ultralytics YOLO models for deployment to [Replicate](https://replicate.com) using [Cog](https://github.com/replicate/cog). It is a deployment/packaging repo, not a library — there is no installable package and no application code beyond the per-model Cog predictors.

## Architecture

Each model lives in its own self-contained directory (`yolo11n/`, `yolov8s-worldv2/`, `yoloe11s/`) with an identical four-file layout:

- `cog.yaml` — Cog build config: Python version, system/python packages, and the `image:` target (e.g. `r8.im/ultralytics/yolo11n`). All run CPU-only (`gpu: false`).
- `predict.py` — the Cog `Predictor`. `setup()` loads weights into memory once; `predict()` runs inference per request.
- `download.py` — run **before** `cog build`. It instantiates the model class with a path inside the directory, which triggers Ultralytics to auto-download the `.pt` weights there so Cog bundles them into the image. Weights are gitignored, never committed.
- `README.md` — Replicate model card.

All three predictors share the same `Output` model (`image: Path`, `json_str: str`) and the same `predict()` signature (`image`, `conf`, `iou`, `imgsz`, `return_json`; open-vocab models add `class_names`). Inference always saves an annotated `output.png` and optionally attaches `result.to_json()`.

Key difference between models:

- **`yolo11n`** (`YOLO`) — fixed COCO classes. Model loaded once in `setup()`.
- **`yolov8s-worldv2`** (`YOLOWorld`) and **`yoloe11s`** (`YOLOE`) — open-vocabulary. They define `re_init_model(class_names)`, which **rebuilds the model on every prediction request** to apply the requested classes via `set_classes(...)`. `yoloe11s` additionally falls back to the prompt-free weights (`yoloe-11s-seg-pf.pt`) when `class_names` is empty, so it downloads two `.pt` files.

Got you: directory names and Replicate image names don't always match — `yoloe11s/` deploys to `r8.im/ultralytics/yoloe-11s`. `cog push` with no argument uses the `image:` field in that directory's `cog.yaml`, so always run cog commands from inside the model directory.

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

- `.github/workflows/push.yml` — the deployment pipeline. Runs a matrix over `[yolo11n, yolov8s-worldv2, yoloe11s]`: for each, downloads weights, `cog build`, `cog predict` smoke test against `assets/bus.jpg`, then `cog push` **only on `main`** (PRs build and test but do not push). Requires the `REPLICATE_API_TOKEN` secret.
- `.github/workflows/ci.yml` — lightweight checks across OSes/Python versions: compiles `test_prediction.py`, imports the yolo11n predictor, validates `cog.yaml` YAML.
- `.github/workflows/format.yml` — Ultralytics Actions auto-formats PRs (Ruff + docformatter for Python; Prettier for YAML/JSON/Markdown) and runs codespell. Formatting is applied in CI, so match existing style rather than configuring a local formatter.

## Conventions

- Every source file starts with the header comment `# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license`.
- When adding a new model, copy an existing model directory, then update `cog.yaml` (`image:` and any extra `python_packages`), `predict.py` (model class and weights filename), and `download.py` — and add the directory name to the matrix in `push.yml`.
