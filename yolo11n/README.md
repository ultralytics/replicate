# YOLO11n Demo Deployment

Deploy the official YOLO11n model to Replicate with PyTorch inference at https://replicate.com/ultralytics/yolo11n.

## Setup

1. **Deploy to Replicate:**
   ```bash
   cog push r8.im/ultralytics/yolo11n
   ```

## Model Details

- **Model**: YOLO11n (Nano)
- **Parameters**: 2.6M
- **Format**: PyTorch (.pt)
- **Use Case**: Demonstration of official Ultralytics model deployment

## Model Files

**Note:** The model weights (`yolo11n.pt`) will be automatically downloaded by ultralytics when the container starts.

## Configuration

- **GPU**: Disabled by default (CPU inference)
- **Python**: 3.11 with PyTorch 2.0+
- **Framework**: Ultralytics 8.3+
- **Input**: Single image with configurable confidence/IoU thresholds
- **Output**: Annotated image with detected objects
