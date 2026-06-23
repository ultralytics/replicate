# YOLO26 Demo Deployment

Deploy the official YOLO26 model to Replicate with PyTorch inference at <https://replicate.com/ultralytics/yolo26>.

## Setup

1. **Deploy to Replicate:**

   ```bash
   cog push r8.im/ultralytics/yolo26
   ```

## Model Details

- **Model**: YOLO26 (selectable size: n/s/m/l/x)
- **Format**: PyTorch (.pt)
- **Use Case**: Demonstration of official Ultralytics model deployment with runtime size selection

## Model Files

**Note:** `download.py` stages all five YOLO26 weights (`yolo26n.pt`, `yolo26s.pt`, `yolo26m.pt`, `yolo26l.pt`, `yolo26x.pt`)
before the container builds. The predictor loads `yolo26n.pt` on startup and only reloads when a request selects a
different size, so repeated requests at the same size incur no reload cost.

## Configuration

- **GPU**: Disabled by default (CPU inference)
- **Python**: 3.12 with PyTorch 2.0+
- **Framework**: Ultralytics 8.4.75+
- **Input**: Single image with selectable model size and configurable confidence/IoU thresholds and image size
- **Output**: Annotated image with detected objects
