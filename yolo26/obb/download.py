# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license

from pathlib import Path

from ultralytics import YOLO


def main():
    """Download all YOLO26 oriented bounding box (n/s/m/l/x) weights and move to model directory."""
    current_dir = Path(__file__).parent
    for size in ("n", "s", "m", "l", "x"):
        YOLO(current_dir / f"yolo26{size}-obb.pt")

    # List files in model directory
    print(f"Files in {current_dir.name} directory:")
    for file in sorted(current_dir.iterdir()):
        print(f"  {file.stat().st_size:>10} {file.name}")


if __name__ == "__main__":
    main()
