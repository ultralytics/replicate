[![Ultralytics YOLO banner](https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/banner-yolov8.png)](https://platform.ultralytics.com/?utm_source=github&utm_medium=referral&utm_campaign=platform_launch&utm_content=banner&utm_term=ultralytics_github)

[中文](https://docs.ultralytics.com/zh) | [한국어](https://docs.ultralytics.com/ko) | [日本語](https://docs.ultralytics.com/ja) | [Русский](https://docs.ultralytics.com/ru) | [Deutsch](https://docs.ultralytics.com/de) | [Français](https://docs.ultralytics.com/fr) | [Español](https://docs.ultralytics.com/es) | [Português](https://docs.ultralytics.com/pt) | [Türkçe](https://docs.ultralytics.com/tr) | [Tiếng Việt](https://docs.ultralytics.com/vi) | [العربية](https://docs.ultralytics.com/ar)

[![Ultralytics CI](https://github.com/ultralytics/ultralytics/actions/workflows/ci.yml/badge.svg)](https://github.com/ultralytics/ultralytics/actions/workflows/ci.yml) [![Ultralytics Downloads](https://img.shields.io/pepy/dt/ultralytics?color=blue)](https://clickpy.clickhouse.com/dashboard/ultralytics) [![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics) [![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/) [![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://www.reddit.com/r/ultralytics/)

# Ultralytics YOLO26 Semantic Segmentation

[Ultralytics](https://www.ultralytics.com/) creates cutting-edge, state-of-the-art (SOTA) [YOLO models](https://www.ultralytics.com/yolo) built on years of foundational research in computer vision and AI. [YOLO26](https://docs.ultralytics.com/models/yolo26) is the latest generation — **fast**, **accurate**, and **easy to use**. This Replicate deployment runs YOLO26 on CPU with a runtime-selectable model size (n/s/m/l/x); this endpoint performs [semantic segmentation](https://docs.ultralytics.com/tasks/semantic), assigning every pixel one of the 19 [Cityscapes](https://docs.ultralytics.com/datasets/semantic/cityscapes) urban-scene classes.

Find detailed documentation in the [Ultralytics Docs](https://docs.ultralytics.com/). Get support via [GitHub Issues](https://github.com/ultralytics/ultralytics/issues/new/choose). Join discussions on [Discord](https://discord.com/invite/ultralytics), [Reddit](https://www.reddit.com/r/ultralytics/), and the [Ultralytics Community Forums](https://community.ultralytics.com/)!

Request an Enterprise License for commercial use at [Ultralytics Licensing](https://www.ultralytics.com/license).

[![YOLO26 performance plots](https://raw.githubusercontent.com/ultralytics/assets/refs/heads/main/yolo/performance-comparison.png)](https://platform.ultralytics.com/ultralytics/yolo26)

## 📄 Documentation

For comprehensive guidance on training, validation, prediction, and deployment, refer to the full [Ultralytics Docs](https://docs.ultralytics.com/).

### Install

Install the `ultralytics` package, including all [requirements](https://github.com/ultralytics/ultralytics/blob/main/pyproject.toml), in a [**Python>=3.8**](https://www.python.org/) environment with [**PyTorch>=1.8**](https://pytorch.org/get-started/locally/).

[![PyPI - Version](https://img.shields.io/pypi/v/ultralytics?logo=pypi&logoColor=white)](https://pypi.org/project/ultralytics/) [![Ultralytics Downloads](https://img.shields.io/pepy/dt/ultralytics?color=blue)](https://clickpy.clickhouse.com/dashboard/ultralytics) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/ultralytics?logo=python&logoColor=gold)](https://pypi.org/project/ultralytics/)

```bash
pip install ultralytics
```

For alternative installation methods, including [Conda](https://anaconda.org/conda-forge/ultralytics), [Docker](https://hub.docker.com/r/ultralytics/ultralytics), and building from source via Git, please consult the [Quickstart Guide](https://docs.ultralytics.com/quickstart).

### CLI

You can run this model from the Command Line Interface (CLI) with the `yolo` command:

```bash
yolo predict model=yolo26n-sem.pt source='https://ultralytics.com/images/bus.jpg'
```

The `yolo` command supports various tasks and modes, accepting additional arguments like `imgsz=640`. See the [CLI Docs](https://docs.ultralytics.com/usage/cli).

### Python

You can also run the model directly in Python:

```python
from ultralytics import YOLO

# Load the pretrained YOLO26-sem model
model = YOLO("yolo26n-sem.pt")

# Run inference on an image
results = model("path/to/image.jpg")
results[0].show()  # display the annotated result
results[0].save("output.png")  # save it
```

Discover more in the [Python Docs](https://docs.ultralytics.com/usage/python).

## ✨ Model

See the [Semantic Segmentation Docs](https://docs.ultralytics.com/tasks/semantic) for usage examples. These models are trained on [Cityscapes](https://docs.ultralytics.com/datasets/semantic/cityscapes), including 19 classes. All models download automatically from the latest Ultralytics [release](https://github.com/ultralytics/assets/releases) on first use.

| Model                                                                                        | size (pixels) | mIoU val | Speed RTX3090 PyTorch (ms) | params (M) | FLOPs (B) |
| -------------------------------------------------------------------------------------------- | ------------- | -------- | -------------------------- | ---------- | --------- |
| [YOLO26n-sem](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26n-sem.pt) | 1024 × 2048   | 78.3     | 4.4 ± 0.0                  | 1.6        | 22.7      |
| [YOLO26s-sem](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26s-sem.pt) | 1024 × 2048   | 80.8     | 8.4 ± 0.0                  | 6.5        | 88.8      |
| [YOLO26m-sem](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26m-sem.pt) | 1024 × 2048   | 82.0     | 19.9 ± 0.1                 | 14.3       | 304.5     |
| [YOLO26l-sem](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26l-sem.pt) | 1024 × 2048   | 82.9     | 26.5 ± 0.1                 | 17.9       | 384.7     |
| [YOLO26x-sem](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26x-sem.pt) | 1024 × 2048   | 83.6     | 48.9 ± 0.2                 | 40.2       | 861.7     |

- **mIoU val** values are for single-model single-scale on the [Cityscapes](https://www.cityscapes-dataset.com/) validation set. Reproduce with `yolo semantic val data=cityscapes.yaml device=0 imgsz=2048`
- **Speed** metrics are averaged over Cityscapes validation images on an RTX3090 (PyTorch). See [YOLO Performance Metrics](https://docs.ultralytics.com/guides/yolo-performance-metrics) for details.

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
