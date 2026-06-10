# YOLOE-11S Demo Deployment

Deploy the official YOLOE-11S model to Replicate with PyTorch inference at <https://replicate.com/ultralytics/yoloe-11s>.

## Setup

1. **Deploy to Replicate:**

   ```bash
   cog push r8.im/ultralytics/yoloe-11s
   ```

## Model Details

- **Model**: YOLOE-11S (Small)
- **Parameters**: 10.2M
- **Format**: PyTorch (.pt)
- **Use Case**: Demonstration of official Ultralytics model deployment

## Model Files

**Note:** `download.py` stages the YOLOE weights (`yoloe-11s-seg.pt` and `yoloe-11s-seg-pf.pt`) before the container builds.
The Cog environment installs the CLIP dependency configured in `cog.yaml` for prompt-based inference.

## Configuration

- **GPU**: Disabled by default (CPU inference)
- **Python**: 3.12 with PyTorch 2.3.1+
- **Framework**: Ultralytics 8.3+
- **Input**: Single image with configurable confidence/IoU thresholds, image size, and class names.
- **Output**: Annotated image with detected objects
