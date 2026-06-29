import os
import pathlib

# The model was exported on Windows (Python 3.13), so the pickled paths are
# WindowsPath objects. On a Linux Space they cannot be reconstructed, so map
# WindowsPath -> PosixPath before loading. Only do this on POSIX systems.
if os.name == "posix":
    pathlib.WindowsPath = pathlib.PosixPath
    if hasattr(pathlib, "_local"):
        pathlib._local.WindowsPath = pathlib._local.PosixPath

from fastai.vision.all import load_learner, PILImage
import gradio as gr

learn = load_learner("export.pkl")
labels = learn.dls.vocab


def predict(img):
    img = PILImage.create(img)
    pred, pred_idx, probs = learn.predict(img)
    return {str(labels[i]): float(probs[i]) for i in range(len(labels))}


demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil", label="Upload a bear image"),
    outputs=gr.Label(num_top_classes=3, label="Prediction"),
    title="Bear Classifier",
    description="Upload a bear image to predict whether it is a black bear, grizzly bear, or teddy bear.",
    examples=[f for f in ["examples/black.jpg", "examples/grizzly.jpg", "examples/teddy.jpg"]],
)

if __name__ == "__main__":
    demo.launch()
