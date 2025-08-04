from cog import BasePredictor, Input, Path
from ultralytics import YOLO
from pathlib import Path as PathLib
import tempfile


class Predictor(BasePredictor):
    def setup(self):
        """Load custom YOLO model into memory"""
        # Use ONNX for GPU-agnostic acceleration
        # Replace 'best.onnx' with your custom model name
        self.model = YOLO("best.onnx")

    def predict(
        self,
        image: Path = Input(description="Input image"),
        conf: float = Input(description="Confidence threshold", default=0.25, ge=0.0, le=1.0),
        iou: float = Input(description="IoU threshold for NMS", default=0.45, ge=0.0, le=1.0),
        imgsz: int = Input(description="Image size", default=640, choices=[320, 416, 512, 640, 832, 1024, 1280])
    ) -> Path:
        """Run YOLO inference on input image"""
        results = self.model(str(image), conf=conf, iou=iou, imgsz=imgsz)
        
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as f:
            output_path = PathLib(f.name)
            results[0].save(str(output_path))
            return Path(output_path)
