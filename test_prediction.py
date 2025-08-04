# Ultralytics 🚀 AGPL-3.0 License - https://ultralytics.com/license
"""
Test YOLO model predictions locally before deploying to Replicate.

Usage:
    python test_prediction.py --model yolo11n --image test.jpg
    python test_prediction.py --model custom --image test.jpg
"""

import argparse
import sys
from pathlib import Path

# Add model directories to path
sys.path.append(str(Path(__file__).parent))


def test_prediction(model_dir: str, image_path: str) -> None:
    """Test prediction locally."""
    try:
        # Import the predictor from the specified model directory
        model_path = Path(model_dir)
        if not model_path.exists():
            print(f"❌ Model directory {model_dir} not found")
            return

        # Check for model files
        pt_files = list(model_path.glob("*.pt"))
        if not pt_files:
            print(f"❌ No PyTorch model files found in {model_dir}")
            if model_dir == "yolo11n":
                print("💡 Make sure yolo11n.pt is in the yolo11n/ directory")
            else:
                print("💡 Make sure your custom .pt model is in the custom/ directory")
            return

        print(f"✅ Found PyTorch models: {[f.name for f in pt_files]}")

        # Import and test the predictor
        sys.path.insert(0, str(model_path))
        from predict import Predictor

        predictor = Predictor()
        predictor.setup()

        # Test prediction
        from cog import Path as CogPath

        result = predictor.predict(image=CogPath(image_path))

        print(f"✅ Prediction successful: {result}")
        print(f"💡 Ready to deploy: cd {model_dir} && cog push r8.im/your-username/your-model")

    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Make sure you have ultralytics installed: pip install ultralytics")
    except Exception as e:
        print(f"❌ Prediction failed: {e}")


def main():
    """Main function."""
    parser = argparse.ArgumentParser(description="Test YOLO predictions locally")
    parser.add_argument("--model", required=True, choices=["yolo11n", "custom"], help="Model directory to test")
    parser.add_argument("--image", required=True, help="Path to test image")

    args = parser.parse_args()

    if not Path(args.image).exists():
        print(f"❌ Image file {args.image} not found")
        return

    test_prediction(args.model, args.image)


if __name__ == "__main__":
    main()
