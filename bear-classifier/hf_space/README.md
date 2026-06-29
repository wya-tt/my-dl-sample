---
title: Bear Classifier
emoji: 🐻
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: 6.19.0
python_version: "3.13"
app_file: app.py
pinned: false
---

<!-- 上方 YAML 为 Hugging Face Space 的构建配置，请勿删除。
     以下为 README 风格的中英双语说明文档。
     GitHub / Hugging Face 的 Markdown 不支持 JS 切换，
     因此使用「顶部语言锚点 + 可折叠 <details> 分段」实现双语阅读。 -->

# 🐻 Bear Classifier

**🌐 Language / 语言：[中文](#-中文) · [English](#-english)**

---

<a id="-中文"></a>

<details open>
<summary><b>🇨🇳 中文（点击展开 / 收起）</b></summary>

## 在线访问

- **应用链接**：<https://yaphets429-bear-classifier-test.hf.space/>
- **部署平台**：Hugging Face Spaces（Gradio SDK）
- 打开后即为网页交互界面，无需安装任何环境。

## 一、目的

这是一个基于深度学习的**图像分类 Web 应用**，用于识别上传的图片属于以下三类熊中的哪一种：

| 类别 | 含义 |
|------|------|
| `black`   | 黑熊 |
| `grizzly` | 灰熊（棕熊） |
| `teddy`   | 泰迪熊（玩具熊） |

模型来自 fastai 课程《Practical Deep Learning for Coders》的经典示例，训练数据为通过图片爬虫收集的三类熊图片，使用迁移学习（ResNet）微调得到。目标是把训练好的模型**部署成一个任何人都能在浏览器里直接使用的在线 demo**。

## 二、使用方法

1. 打开应用链接。
2. 在 **"Upload a bear image"** 区域上传一张图片（点击或拖拽，支持常见图片格式）。页面底部提供了 3 张示例图，可直接点击试用。
3. 模型自动预测，**"Prediction"** 区域显示最可能的类别及各类别的**置信度概率**（最多 3 类）。
4. 想换图重测，重新上传即可。

> 首次访问若 Space 处于休眠状态，会有几十秒的唤醒/加载时间，属正常现象。

## 三、主要设计思路

- **训练与推理分离**：训练在本地完成（见 `02_production.ipynb`），通过 `learn.export()` 导出单文件 `export.pkl`（约 45MB，含结构、权重、预处理与类别词表）；部署端只需 `load_learner("export.pkl")`。
- **用 Gradio 构建界面**：`gr.Interface` 高层封装，输入图片、输出带概率标签（`gr.Label(num_top_classes=3)`），几行代码生成完整 UI。
- **选 Hugging Face Spaces 而非 Binder**：Binder 会话空闲即回收、子域名网络可达性差（多次 `Binder inaccessible` / `424`）；HF Spaces 免费、持久、单域名稳定，闲置仅休眠、访问即唤醒。
- **解决跨平台 / 跨版本部署坑**（模型在 Windows + Python 3.13 导出，部署到 Linux）：
  - `WindowsPath` 无法在 Linux 重建 → 加载前映射 `WindowsPath → PosixPath`（仅 POSIX）。
  - `pathlib._local` 仅 Python 3.13 有 → Space 固定使用 Python 3.13。
  - Python 3.13 移除 `audioop` 而 gradio 依赖的 `pydub` 需要它 → 加 `audioop-lts`。
  - 反序列化需 `cloudpickle` / `fasttransform` / `plum` / `numpy(_core)` 等 → 在 `requirements.txt` 固定版本。
  - `fastai` / `fastcore` / `torch` / `numpy` 等钉到与导出时一致的版本。
  - **Gradio 版本策略**：直接用最新版 gradio（6.x），由它自动拉取配套的 `fastapi`/`starlette`/`pydantic`/`huggingface_hub`，避免"旧 gradio 撞新依赖"的不兼容。

## 四、用到的主要模块

```text
hf_space/
├── app.py              # Gradio 应用主程序
├── requirements.txt    # 依赖声明
├── README.md           # 本文件：HF Space 配置 + 说明文档
├── export.pkl          # 训练导出的 fastai 模型（约 45MB）
└── examples/           # 示例图片（black / grizzly / teddy）
```

| 模块 / 库 | 作用 |
|-----------|------|
| **fastai** (`fastai.vision.all`) | 加载模型 `load_learner`、图像封装 `PILImage`、执行预测 `learn.predict` |
| **gradio** | 构建 Web 界面（`gr.Interface` / `gr.Image` / `gr.Label`）并启动服务 |
| **PyTorch** (`torch` / `torchvision`) | 底层深度学习框架，承载 ResNet 推理 |
| **fastcore / fasttransform / plum-dispatch** | fastai 底层依赖，反序列化时被引用 |
| **cloudpickle** | 模型 pickle 部分对象的序列化支持 |
| **numpy** | 数值数组运算（pickle 引用 `numpy._core`） |
| **PIL (Pillow)** | 图像读取与处理 |
| **pathlib** | 路径处理；跨平台 `WindowsPath → PosixPath` 补丁 |
| **audioop-lts** | 为 Python 3.13 提供 `audioop`，满足 gradio 依赖的 `pydub` |

## 五、本地运行（可选）

```bash
cd hf_space
pip install -r requirements.txt
python app.py
```

启动后访问终端提示的本地地址（默认 `http://127.0.0.1:7860`）。

<p align="right"><a href="#-bear-classifier">⬆ 回到顶部</a></p>

</details>

---

<a id="-english"></a>

<details>
<summary><b>🇬🇧 English (click to expand / collapse)</b></summary>

## Live App

- **App link**: <https://yaphets429-bear-classifier-test.hf.space/>
- **Platform**: Hugging Face Spaces (Gradio SDK)
- Opens directly as a web UI — no local setup required.

## 1. Purpose

A deep-learning **image classification web app** that identifies which of three bear types an uploaded image belongs to:

| Class | Meaning |
|-------|---------|
| `black`   | Black bear |
| `grizzly` | Grizzly / brown bear |
| `teddy`   | Teddy bear (toy) |

The model comes from the classic example in the fastai course *Practical Deep Learning for Coders*. Training data was collected via an image crawler and fine-tuned with transfer learning (ResNet). The goal is to **deploy the trained model as an online demo anyone can use in a browser**.

## 2. How to Use

1. Open the app link.
2. Upload an image in the **"Upload a bear image"** area (click or drag & drop). Three example images at the bottom can be clicked for quick testing.
3. The model predicts automatically; the **"Prediction"** area shows the most likely class and **confidence probabilities** per class (top 3).
4. To test another image, just upload a new one.

> On the first visit, if the Space is asleep, expect a few tens of seconds for wake-up/loading — this is normal.

## 3. Main Design Ideas

- **Separation of training and inference**: training is done locally (see `02_production.ipynb`) and exported via `learn.export()` into a single `export.pkl` (~45MB, containing architecture, weights, preprocessing, and the class vocabulary); deployment only calls `load_learner("export.pkl")`.
- **UI built with Gradio**: the high-level `gr.Interface` takes an image input and returns a labeled-probability output (`gr.Label(num_top_classes=3)`) — a complete UI in a few lines.
- **Hugging Face Spaces over Binder**: Binder sessions are reclaimed when idle and its sub-domain had poor reachability (repeated `Binder inaccessible` / `424`); HF Spaces is free, persistent, single-domain and stable, sleeping when idle and waking on access.
- **Cross-platform / cross-version fixes** (model exported on Windows + Python 3.13, deployed to Linux):
  - `WindowsPath` can't be rebuilt on Linux → map `WindowsPath → PosixPath` before loading (POSIX only).
  - `pathlib._local` exists only in Python 3.13 → the Space is fixed to Python 3.13.
  - Python 3.13 removed `audioop` but gradio's `pydub` needs it → add `audioop-lts`.
  - Deserialization needs `cloudpickle` / `fasttransform` / `plum` / `numpy(_core)` → pin versions in `requirements.txt`.
  - `fastai` / `fastcore` / `torch` / `numpy` pinned to the same versions used at export time.
  - **Gradio version strategy**: use the latest gradio (6.x) and let it pull matching `fastapi`/`starlette`/`pydantic`/`huggingface_hub`, avoiding "old gradio meets new transitive deps" incompatibilities.

## 4. Main Modules Used

```text
hf_space/
├── app.py              # Gradio app entry point
├── requirements.txt    # Dependency declarations
├── README.md           # This file: HF Space config + documentation
├── export.pkl          # Exported fastai model (~45MB)
└── examples/           # Example images (black / grizzly / teddy)
```

| Module / Library | Role |
|------------------|------|
| **fastai** (`fastai.vision.all`) | Load the model (`load_learner`), wrap images (`PILImage`), run prediction (`learn.predict`) |
| **gradio** | Build the web UI (`gr.Interface` / `gr.Image` / `gr.Label`) and launch the server |
| **PyTorch** (`torch` / `torchvision`) | Underlying DL framework powering ResNet inference |
| **fastcore / fasttransform / plum-dispatch** | fastai low-level deps, referenced during deserialization |
| **cloudpickle** | Serialization support for certain objects in the model pickle |
| **numpy** | Numerical array operations (pickle references `numpy._core`) |
| **PIL (Pillow)** | Image reading and processing |
| **pathlib** | Path handling; cross-platform `WindowsPath → PosixPath` patch |
| **audioop-lts** | Provides `audioop` for Python 3.13, satisfying gradio's `pydub` |

## 5. Running Locally (optional)

```bash
cd hf_space
pip install -r requirements.txt
python app.py
```

Then open the local address shown in the terminal (default `http://127.0.0.1:7860`).

<p align="right"><a href="#-bear-classifier">⬆ Back to top</a></p>

</details>
