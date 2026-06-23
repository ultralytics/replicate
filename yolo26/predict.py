# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from __future__ import annotations

from cog import BaseModel, BasePredictor, Input, Path
from ultralytics import YOLO


class Output(BaseModel):
    """Output model for predictions."""

    image: Path | None = None
    json_str: str | None = None


class Predictor(BasePredictor):
    """YOLO26 model predictor for Replicate deployment with selectable model size (n/s/m/l/x)."""

    def setup(self) -> None:
        """Load the default YOLO26 model into memory."""
        self.model_size = "n"
        self.model = YOLO(f"yolo26{self.model_size}.pt")

    def re_init_model(self, model_size: str) -> None:
        """Reload the model only if the requested size differs from the currently loaded one."""
        if model_size != self.model_size:
            self.model = YOLO(f"yolo26{model_size}.pt")
            self.model_size = model_size

    def predict(
        self,
        image: Path = Input(description="Input image"),
        model_size: str = Input(
            description="Model size (n=nano, s=small, m=medium, l=large, x=extra-large)",
            default="n",
            choices=["n", "s", "m", "l", "x"],
        ),
        conf: float = Input(description="Confidence threshold", default=0.25, ge=0.0, le=1.0),
        iou: float = Input(description="IoU threshold for NMS", default=0.45, ge=0.0, le=1.0),
        imgsz: int = Input(description="Image size", default=640, choices=[320, 416, 512, 640, 832, 1024, 1280]),
        return_json: bool = Input(description="Return detection results as JSON", default=False),
    ) -> Output:
        """Run inference and return annotated image with optional JSON results."""
        self.re_init_model(model_size)
        result = self.model(str(image), conf=conf, iou=iou, imgsz=imgsz)[0]
        image_path = "output.png"
        result.save(image_path)

        if return_json:
            return Output(image=Path(image_path), json_str=result.to_json())
        else:
            return Output(image=Path(image_path))
