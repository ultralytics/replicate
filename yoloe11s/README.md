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

**Note:** The model weights (`yoloe-11s-seg.pt` and `yoloe-11s-seg-pf.pt`) will be downloaded before the container builds.

## Configuration

- **GPU**: Disabled by default (CPU inference)
- **Python**: 3.12 with PyTorch 2.3.1+
- **Framework**: Ultralytics 8.3+
- **Input**: Single image with configurable confidence/IoU thresholds, image size, and class names.
- **Output**: Annotated image with detected objects
