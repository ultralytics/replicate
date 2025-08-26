# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from typing import Optional

from cog import BaseModel, BasePredictor, Input, Path
from ultralytics import YOLOE


class Output(BaseModel):
    """Output model for predictions."""

    image: Optional[Path] = None
    json_str: Optional[str] = None


class Predictor(BasePredictor):
    """YOLOE: Real-Time Seeing Anything model predictor for Replicate deployment."""

    def setup(self) -> None:
        """Load YOLOE-11S model into memory."""
        self.model = YOLOE("yoloe-11s-seg.pt")

    def re_init_model(self, class_names: str) -> None:
        """Re-Initialize model with class names."""
        if not class_names.strip():
            # Load YOLOE-11s model prompt free model into memory
            self.model = YOLOE("yoloe-11s-seg-pf.pt")

        else:
            self.model = YOLOE("yoloe-11s-seg.pt")
            class_list = class_names.split(", ")
            self.model.set_classes(class_list, self.model.get_text_pe(class_list))

    def predict(
        self,
        image: Path = Input(description="Input image"),
        conf: float = Input(description="Confidence threshold", default=0.25, ge=0.0, le=1.0),
        iou: float = Input(description="IoU threshold for NMS", default=0.45, ge=0.0, le=1.0),
        imgsz: int = Input(description="Image size", default=640, choices=[320, 416, 512, 640, 832, 1024, 1280]),
        class_names: str = Input(
            description="Comma-separated list of class names to filter results (e.g., 'person, bus, sign') You can also leave it empty to detect classes automatically.",
            default="person, bus, sign",
        ),
        return_json: bool = Input(description="Return detection results as JSON", default=False),
    ) -> Output:
        """Run inference and return annotated image with optional JSON results."""
        self.re_init_model(class_names)
        result = self.model(str(image), conf=conf, iou=iou, imgsz=imgsz)[0]
        image_path = "output.png"
        result.save(image_path)

        if return_json:
            return Output(image=Path(image_path), json_str=result.to_json())
        else:
            return Output(image=Path(image_path))
