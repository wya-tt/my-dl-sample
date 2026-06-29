<!-- 仓库级 README（中英双语）。
     GitHub 的 Markdown 不支持 JS 切换，
     因此使用「顶部语言锚点 + 可折叠 <details> 分段」实现双语阅读。 -->

# 🧠 my-dl-sample

**🌐 Language / 语言：[中文](#-中文) · [English](#-english)**

> A growing collection of small deep-learning learning projects.
> 一个持续更新的深度学习练习项目合集。

---

<a id="-中文"></a>

<details open>
<summary><b>🇨🇳 中文（点击展开 / 收起）</b></summary>

## 简介

这个仓库收录了我在学习深度学习过程中做的一些小项目（learning projects）。
内容主要参考 fastai 课程《Practical Deep Learning for Coders》等资料，目标是**边学边做、并把成果部署成可访问的在线 demo**。

目前包含第一个项目：**熊类图像分类器（Bear Classifier）**。后续会陆续加入更多项目。

## 项目列表

| # | 项目 | 简介 | 链接 |
|---|------|------|------|
| 1 | **Bear Classifier 熊类分类器** | 基于 fastai + ResNet 的图像分类，识别图片是黑熊 / 灰熊 / 泰迪熊；部署在 Hugging Face Spaces（Gradio） | [在线 Demo](https://yaphets429-bear-classifier-test.hf.space/) · [说明文档](bear-classifier/hf_space/README.md) |
| … | *后续项目* | 敬请期待 | — |

## 仓库结构

```text
my-dl-sample/
├── README.md                   # 本文件：仓库总览
└── bear-classifier/            # 项目 1：熊类分类器
    ├── 02_production.ipynb     # 学习/训练笔记（fastai 课程 production 章节）
    ├── export.pkl              # 训练导出的模型
    ├── bears/                  # 训练用的熊图片数据集
    ├── images/                 # 辅助图片
    ├── binder/                 # 早期 Binder + Voilà 部署（已弃用，存档）
    │   ├── bear_classifier.ipynb
    │   ├── requirements.txt
    │   ├── runtime.txt
    │   └── README.md           # 说明思路、遇到的困难、为何迁移到 HF
    └── hf_space/               # 当前 Hugging Face Spaces 部署
        ├── app.py              # Gradio 应用
        ├── requirements.txt    # 依赖
        ├── README.md           # Space 配置 + 该项目详细文档（双语）
        ├── export.pkl          # 部署用模型
        └── examples/           # 示例图片
```

## 用到的主要技术

- **fastai / PyTorch**：模型训练与推理（迁移学习，ResNet）
- **Gradio**：构建交互式 Web 界面
- **Hugging Face Spaces**：免费、持久地托管在线 demo

## 后续计划

- 加入更多深度学习练习项目（如其他图像/文本任务）
- 每个项目尽量配套：可运行的 notebook + 在线 demo + 文档

<p align="right"><a href="#-my-dl-sample">⬆ 回到顶部</a></p>

</details>

---

<a id="-english"></a>

<details>
<summary><b>🇬🇧 English (click to expand / collapse)</b></summary>

## Overview

This repository collects small deep-learning **learning projects** I build while studying.
It mainly follows resources such as the fastai course *Practical Deep Learning for Coders*, with the goal of **learning by doing and deploying the results as accessible online demos**.

It currently contains the first project: the **Bear Classifier**. More projects will be added over time.

## Projects

| # | Project | Description | Links |
|---|---------|-------------|-------|
| 1 | **Bear Classifier** | fastai + ResNet image classification telling black / grizzly / teddy bears apart; deployed on Hugging Face Spaces (Gradio) | [Live Demo](https://yaphets429-bear-classifier-test.hf.space/) · [Docs](bear-classifier/hf_space/README.md) |
| … | *future projects* | Stay tuned | — |

## Repository Structure

```text
my-dl-sample/
├── README.md                   # This file: repository overview
└── bear-classifier/            # Project 1: Bear Classifier
    ├── 02_production.ipynb     # Study/training notebook (fastai "production" chapter)
    ├── export.pkl              # Exported trained model
    ├── bears/                  # Bear image dataset used for training
    ├── images/                 # Auxiliary images
    ├── binder/                 # Early Binder + Voilà deployment (deprecated, archived)
    │   ├── bear_classifier.ipynb
    │   ├── requirements.txt
    │   ├── runtime.txt
    │   └── README.md           # Notes the approach, difficulties, and why moved to HF
    └── hf_space/               # Current Hugging Face Spaces deployment
        ├── app.py              # Gradio app
        ├── requirements.txt    # Dependencies
        ├── README.md           # Space config + detailed bilingual docs
        ├── export.pkl          # Model used for deployment
        └── examples/           # Example images
```

## Main Technologies

- **fastai / PyTorch**: model training and inference (transfer learning, ResNet)
- **Gradio**: building the interactive web UI
- **Hugging Face Spaces**: free, persistent hosting for the online demo

## Roadmap

- Add more deep-learning learning projects (e.g. other image/text tasks)
- For each project, aim to provide: a runnable notebook + an online demo + documentation

<p align="right"><a href="#-my-dl-sample">⬆ Back to top</a></p>

</details>
