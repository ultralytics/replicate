<a href="https://www.ultralytics.com/"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# 🚀 Ultralytics Replicate

Deploy YOLO models to Replicate with ready-to-use Cog configurations and automated CI/CD workflows.

[![Push YOLO to Replicate](https://github.com/ultralytics/replicate/actions/workflows/push.yml/badge.svg)](https://github.com/ultralytics/replicate/actions/workflows/push.yml)
[![Push All YOLO Models](https://github.com/ultralytics/replicate/actions/workflows/push-all.yml/badge.svg)](https://github.com/ultralytics/replicate/actions/workflows/push-all.yml)

[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/)

## 🗂️ Repository Structure

This repository provides optimized Replicate deployments for Ultralytics YOLO models with automated CI/CD workflows.

```plaintext
ultralytics/replicate/
│
├── yolo11n/                  # Official YOLO11n demo
│   ├── cog.yaml              # Cog configuration
│   ├── predict.py            # Prediction interface
│   ├── yolo11n.onnx          # Model weights (add yourself)
│   └── README.md             # Model-specific docs
│
├── custom/                   # Custom model template
│   ├── cog.yaml              # Cog configuration
│   ├── predict.py            # Prediction interface
│   ├── best.onnx             # Your custom weights (add yourself)
│   └── README.md             # Custom model guide
│
├── .github/workflows/        # Automated deployment
│   ├── push.yml              # Manual model push
│   ├── push-all.yml          # Push all models
│   ├── ci.yml                # Code quality checks
│   └── format.yml            # Code formatting
│
├── export_models.py          # Model export utility
├── test_prediction.py        # Local testing utility
├── LICENSE                   # AGPL-3.0 license
└── README.md                 # This file
```

## ⚡ Quick Start

### 1. Deploy Official YOLO11n Model

```bash
# Clone repository
git clone https://github.com/ultralytics/replicate.git
cd replicate

# Export official YOLO11n model
yolo export model=yolo11n.pt format=onnx

# Add model weights
cp yolo11n.onnx yolo11n/

# Deploy to Replicate
cd yolo11n
cog login
cog push r8.im/ultralytics/yolo11n
```

### 2. Deploy Your Custom Model

```bash
# Export your custom model
yolo export model=best.pt format=onnx

# Add to custom directory
cp best.onnx custom/

# Update image name in custom/cog.yaml
# image: "r8.im/your-username/your-model-name"

# Deploy your custom model
cd custom
cog push r8.im/your-username/your-model-name
```

### 3. Automated Deployment with GitHub Actions

1. **Setup secrets:**
   - Go to repository Settings → Secrets → Actions
   - Add `REPLICATE_CLI_AUTH_TOKEN` with your [Replicate API token](https://replicate.com/auth/token)

2. **Setup variables:**
   - Go to Settings → Variables → Actions
   - Add `DEFAULT_MODEL_NAME` = `ultralytics/yolo11n`

3. **Deploy:**
   - **Manual**: Actions tab → "Push YOLO to Replicate" → Run workflow
   - **Automatic**: Push changes to `main` branch auto-deploys all models

## 🛠️ Installation

Install Cog (Replicate's deployment tool):

```bash
sudo curl -o /usr/local/bin/cog -L https://github.com/replicate/cog/releases/latest/download/cog_$(uname -s)_$(uname -m)
sudo chmod +x /usr/local/bin/cog
```

## 🎯 Use Cases

### Official Model Demo (`yolo11n/`)

- **Purpose**: Demonstrate official YOLO11n deployment
- **Model**: Pre-trained YOLO11n (2.6M parameters)
- **Classes**: 80 COCO classes
- **Use Case**: Quick proof-of-concept, API demos

### Custom Model Template (`custom/`)

- **Purpose**: Deploy your own trained models
- **Model**: Your `best.pt` checkpoint
- **Classes**: Your custom classes
- **Use Case**: Production deployments, specialized detection

## 🔧 Model Export Utility

Use the included export script for batch processing:

```bash
# Export official model
python export_models.py --model yolo11n.pt --output yolo11n/

# Export custom model
python export_models.py --model best.pt --output custom/
```

## 🧪 Local Testing

Test your models locally before deploying:

```bash
# Test official YOLO11n
python test_prediction.py --model yolo11n --image test.jpg

# Test custom model
python test_prediction.py --model custom --image test.jpg
```

## 🚀 Features

- **🏎️ Optimized**: ONNX models for cross-GPU compatibility
- **🤖 Automated**: GitHub Actions for CI/CD
- **📦 Ready-to-use**: Pre-configured for YOLO11n demo
- **🔧 Flexible**: Template for custom model deployment
- **📊 Scalable**: Supports multiple model deployments
- **🎯 Focused**: Official demo + custom template approach

## 📚 Examples

### Deploy Fine-tuned Model

```bash
# After training on custom dataset
yolo train data=my_dataset.yaml model=yolo11n.pt epochs=100

# Export best checkpoint
yolo export model=runs/detect/train/weights/best.pt format=onnx

# Deploy to Replicate
cp runs/detect/train/weights/best.onnx custom/
cd custom
cog push r8.im/myusername/my-detector
```

### Update Custom Model

```python
# In custom/predict.py, update model name if needed
self.model = YOLO("my_model.onnx")  # Instead of "best.onnx"
```

## 💡 Contribute

We welcome contributions! Whether it's adding new deployment examples, improving configurations, or enhancing documentation:

- **Issues**: Report bugs or request features on [GitHub Issues](https://github.com/ultralytics/replicate/issues)
- **Pull Requests**: Follow our [Contributing Guide](https://docs.ultralytics.com/help/contributing/)
- **Discussions**: Join our [Discord](https://discord.com/invite/ultralytics) community

## 📄 License

Ultralytics offers two licensing options:

- **AGPL-3.0 License**: Open-source license for research and non-commercial use. See [LICENSE](LICENSE) file.
- **Enterprise License**: For commercial applications. Contact [Ultralytics Licensing](https://www.ultralytics.com/license).

## 📮 Contact

- **Issues**: [GitHub Issues](https://github.com/ultralytics/replicate/issues)
- **Community**: [Discord](https://discord.com/invite/ultralytics)
- **Enterprise**: [Ultralytics Enterprise](https://www.ultralytics.com/license)

<br>
<div align="center">
  <a href="https://github.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-github.png" width="3%" alt="Ultralytics GitHub"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.linkedin.com/company/ultralytics/"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-linkedin.png" width="3%" alt="Ultralytics LinkedIn"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://twitter.com/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-twitter.png" width="3%" alt="Ultralytics Twitter"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://youtube.com/ultralytics?sub_confirmation=1"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-youtube.png" width="3%" alt="Ultralytics YouTube"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://www.tiktok.com/@ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-tiktok.png" width="3%" alt="Ultralytics TikTok"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://ultralytics.com/bilibili"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-bilibili.png" width="3%" alt="Ultralytics BiliBili"></a>
  <img src="https://github.com/ultralytics/assets/raw/main/social/logo-transparent.png" width="3%" alt="space">
  <a href="https://discord.com/invite/ultralytics"><img src="https://github.com/ultralytics/assets/raw/main/social/logo-social-discord.png" width="3%" alt="Ultralytics Discord"></a>
</div>
