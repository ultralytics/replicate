# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from pathlib import Path

from ultralytics import YOLOWorld


def main():
    """Download YOLOv8s-worldv2 weights and move to model directory."""
    current_dir = Path(__file__).parent
    YOLOWorld(current_dir / "yolov8s-worldv2.pt")

    # List files in model directory
    print(f"Files in {current_dir.name} directory:")
    for file in sorted(current_dir.iterdir()):
        print(f"  {file.stat().st_size:>10} {file.name}")


if __name__ == "__main__":
    main()
