# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

import tempfile
from pathlib import Path as PathLib

from cog import BasePredictor, Input, Path
from ultralytics import YOLO


class Predictor(BasePredictor):
    def setup(self):
        """Load YOLO model into memory."""
        # Use ONNX for GPU-agnostic acceleration
        self.model = YOLO("yolo11n.onnx")

    def predict(
        self,
        image: Path = Input(description="Input image"),
        conf: float = Input(description="Confidence threshold", default=0.25, ge=0.0, le=1.0),
        iou: float = Input(description="IoU threshold for NMS", default=0.45, ge=0.0, le=1.0),
        imgsz: int = Input(description="Image size", default=640, choices=[320, 416, 512, 640, 832, 1024, 1280]),
    ) -> Path:
        """Run YOLO inference on input image."""
        results = self.model(str(image), conf=conf, iou=iou, imgsz=imgsz)

        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as f:
            output_path = PathLib(f.name)
            results[0].save(str(output_path))
            return Path(output_path)
