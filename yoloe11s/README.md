[![Ultralytics YOLO banner](https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/banner-yolov8.png)](https://platform.ultralytics.com/?utm_source=github&utm_medium=referral&utm_campaign=platform_launch&utm_content=banner&utm_term=ultralytics_github)

[中文](https://docs.ultralytics.com/zh) | [한국어](https://docs.ultralytics.com/ko) | [日本語](https://docs.ultralytics.com/ja) | [Русский](https://docs.ultralytics.com/ru) | [Deutsch](https://docs.ultralytics.com/de) | [Français](https://docs.ultralytics.com/fr) | [Español](https://docs.ultralytics.com/es) | [Português](https://docs.ultralytics.com/pt) | [Türkçe](https://docs.ultralytics.com/tr) | [Tiếng Việt](https://docs.ultralytics.com/vi) | [العربية](https://docs.ultralytics.com/ar)

[![Ultralytics CI](https://github.com/ultralytics/ultralytics/actions/workflows/ci.yml/badge.svg)](https://github.com/ultralytics/ultralytics/actions/workflows/ci.yml) [![Ultralytics Downloads](https://static.pepy.tech/badge/ultralytics)](https://clickpy.clickhouse.com/dashboard/ultralytics) [![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics) [![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/) [![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://www.reddit.com/r/ultralytics/)

[![Run Ultralytics on Gradient](https://assets.paperspace.io/img/gradient-badge.svg)](https://console.paperspace.com/github/ultralytics/ultralytics) [![Open Ultralytics In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ultralytics/ultralytics/blob/main/examples/tutorial.ipynb) [![Open Ultralytics In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/models/ultralytics/yolo26) [![Open Ultralytics In Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ultralytics/ultralytics/HEAD?labpath=examples%2Ftutorial.ipynb)

# Ultralytics YOLOE-11S Open-Vocabulary Instance Segmentation

This endpoint deploys Ultralytics [YOLOE](https://docs.ultralytics.com/models/yoloe/)-11S (`yoloe-11s-seg.pt`), a real-time open-vocabulary instance segmentation model that detects and segments arbitrary object classes from text prompts. The Replicate endpoint accepts a comma-separated `class_names` input, which is applied via `set_classes()` before inference; when `class_names` is left empty it falls back to the prompt-free weights (`yoloe-11s-seg-pf.pt`) that detect from a built-in vocabulary. Both detection boxes and pixel-precise segmentation masks are returned on the annotated image, with optional JSON.

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
yolo predict model=yoloe-11s-seg.pt source=path/to/bus.jpg
```

The `yolo` command supports various tasks and modes, accepting additional arguments like `imgsz=640`. See the [CLI Docs](https://docs.ultralytics.com/usage/cli).

### Python

You can also run the model directly in Python:

```python
from ultralytics import YOLOE

# Load the deployed open-vocabulary segmentation model
model = YOLOE("yoloe-11s-seg.pt")

# Set the text-prompt classes to detect (applied once before predict)
class_names = ["person", "bus", "sign"]
model.set_classes(class_names, model.get_text_pe(class_names))

# Run open-vocabulary instance segmentation
results = model("path/to/bus.jpg", conf=0.25, iou=0.45, imgsz=640)
results[0].save("output.png")
```

Discover more in the [Python Docs](https://docs.ultralytics.com/usage/python).

## ✨ Model

YOLOE-11 open-vocabulary instance segmentation models. This endpoint serves **YOLOE-11S** (`yoloe-11s-seg.pt`), automatically using the prompt-free `yoloe-11s-seg-pf.pt` when no classes are provided. All weights download automatically from the latest Ultralytics [release](https://github.com/ultralytics/assets/releases) on first use.

| Model     | Pretrained weights | Prompt-free variant | Task                  |
| --------- | ------------------ | ------------------- | --------------------- |
| YOLOE-11S | yoloe-11s-seg.pt   | yoloe-11s-seg-pf.pt | Instance Segmentation |
| YOLOE-11M | yoloe-11m-seg.pt   | yoloe-11m-seg-pf.pt | Instance Segmentation |
| YOLOE-11L | yoloe-11l-seg.pt   | yoloe-11l-seg-pf.pt | Instance Segmentation |

- YOLOE improves by **+3.5 AP** over YOLO-Worldv2 on LVIS while using about a third of the training resources and ~1.4× faster inference, and supports text prompts, visual prompts, and a prompt-free mode. See the [YOLOE docs](https://docs.ultralytics.com/models/yoloe/).
- This endpoint serves **YOLOE-11S**; the larger 11M/11L variants are shown for reference.

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
