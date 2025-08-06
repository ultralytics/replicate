from pathlib import Path
from ultralytics import YOLO

def main():
    """Download YOLO11n weights and move to model directory."""
    model = YOLO(Path(__file__).parent / 'yolo11n.pt')
    
    # List files in model directory
    print(f"Files in {current_dir.name} directory:")
    for file in sorted(current_dir.iterdir()):
        print(f"  {file.stat().st_size:>10} {file.name}")

if __name__ == '__main__':
    main()
