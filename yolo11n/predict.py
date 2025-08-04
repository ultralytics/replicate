# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

import tempfile
from typing import Any, Dict

from cog import BasePredictor, Input, Path
from ultralytics import YOLO


class Predictor(BasePredictor):
    """YOLO11n model predictor for Replicate deployment."""

    def setup(self) -> None:
        """Load YOLO model into memory."""
        self.model = YOLO("yolo11n.pt")

    def predict(
        self,
        image: Path = Input(description="Input image"),
        conf: float = Input(description="Confidence threshold", default=0.25, ge=0.0, le=1.0),
        iou: float = Input(description="IoU threshold for NMS", default=0.45, ge=0.0, le=1.0),
        imgsz: int = Input(description="Image size", default=640, choices=[320, 416, 512, 640, 832, 1024, 1280]),
        return_json: bool = Input(description="Return detection results as JSON", default=False),
    ) -> Dict[str, Any]:
        """Run inference and return annotated image with optional JSON results."""
        result = self.model(str(image), conf=conf, iou=iou, imgsz=imgsz)[0]

        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as f:
            output_path = Path(f.name)
            result.save(str(output_path))

        if return_json:
            json_str = result.to_json()  # Already a JSON string
            return {"json_str": json_str, "media_path": None}
        else:
            return {"json_str": None, "media_path": output_path}
