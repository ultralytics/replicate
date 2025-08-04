<a href="https://www.ultralytics.com/"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# 🚀 Ultralytics Replicate

Deploy YOLO11n to Replicate with ready-to-use Cog configuration and automated CI/CD workflow.

[![Push YOLO11n to Replicate](https://github.com/ultralytics/replicate/actions/workflows/push.yml/badge.svg)](https://github.com/ultralytics/replicate/actions/workflows/push.yml)
[![Ultralytics Actions](https://github.com/ultralytics/replicate/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/replicate/actions/workflows/format.yml)

[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

<img width="1920" height="939" alt="Replicate AI" src="https://github.com/user-attachments/assets/effaa643-4710-4187-849a-aa4d933fb0ee" />

## 🗂️ Repository Structure

This repository provides optimized Replicate deployment for the YOLO11n model with automated CI/CD workflow.

```plaintext
ultralytics/replicate/
│
├── yolo11n/                  # YOLO11n model deployment
│   ├── cog.yaml              # Cog configuration
│   ├── predict.py            # Prediction interface
│   └── README.md             # Model documentation
│
├── .github/workflows/        # Automated deployment
│   ├── push.yml              # Model deployment workflow
│   ├── ci.yml                # Code quality checks
│   └── format.yml            # Code formatting
│
├── test_prediction.py        # Local testing utility
├── requirements.txt          # Dependencies
├── LICENSE                   # AGPL-3.0 license
└── README.md                 # This file
```

## ⚡ Quick Start

### Deploy YOLO11n Model

```bash
# Clone repository
git clone https://github.com/ultralytics/replicate.git
cd replicate

# Deploy to Replicate
cd yolo11n
cog login
cog push r8.im/ultralytics/yolo11n
```

### Automated Deployment with GitHub Actions

1. **Setup secrets:**
   - Go to repository Settings → Secrets → Actions
   - Add `REPLICATE_API_TOKEN` with your [Replicate API token](https://replicate.com/auth/token)

2. **Deploy:**
   - **Manual**: Actions tab → "Push YOLO11n to Replicate" → Run workflow
   - **Automatic**: Push changes to `main` branch auto-deploys

## 🛠️ Installation

Install Cog (Replicate's deployment tool):

```bash
sudo curl -o /usr/local/bin/cog -L https://github.com/replicate/cog/releases/latest/download/cog_$(uname -s)_$(uname -m)
sudo chmod +x /usr/local/bin/cog
```

For local development and testing:

```bash
pip install -r requirements.txt
```

## 🎯 YOLO11n Model

- **Purpose**: Official YOLO11n object detection
- **Parameters**: 2.6M parameters
- **Classes**: 80 COCO classes
- **Performance**: 39.5 mAP50-95 on COCO dataset
- **Speed**: Optimized for real-time inference

## 🔧 Model Setup

The model will be automatically downloaded by ultralytics when needed:

```python
from ultralytics import YOLO

model = YOLO("yolo11n.pt")  # Downloads automatically if not present
```

## 🧪 Local Testing

Test the model locally before deploying:

```bash
# Test YOLO11n
python test_prediction.py --model yolo11n --image test.jpg
```

## 🚀 Features

- **🏎️ Optimized**: PyTorch model for fast inference
- **🤖 Automated**: GitHub Actions for CI/CD
- **📦 Ready-to-use**: Pre-configured YOLO11n deployment
- **📊 Scalable**: Auto-scaling Replicate infrastructure
- **🎯 Simple**: Single model focus

## 💡 Contribute

Ultralytics thrives on community collaboration, and we deeply value your contributions! Whether it's reporting bugs, suggesting features, or submitting code changes, your involvement is crucial.

- **Reporting Issues**: Encounter a bug? Please report it on [GitHub Issues](https://github.com/ultralytics/replicate/issues).
- **Feature Requests**: Have an idea for improvement? Share it via [GitHub Issues](https://github.com/ultralytics/replicate/issues).
- **Pull Requests**: Want to contribute code? Please read our [Contributing Guide](https://docs.ultralytics.com/help/contributing/) first, then submit a Pull Request.
- **Feedback**: Share your thoughts and experiences by participating in our official [Survey](https://www.ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey).

A heartfelt thank you 🙏 goes out to all our contributors! Your efforts help make Ultralytics tools better for everyone.

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/ultralytics/graphs/contributors)

## 📄 License

Ultralytics offers two licensing options to accommodate diverse needs:

- **AGPL-3.0 License**: Ideal for students, researchers, and enthusiasts passionate about open collaboration and knowledge sharing. This [OSI-approved](https://opensource.org/license/agpl-v3) open-source license promotes transparency and community involvement. See the [LICENSE](LICENSE) file for details.
- **Enterprise License**: Designed for commercial applications, this license permits the seamless integration of Ultralytics software and AI models into commercial products and services, bypassing the copyleft requirements of AGPL-3.0. For commercial use cases, please inquire about an [Ultralytics Enterprise License](https://www.ultralytics.com/license).

## 📮 Contact

For bug reports or feature suggestions related to this project or other Ultralytics projects, please use [GitHub Issues](https://github.com/ultralytics/replicate/issues). For general questions, discussions, and community support, join our [Discord](https://discord.com/invite/ultralytics) server!

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
