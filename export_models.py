# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

"""
Export YOLO models to ONNX format for Replicate deployment.

Usage:
    python export_models.py --model yolo11n.pt --output yolo11n/
    python export_models.py --model best.pt --output custom/
"""

import argparse
from pathlib import Path

from ultralytics import YOLO


def export_model(model_path: str, output_dir: str) -> None:
    """Export YOLO model to ONNX format."""
    model = YOLO(model_path)
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True)

    # Export to ONNX
    model.export(format="onnx", imgsz=640)

    # Move exported file to output directory
    model_name = Path(model_path).stem
    exported_file = Path(model_path).parent / f"{model_name}.onnx"
    target_file = output_path / f"{model_name}.onnx"

    if exported_file.exists():
        exported_file.rename(target_file)
        print(f"✅ Exported {model_path} to {target_file}")
    else:
        print(f"❌ Export failed for {model_path}")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Export YOLO models to ONNX for Replicate")
    parser.add_argument("--model", required=True, help="Path to YOLO model (.pt file)")
    parser.add_argument(
        "--output", required=True, choices=["yolo11n", "custom"], help="Output directory (yolo11n or custom)"
    )

    args = parser.parse_args()
    export_model(args.model, args.output)


if __name__ == "__main__":
    main()
