# YOLO11n Demo Deployment

Deploy the official YOLO11n model to Replicate with optimized ONNX inference.

## Setup

1. **Export the official YOLO11n model to ONNX:**

   ```bash
   yolo export model=yolo11n.pt format=onnx
   ```

2. **Add model weights to this directory:**

   ```bash
   cp yolo11n.onnx ./
   ```

3. **Deploy to Replicate:**
   ```bash
   cog push r8.im/ultralytics/yolo11n
   ```

## Model Details

- **Model**: YOLO11n (Nano)
- **Parameters**: 2.6M
- **Format**: ONNX for cross-GPU compatibility
- **Use Case**: Demonstration of official Ultralytics model deployment

## Model Files

**Note:** Model weight files (`.onnx`) are not included in this repository. Export the official model using the Ultralytics library as shown above.

## Configuration

- **GPU**: Enabled by default for optimal inference speed
- **Python**: 3.11 with PyTorch 2.0+
- **Framework**: Ultralytics 8.3+
- **Input**: Single image with configurable confidence/IoU thresholds
- **Output**: Annotated image with detected objects
