# Binder + Voilà 部署（已弃用，存档）

> 这个文件夹保存了熊类分类器**最初**的部署尝试：用 **Voilà + Binder** 把训练好的 notebook 变成网页应用。
> 后来因为一系列问题，项目迁移到了 **Hugging Face Spaces**（见上一级目录的 [`hf_space/`](../hf_space/)）。
> 此处仅作过程记录与存档，**不再维护**。

---

## 一、这里有什么

| 文件 | 作用 |
|------|------|
| `bear_classifier.ipynb` | 用 ipywidgets 写的交互式 notebook：上传图片 → 调用模型 → 显示预测结果。Voilà 会把它渲染成纯网页 app（隐藏代码，只留交互控件）。 |
| `requirements.txt` | Binder 构建环境时用的 pip 依赖。 |
| `runtime.txt` | 指定 Binder 使用的 Python 版本（`python-3.11`）。 |

> 模型文件 `export.pkl` 在上一级目录（`../export.pkl`）。原始 Binder 部署时它和 notebook 放在仓库根目录。

## 二、设计思路

1. **训练 → 导出**：在 `02_production.ipynb` 中用 fastai 训练熊类分类器，`learn.export()` 导出为 `export.pkl`。
2. **做交互界面**：在 `bear_classifier.ipynb` 中用 `ipywidgets` 搭一个简单 UI（上传按钮、分类按钮、结果标签），加载 `export.pkl` 进行推理。
3. **Voilà 渲染**：Voilà 能把 notebook 转成不显示代码的网页应用。
4. **Binder 托管**：把仓库交给 [mybinder.org](https://mybinder.org)，它会根据 `requirements.txt` + `runtime.txt` 自动构建一个临时容器环境，并通过 `?urlpath=voila/render/bear_classifier.ipynb` 直接打开 Voilà 页面。

## 三、遇到的困难

部署过程中踩了很多坑，主要包括：

1. **环境配置冲突**
   - 仓库里同时存在 `environment.yml`（conda）和 `requirements.txt`（pip），Binder 优先用了 `environment.yml`，导致 conda 装的 PyTorch 与 pip 钉的 `torch` 版本互相冲突。
   - 过度精确的版本钉死（从本地 Windows 环境导出的版本）在 Binder 的 Linux 环境里找不到对应 wheel，构建失败。

2. **大模型文件上传**
   - `export.pkl` 约 45MB，超过 GitHub 网页上传 25MB 的限制，只能改用命令行 `git push`（上限 100MB）。

3. **会话不稳定 / 无法访问**（最致命）
   - Binder 会话是**临时**的，**空闲约 10 分钟就被回收**，认证 cookie 失效后页面变成 `Binder inaccessible`。
   - 页面经常**卡在 "Launching…" 不自动跳转**：日志里服务器已 `ready`，但前端迟迟不跳到 Voilà。
   - 等待过程中会话超时被回收，最终出现 `424` 错误。
   - 推测根因：实际应用跑在 `hub.2i2c.mybinder.org` 子域名上，本地网络对该子域名**可达性差**，主站能看日志、却跳不过去。

4. **Voilà 执行报错被隐藏**
   - 出现过 `There was an error when executing cell [1]` 的笼统提示，需要额外加 `--show_tracebacks=True` 才能看到真实报错，调试体验差。

## 四、为什么迁移到 Hugging Face Spaces

综合来看，Binder 的定位是"**临时演示**"，并不适合做长期、稳定可访问的 demo。对比之下选择了 **Hugging Face Spaces**：

| 维度 | Binder | Hugging Face Spaces |
|------|--------|---------------------|
| 持久性 | 空闲即回收、会话短命 | **持久**；闲置只是休眠，访问即唤醒 |
| 访问稳定性 | 跳转到 `hub.2i2c` 子域名，易卡住/超时 | **单一域名**，访问稳定 |
| 部署方式 | Voilà + notebook + Binder 构建 | **Gradio**，几十行 `app.py` 即可 |
| 适用场景 | 一次性临时演示 | **长期可用的在线 demo** |

因此项目改用 Gradio 重写界面并部署到 HF Spaces，详见上一级目录的 [`hf_space/`](../hf_space/)。

## 五、（仅供参考）原 Binder 启动链接

```text
https://mybinder.org/v2/gh/wya-tt/my-dl-sample/main?urlpath=%2Fvoila%2Frender%2Fbear_classifier.ipynb
```

> 注意：由于仓库已重组、文件路径变化，且项目已迁移到 HF，该链接**不再保证可用**，仅作历史记录。
