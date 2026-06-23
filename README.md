<a href="https://www.ultralytics.com/"><img src="https://raw.githubusercontent.com/ultralytics/assets/main/logo/Ultralytics_Logotype_Original.svg" width="320" alt="Ultralytics logo"></a>

# 🚀 Ultralytics Replicate

Deploy Ultralytics YOLO models to Replicate with ready-to-use Cog configurations and automated CI/CD workflows.

[![Push YOLO to Replicate](https://github.com/ultralytics/replicate/actions/workflows/push.yml/badge.svg)](https://github.com/ultralytics/replicate/actions/workflows/push.yml)
[![Ultralytics Actions](https://github.com/ultralytics/replicate/actions/workflows/format.yml/badge.svg)](https://github.com/ultralytics/replicate/actions/workflows/format.yml)
[![Codecov](https://codecov.io/github/ultralytics/replicate/branch/main/graph/badge.svg)](https://app.codecov.io/github/ultralytics/replicate)

[![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics)
[![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/)
[![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://reddit.com/r/ultralytics)

<img width="1920" height="939" alt="Replicate AI" src="https://github.com/user-attachments/assets/effaa643-4710-4187-849a-aa4d933fb0ee" />

## 🗂️ Repository Structure

This repository provides optimized Replicate deployments for YOLO11n, YOLOv8s WorldV2, and YOLOE-11S models with an
automated CI/CD workflow.

```plaintext
ultralytics/replicate/
│
├── yolo11n/                  # YOLO11n model deployment
│   ├── cog.yaml              # Cog configuration
│   ├── predict.py            # Prediction interface
│   └── README.md             # Model documentation
├── yolov8s-worldv2/          # YOLOv8s WorldV2 model deployment
│   ├── cog.yaml              # Cog configuration
│   ├── predict.py            # Prediction interface
│   └── README.md             # Model documentation
├── yoloe11s/                 # YOLOE-11S model deployment
│   ├── cog.yaml              # Cog configuration
│   ├── predict.py            # Prediction interface
│   └── README.md             # Model documentation
├── yolo26/                   # YOLO26 model deployment (selectable size n/s/m/l/x)
│   ├── cog.yaml              # Cog configuration
│   ├── predict.py            # Prediction interface
│   └── README.md             # Model documentation
├── assets/                   # Sample images for workflow smoke tests
│
├── .github/workflows/        # Automated deployment
│   ├── push.yml              # Model deployment workflow
│   ├── ci.yml                # Code quality checks
│   └── format.yml            # Code formatting
│
├── test_prediction.py        # Local YOLO11n testing utility
├── requirements.txt          # Dependencies
├── LICENSE                   # AGPL-3.0 license
└── README.md                 # This file
```

## ⚡ Quick Start

### Deploy a Model

Models deploy to the corresponding Replicate endpoints:

```bash
# Clone repository
git clone https://github.com/ultralytics/replicate.git
cd replicate

# Deploy YOLO11n
cd yolo11n
python download.py
cog login
cog push r8.im/ultralytics/yolo11n

# Or deploy another configured model
cd ../yolov8s-worldv2
python download.py
cog push r8.im/ultralytics/yolov8s-worldv2

cd ../yoloe11s
python download.py
cog push r8.im/ultralytics/yoloe-11s
```

### Automated Deployment with GitHub Actions

1. **Setup secrets:**
   - Go to repository Settings → Secrets → Actions
   - Add `REPLICATE_API_TOKEN` with your [Replicate API token](https://replicate.com/signin?next=/auth/token)

2. **Deploy:**
   - **Manual**: Actions tab → "Push YOLO to Replicate" → Run workflow
   - **Automatic**: Push changes to `main` builds, tests, and deploys each configured model

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

## 🎯 Available Models

| Directory          | Replicate model                     | Predictor   | Notes                                                  |
| ------------------ | ----------------------------------- | ----------- | ------------------------------------------------------ |
| `yolo11n/`         | `r8.im/ultralytics/yolo11n`         | `YOLO`      | Official YOLO11n object detection model                |
| `yolov8s-worldv2/` | `r8.im/ultralytics/yolov8s-worldv2` | `YOLOWorld` | Open-vocabulary YOLOv8s WorldV2 model                  |
| `yoloe11s/`        | `r8.im/ultralytics/yoloe-11s`       | `YOLOE`     | YOLOE-11S segmentation model with class prompt support |
| `yolo26/`          | `r8.im/ultralytics/yolo26`          | `YOLO`      | YOLO26 detection with runtime size selection (n/s/m/l/x) |

## 🔧 Model Setup

Each model directory includes a `download.py` script used by the deployment workflow before `cog build`:

```bash
python yolo11n/download.py
python yolov8s-worldv2/download.py
python yoloe11s/download.py
```

## 🧪 Local Testing

Test the model locally before deploying:

```bash
# Test YOLO11n
python yolo11n/download.py
python test_prediction.py --model yolo11n --image assets/bus.jpg
```

## 🚀 Features

- **🏎️ Optimized**: PyTorch model for fast inference
- **🤖 Automated**: GitHub Actions for CI/CD
- **📦 Ready-to-use**: Pre-configured deployments for multiple YOLO models
- **📊 Scalable**: Auto-scaling Replicate infrastructure
- **🎯 Focused**: One Cog configuration per model

## 💡 Contribute

Ultralytics thrives on community collaboration, and we deeply value your contributions! Whether it's reporting bugs, suggesting features, or submitting code changes, your involvement is crucial.

- **Reporting Issues**: Encounter a bug? Please report it on [GitHub Issues](https://github.com/ultralytics/replicate/issues).
- **Feature Requests**: Have an idea for improvement? Share it via [GitHub Issues](https://github.com/ultralytics/replicate/issues).
- **Pull Requests**: Want to contribute code? Please read our [Contributing Guide](https://docs.ultralytics.com/help/contributing) first, then submit a Pull Request.
- **Feedback**: Share your thoughts and experiences by participating in our official [Survey](https://www.ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey).

A heartfelt thank you 🙏 goes out to all our contributors! Your efforts help make Ultralytics tools better for everyone.

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/ultralytics/graphs/contributors)

## 📄 License

Ultralytics offers two licensing options to accommodate diverse needs:

- **AGPL-3.0 License**: Ideal for students, researchers, and enthusiasts passionate about open collaboration and knowledge sharing. This [OSI-approved](https://opensource.org/license/agpl-3.0) open-source license promotes transparency and community involvement. See the [LICENSE](LICENSE) file for details.
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
