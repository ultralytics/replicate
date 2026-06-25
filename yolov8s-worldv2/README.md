[![Ultralytics YOLO banner](https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/banner-yolov8.png)](https://platform.ultralytics.com/?utm_source=github&utm_medium=referral&utm_campaign=platform_launch&utm_content=banner&utm_term=ultralytics_github)

[中文](https://docs.ultralytics.com/zh) | [한국어](https://docs.ultralytics.com/ko) | [日本語](https://docs.ultralytics.com/ja) | [Русский](https://docs.ultralytics.com/ru) | [Deutsch](https://docs.ultralytics.com/de) | [Français](https://docs.ultralytics.com/fr) | [Español](https://docs.ultralytics.com/es) | [Português](https://docs.ultralytics.com/pt) | [Türkçe](https://docs.ultralytics.com/tr) | [Tiếng Việt](https://docs.ultralytics.com/vi) | [العربية](https://docs.ultralytics.com/ar)

[![Ultralytics CI](https://github.com/ultralytics/ultralytics/actions/workflows/ci.yml/badge.svg)](https://github.com/ultralytics/ultralytics/actions/workflows/ci.yml) [![Ultralytics Downloads](https://static.pepy.tech/badge/ultralytics)](https://clickpy.clickhouse.com/dashboard/ultralytics) [![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics) [![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/) [![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://www.reddit.com/r/ultralytics/)

[![Run Ultralytics on Gradient](https://assets.paperspace.io/img/gradient-badge.svg)](https://console.paperspace.com/github/ultralytics/ultralytics) [![Open Ultralytics In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ultralytics/ultralytics/blob/main/examples/tutorial.ipynb) [![Open Ultralytics In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/models/ultralytics/yolo26) [![Open Ultralytics In Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ultralytics/ultralytics/HEAD?labpath=examples%2Ftutorial.ipynb)

# Ultralytics YOLOv8s-WorldV2 Open-Vocabulary Detection

This endpoint deploys the YOLOv8s-WorldV2 open-vocabulary object detector (`yolov8s-worldv2.pt`, loaded via the Ultralytics `YOLOWorld` class) for real-time, zero-shot detection of arbitrary objects described by text — see [YOLO-World](https://docs.ultralytics.com/models/yolo-world/). The Replicate endpoint takes a comma-separated `class_names` input (default `person, bus, sign`) and applies it via `set_classes()` on every request, so you choose exactly what to detect. It returns an annotated image plus optional JSON, with adjustable confidence, IoU, and image size.

Find detailed documentation in the [Ultralytics Docs](https://docs.ultralytics.com/). Get support via [GitHub Issues](https://github.com/ultralytics/ultralytics/issues/new/choose). Join discussions on [Discord](https://discord.com/invite/ultralytics), [Reddit](https://www.reddit.com/r/ultralytics/), and the [Ultralytics Community Forums](https://community.ultralytics.com/)!

Request an Enterprise License for commercial use at [Ultralytics Licensing](https://www.ultralytics.com/license).

## 📄 Documentation

For comprehensive guidance on training, validation, prediction, and deployment, refer to the full [Ultralytics Docs](https://docs.ultralytics.com/).

### Install

Install the `ultralytics` package, including all [requirements](https://github.com/ultralytics/ultralytics/blob/main/pyproject.toml), in a [**Python>=3.8**](https://www.python.org/) environment with [**PyTorch>=1.8**](https://pytorch.org/get-started/locally/).

[![PyPI - Version](https://img.shields.io/pypi/v/ultralytics?logo=pypi&logoColor=white)](https://pypi.org/project/ultralytics/) [![Ultralytics Downloads](https://static.pepy.tech/badge/ultralytics)](https://clickpy.clickhouse.com/dashboard/ultralytics) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ultralytics?logo=python&logoColor=gold)](https://pypi.org/project/ultralytics/)

```bash
pip install ultralytics
```

For alternative installation methods, including [Conda](https://anaconda.org/conda-forge/ultralytics), [Docker](https://hub.docker.com/r/ultralytics/ultralytics), and building from source via Git, please consult the [Quickstart Guide](https://docs.ultralytics.com/quickstart).

### CLI

You can run this model from the Command Line Interface (CLI) with the `yolo` command:

```bash
yolo predict model=yolov8s-worldv2.pt source=path/to/image.jpg imgsz=640
```

The `yolo` command supports various tasks and modes, accepting additional arguments like `imgsz=640`. See the [CLI Docs](https://docs.ultralytics.com/usage/cli).

### Python

You can also run the model directly in Python:

```python
from ultralytics import YOLOWorld

# Load the deployed YOLOv8s-worldv2 model
model = YOLOWorld("yolov8s-worldv2.pt")

# Set custom open-vocabulary classes before inference
model.set_classes(["person", "bus", "sign"])

# Run inference
results = model("path/to/image.jpg", conf=0.25, iou=0.45, imgsz=640)
results[0].show()
```

Discover more in the [Python Docs](https://docs.ultralytics.com/usage/python).

## ✨ Model

Zero-shot transfer performance on the [COCO](https://cocodataset.org/) dataset. All weights download automatically from the latest Ultralytics [release](https://github.com/ultralytics/assets/releases) on first use.

| Model           | mAP  | mAP50 | mAP75 |
| --------------- | ---- | ----- | ----- |
| YOLOv8s-worldv2 | 37.7 | 52.2  | 41.0  |
| YOLOv8m-worldv2 | 43.0 | 58.4  | 46.8  |
| YOLOv8l-worldv2 | 45.8 | 61.3  | 49.8  |
| YOLOv8x-worldv2 | 47.1 | 62.8  | 51.4  |

- Metrics are zero-shot transfer mAP / mAP50 / mAP75 on [COCO](https://cocodataset.org/), from the Ultralytics [YOLO-World docs](https://docs.ultralytics.com/models/yolo-world/).
- This endpoint serves the deployed **yolov8s-worldv2** variant (37.7 mAP); other rows are shown for reference.

## 🧩 Integrations

Our key integrations with leading AI platforms extend the functionality of Ultralytics' offerings, enhancing tasks like dataset labeling, training, visualization, and model management. Discover how Ultralytics, in collaboration with partners like [Weights & Biases](https://docs.ultralytics.com/integrations/weights-biases), [Comet ML](https://docs.ultralytics.com/integrations/comet), [Roboflow](https://docs.ultralytics.com/integrations/roboflow), and [Intel OpenVINO](https://docs.ultralytics.com/integrations/openvino), can optimize your AI workflow. Explore more at [Ultralytics Integrations](https://docs.ultralytics.com/integrations).

## 🤝 Contribute

We thrive on community collaboration! Ultralytics YOLO wouldn't be the SOTA framework it is without contributions from developers like you. Please see our [Contributing Guide](https://docs.ultralytics.com/help/contributing) to get started. We also welcome your feedback—share your experience by completing our [Survey](https://www.ultralytics.com/survey?utm_source=github&utm_medium=social&utm_campaign=Survey). A huge **Thank You** 🙏 to everyone who contributes!

[![Ultralytics open-source contributors](https://raw.githubusercontent.com/ultralytics/assets/main/im/image-contributors.png)](https://github.com/ultralytics/ultralytics/graphs/contributors)

## 📜 License

Ultralytics offers two licensing options to suit different needs:

- **AGPL-3.0 License**: This [OSI-approved](https://opensource.org/license/agpl-3.0) open-source license is perfect for students, researchers, and enthusiasts. It encourages open collaboration and knowledge sharing. See the [LICENSE](https://github.com/ultralytics/ultralytics/blob/main/LICENSE) file for full details.
- **Ultralytics Enterprise License**: For development and production use, this license enables seamless integration of Ultralytics software and AI models into business products and services, bypassing the open-source requirements of AGPL-3.0. To get started, please contact us via [Ultralytics Licensing](https://www.ultralytics.com/license).

## 📞 Contact

For bug reports and feature requests related to Ultralytics software, please visit [GitHub Issues](https://github.com/ultralytics/ultralytics/issues). For questions, discussions, and community support, join our active communities on [Discord](https://discord.com/invite/ultralytics), [Reddit](https://www.reddit.com/r/ultralytics/), and the [Ultralytics Community Forums](https://community.ultralytics.com/). We're here to help with all things Ultralytics!
