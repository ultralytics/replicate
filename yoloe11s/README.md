# YOLO11n Demo Deployment

Deploy the official YOLO11n model to Replicate with PyTorch inference at https://replicate.com/ultralytics/yoloe11s.

## Setup

1. **Deploy to Replicate:**

   ```bash
   cog push r8.im/ultralytics/yoloe11s
   ```

## Model Details

- **Model**: YOLE11s (Small)
- **Parameters**: 2.6M
- **Format**: PyTorch (.pt)
- **Use Case**: Demonstration of official Ultralytics model deployment

## Model Files

**Note:** The model weights (`yoloe-11s-seg.pt`) and (`mobileclip_blt.ts`) will be automatically downloaded by ultralytics when the container starts.

## Configuration

- **GPU**: Disabled by default (CPU inference)
- **Python**: 3.12 with PyTorch 2.3.1+
- **Framework**: Ultralytics 8.3+
- **Input**: Single image with configurable confidence/IoU thresholds, image size, and class names.
- **Output**: Annotated image with detected objects
