[![Ultralytics YOLO banner](https://raw.githubusercontent.com/ultralytics/assets/main/yolov8/banner-yolov8.png)](https://platform.ultralytics.com/?utm_source=github&utm_medium=referral&utm_campaign=platform_launch&utm_content=banner&utm_term=ultralytics_github)

[中文](https://docs.ultralytics.com/zh) | [한국어](https://docs.ultralytics.com/ko) | [日本語](https://docs.ultralytics.com/ja) | [Русский](https://docs.ultralytics.com/ru) | [Deutsch](https://docs.ultralytics.com/de) | [Français](https://docs.ultralytics.com/fr) | [Español](https://docs.ultralytics.com/es) | [Português](https://docs.ultralytics.com/pt) | [Türkçe](https://docs.ultralytics.com/tr) | [Tiếng Việt](https://docs.ultralytics.com/vi) | [العربية](https://docs.ultralytics.com/ar)

[![Ultralytics CI](https://github.com/ultralytics/ultralytics/actions/workflows/ci.yml/badge.svg)](https://github.com/ultralytics/ultralytics/actions/workflows/ci.yml) [![Ultralytics Downloads](https://static.pepy.tech/badge/ultralytics)](https://clickpy.clickhouse.com/dashboard/ultralytics) [![Ultralytics Discord](https://img.shields.io/discord/1089800235347353640?logo=discord&logoColor=white&label=Discord&color=blue)](https://discord.com/invite/ultralytics) [![Ultralytics Forums](https://img.shields.io/discourse/users?server=https%3A%2F%2Fcommunity.ultralytics.com&logo=discourse&label=Forums&color=blue)](https://community.ultralytics.com/) [![Ultralytics Reddit](https://img.shields.io/reddit/subreddit-subscribers/ultralytics?style=flat&logo=reddit&logoColor=white&label=Reddit&color=blue)](https://www.reddit.com/r/ultralytics/)

[![Run Ultralytics on Gradient](https://assets.paperspace.io/img/gradient-badge.svg)](https://console.paperspace.com/github/ultralytics/ultralytics) [![Open Ultralytics In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ultralytics/ultralytics/blob/main/examples/tutorial.ipynb) [![Open Ultralytics In Kaggle](https://kaggle.com/static/images/open-in-kaggle.svg)](https://www.kaggle.com/models/ultralytics/yolo26) [![Open Ultralytics In Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/ultralytics/ultralytics/HEAD?labpath=examples%2Ftutorial.ipynb)

# Ultralytics YOLO26 Oriented Bounding Boxes (OBB)

[Ultralytics](https://www.ultralytics.com/) creates cutting-edge, state-of-the-art (SOTA) [YOLO models](https://www.ultralytics.com/yolo) built on years of foundational research in computer vision and AI. [YOLO26](https://docs.ultralytics.com/models/yolo26) is the latest generation — **fast**, **accurate**, and **easy to use**. This Replicate deployment runs YOLO26 on CPU with a runtime-selectable model size (n/s/m/l/x); this endpoint performs [oriented bounding box (OBB) detection](https://docs.ultralytics.com/tasks/obb) on the 15 [DOTAv1](https://docs.ultralytics.com/datasets/obb/dota-v2#dota-v10) aerial classes, predicting rotated boxes for overhead imagery.

Find detailed documentation in the [Ultralytics Docs](https://docs.ultralytics.com/). Get support via [GitHub Issues](https://github.com/ultralytics/ultralytics/issues/new/choose). Join discussions on [Discord](https://discord.com/invite/ultralytics), [Reddit](https://www.reddit.com/r/ultralytics/), and the [Ultralytics Community Forums](https://community.ultralytics.com/)!

Request an Enterprise License for commercial use at [Ultralytics Licensing](https://www.ultralytics.com/license).

[![YOLO26 performance plots](https://raw.githubusercontent.com/ultralytics/assets/refs/heads/main/yolo/performance-comparison.png)](https://platform.ultralytics.com/ultralytics/yolo26)

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
yolo predict model=yolo26n-obb.pt source='https://ultralytics.com/images/bus.jpg'
```

The `yolo` command supports various tasks and modes, accepting additional arguments like `imgsz=640`. See the [CLI Docs](https://docs.ultralytics.com/usage/cli).

### Python

You can also run the model directly in Python:

```python
from ultralytics import YOLO

# Load the pretrained YOLO26-obb model
model = YOLO("yolo26n-obb.pt")

# Run inference on an image
results = model("path/to/image.jpg")
results[0].show()  # display the annotated result
results[0].save("output.png")  # save it
```

Discover more in the [Python Docs](https://docs.ultralytics.com/usage/python).

## ✨ Model

Check the [OBB Docs](https://docs.ultralytics.com/tasks/obb) for usage examples. These models are trained on [DOTAv1](https://docs.ultralytics.com/datasets/obb/dota-v2#dota-v10), including 15 classes. All models download automatically from the latest Ultralytics [release](https://github.com/ultralytics/assets/releases) on first use.

| Model                                                                                        | size (pixels) | mAP test 50-95 (e2e) | mAP test 50 (e2e) | Speed CPU ONNX (ms) | Speed T4 TensorRT10 (ms) | params (M) | FLOPs (B) |
| -------------------------------------------------------------------------------------------- | ------------- | -------------------- | ----------------- | ------------------- | ------------------------ | ---------- | --------- |
| [YOLO26n-obb](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26n-obb.pt) | 1024          | 52.4                 | 78.9              | 97.7 ± 0.9          | 2.8 ± 0.0                | 2.5        | 14.0      |
| [YOLO26s-obb](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26s-obb.pt) | 1024          | 54.8                 | 80.9              | 218.0 ± 1.4         | 4.9 ± 0.1                | 9.8        | 55.1      |
| [YOLO26m-obb](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26m-obb.pt) | 1024          | 55.3                 | 81.0              | 579.2 ± 3.8         | 10.2 ± 0.3               | 21.2       | 183.3     |
| [YOLO26l-obb](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26l-obb.pt) | 1024          | 56.2                 | 81.6              | 735.6 ± 3.1         | 13.0 ± 0.2               | 25.6       | 230.0     |
| [YOLO26x-obb](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26x-obb.pt) | 1024          | 56.7                 | 81.7              | 1485.7 ± 11.5       | 30.5 ± 0.9               | 57.6       | 516.5     |

- **mAP test** values are for single-model multiscale performance on the [DOTAv1 test set](https://captain-whu.github.io/DOTA/dataset.html). Reproduce with `yolo val obb data=DOTAv1.yaml device=0`
- **Speed** metrics are averaged over dataset val images; CPU speeds measured with [ONNX](https://onnx.ai/) export, GPU speeds with [TensorRT](https://developer.nvidia.com/tensorrt). See [YOLO Performance Metrics](https://docs.ultralytics.com/guides/yolo-performance-metrics) for details.

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
