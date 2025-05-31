import os
import gradio as gr
from PIL import Image
import numpy as np

# 確保資料夾存在
os.makedirs("data", exist_ok=True)
os.makedirs("results", exist_ok=True)

def infer(img: Image.Image):
    width, height = img.size
    res = np.ones((height, width, 3))
    print(res.shape)
    print(width)

    img.save("./data/data.png")
    img.save("./results/data.png")

    # 執行模型
    os.system('python main_test_swinir.py')

    result_path = "./results/data.png"
    if os.path.exists(result_path):
        return result_path, result_path
    else:
        return None, None

inputs = gr.Image(type='pil', label="Original Image")
outputs = [
    gr.Image(type='filepath', label="Output"),
    gr.File(label="Download")
]

title = "SwinIR: Image Restoration Using Swin Transformer (Super-Resolution)"
description = "Gradio demo for SwinIR: Super-Resolution. Upload an image or choose an example below."
article = """
<p style='text-align: center'>
<a href='https://arxiv.org/pdf/2108.10257.pdf' target='_blank'>SwinIR Paper</a> | 
<a href='https://github.com/JingyunLiang/SwinIR' target='_blank'>GitHub Repo</a>
</p>
"""

examples = [["example.png"]]

# 正確的 Gradio 5.x 寫法
demo = gr.Interface(
    fn=infer,
    inputs=inputs,
    outputs=outputs,
    title=title,
    description=description,
    article=article,
    examples=examples,
    flagging_mode="never"  # 替代 allow_flagging
)

demo.queue()  # 啟用排程隊列（取代 enable_queue）
demo.launch(share=False)
