import torch
import gradio as gr
from InferenceServer import inferVedio
from file.base64.toBase64 import image_to_base64
# 预设的默认视频路径
DEFAULT_VIDEOS = {
    "demo1": "path.......................................................",
    "demo2": "path.......................................................",
    "demo3": "path.......................................................",
    # "demo1": "path.......................................................",
    # "demo2": "path.......................................................",
    # "demo3": "path.......................................................",
    "上传视频": None  # 允许用户上传视频
}

def infer_video_wrapper(video_choice, uploaded_video):
    """根据用户的选择，使用默认视频或上传视频"""
    if video_choice == "上传视频" and uploaded_video is not None:
        video_path = uploaded_video
    elif video_choice in DEFAULT_VIDEOS:
        video_path = DEFAULT_VIDEOS[video_choice]
    else:
        return "请上传视频或选择默认视频"

    output_path = inferVedio(video_path, 90, torch.device('cuda' if torch.cuda.is_available() else 'cpu'))
    return output_path

# 创建 Gradio 界面
with gr.Blocks(theme=gr.themes.Soft()) as iface:
    # 顶部布局：Logo、标题和提示
    with gr.Row():
        try:
            icon_path="file/base64/icon.png"
            icon_base64=image_to_base64(icon_path)
        except Exception as e:
            print(f"图像文件无效: {e}")


        gr.HTML(
            f"""
            <div style="text-align: left;">
                <img src="data:image/png;base64,{icon_base64}" alt="Logo" style="width: 250px; height: auto;">
            </div>
            """
        )

        # 标题和提示
        with gr.Column(scale=4):
            # 标题
            gr.HTML(
                """
                <h1 style='margin: 0; text-align: left; font-size: 40px; font-family: Arial, sans-serif; font-weight: bold; color: #2575fc;'>
                    ************************************
                </h1>
                """
            )

            # 提示
            gr.HTML(
                """
                <div style='text-align: left; font-size: 18px; color: #555; margin-top: 10px;'>
                    🧠 **********************************<br>
                    💡 特点：********* | ******* | **********<br>
                    🚀 提示：*********************************
                </div>
                """
            )

    # 视频选择和上传区域
    with gr.Row():
        with gr.Column():
            gr.Markdown("### 选择或上传视频")
            video_choice = gr.Radio(
                label="选择视频",
                choices=list(DEFAULT_VIDEOS.keys()),
                value="真实视频1",
                interactive=True
            )
            uploaded_video = gr.File(label="上传视频", type="filepath", interactive=True)
            submit_btn = gr.Button("开始检测", variant="primary")

        # 视频播放区域
        with gr.Column():
            gr.Markdown("### 视频播放")
            video_display = gr.Video(label="原始视频", interactive=False)
            output_video = gr.Video(label="处理后的视频", interactive=False)

    # 当用户选择视频时更新默认视频播放
    def update_video_display(video_choice, uploaded_video):
        if video_choice == "上传视频" and uploaded_video:
            return uploaded_video
        if video_choice in DEFAULT_VIDEOS:
            return DEFAULT_VIDEOS[video_choice]
        return DEFAULT_VIDEOS["真实视频1"]

    # 设置事件处理
    video_choice.change(update_video_display, inputs=[video_choice, uploaded_video], outputs=video_display)
    uploaded_video.change(update_video_display, inputs=[video_choice, uploaded_video], outputs=video_display)
    submit_btn.click(
        fn=infer_video_wrapper,
        inputs=[video_choice, uploaded_video],
        outputs=output_video
    )

    # 自定义 CSS 样式
    iface.css = """
    .icon-style {
        border-radius: 20px;
        margin-right: 20px;
    }
    .gradio-container {
        max-width: 1200px;
        margin: auto;
        padding: 20px;
    }
    .gradio-button, .gradio-file, .gradio-radio, .gradio-video {
        box-shadow: none !important;
    }
    """

if __name__ == "__main__":
    iface.launch()
