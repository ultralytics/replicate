# Custom YOLO Model Deployment

Deploy your own custom-trained YOLO models to Replicate. This example shows how to deploy a model trained on your own dataset.

## Setup

1. **Train your custom model** (or use existing `best.pt`)
2. **Export your custom model to ONNX:**

   ```bash
   yolo export model=best.pt format=onnx
   ```

3. **Add model weights to this directory:**

   ```bash
   cp best.onnx ./
   ```

4. **Update the model name in `predict.py`** if different from `best.onnx`

5. **Update `cog.yaml`** with your desired image name:

   ```yaml
   image: "r8.im/your-username/your-custom-model"
   ```

6. **Deploy to Replicate:**
   ```bash
   cog push r8.im/your-username/your-custom-model
   ```

## Custom Model Examples

- **Object Detection**: Custom classes trained on your specific dataset
- **Fine-tuned Models**: YOLO models adapted for specific domains
- **Specialized Detection**: Models for specific industries or use cases

## Model Files

Place your custom model files in this directory:

- `best.onnx` - Your custom trained model (exported from `best.pt`)
- `predict.py` - Update model name if different
- `cog.yaml` - Update image name for your deployment

## Configuration

- **GPU**: Enabled by default for optimal inference speed
- **Format**: ONNX for cross-GPU compatibility
- **Python**: 3.11 with PyTorch 2.0+
- **Framework**: Ultralytics 8.3+
- **Custom Classes**: Automatically detected from your model

## Customization Tips

1. **Model Name**: Update `self.model = YOLO("best.onnx")` in `predict.py`
2. **Input Parameters**: Modify confidence/IoU defaults based on your model
3. **Output Format**: Customize result visualization if needed
4. **Deployment Name**: Choose descriptive names for easy identification

This template demonstrates how any YOLO model can be easily deployed to Replicate!
