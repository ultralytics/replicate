# YOLOv8s WorldV2 Demo Deployment

Deploy the official YOLOv8s WorldV2 model to Replicate with PyTorch inference at https://replicate.com/ultralytics/yolov8s-worldv2.

## Setup

1. **Deploy to Replicate:**

   ```bash
   cog push r8.im/ultralytics/yolov8s-worldv2
   ```

## Model Details

- **Model**: YOLOv8s WorldV2 (Small)
- **Parameters**: 12.7M
- **Format**: PyTorch (.pt)
- **Use Case**: Demonstration of official Ultralytics model deployment

## Model Files

**Note:** The model weights (`yolov8s-worldv2.pt`) will be automatically downloaded by ultralytics when the container starts.

## Configuration

- **GPU**: Disabled by default (CPU inference)
- **Python**: 3.12 with PyTorch 2.3.1+
- **Framework**: Ultralytics 8.3+
- **Input**: Single image with configurable confidence/IoU thresholds
- **Output**: Annotated image with detected objects
