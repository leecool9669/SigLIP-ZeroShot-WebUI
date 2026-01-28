# -*- coding: utf-8 -*-
"""SigLIP Base Patch16-224 零样本图像分类 WebUI（前端展示，不加载模型）"""
import gradio as gr


def run_zero_shot(image, candidate_labels_text):
    """零样本分类占位：仅展示界面与结果区域，不执行模型推理。"""
    if image is None:
        return None, "请上传一张图片，并输入候选标签（多个标签用英文逗号分隔）。\n\n加载模型后，将在此显示各候选类别的置信度分数。"
    labels = [s.strip() for s in (candidate_labels_text or "").split(",") if s.strip()]
    if not labels:
        return image, "请在「候选标签」中输入至少一个标签，多个标签用英文逗号分隔。\n\n示例：playing music, playing sports, a photo of cats"
    lines = ["【演示模式】未加载模型，以下为示例输出格式：\n"]
    for lb in labels:
        lines.append(f"  • {lb}: -- (加载模型后显示分数)")
    return image, "\n".join(lines)


with gr.Blocks(title="SigLIP Base Patch16-224 WebUI") as demo:
    gr.Markdown(
        "# SigLIP Base Patch16-224 WebUI\n\n"
        "零样本图像分类可视化界面（224×224 输入，支持上传图片与自定义候选标签）"
    )
    with gr.Row():
        with gr.Column(scale=1):
            input_image = gr.Image(label="上传图片", type="pil")
            candidate_labels = gr.Textbox(
                label="候选标签（多个用英文逗号分隔）",
                placeholder="例如: playing music, playing sports, a photo of cats",
                lines=2,
            )
            run_btn = gr.Button("零样本分类", variant="primary")
        with gr.Column(scale=1):
            output_image = gr.Image(label="输入预览", type="pil")
            output_text = gr.Textbox(label="分类结果", lines=8)
    run_btn.click(
        fn=run_zero_shot,
        inputs=[input_image, candidate_labels],
        outputs=[output_image, output_text],
    )
    gr.Markdown(
        "---\n**模型说明**：SigLIP 为基于 Sigmoid 损失的视觉-语言预训练模型，本界面用于加载 "
        "SigLIP-Base-Patch16-224（224×224 输入）进行零样本图像分类与结果可视化。"
    )


if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, share=False)
