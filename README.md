# 🎉 welcome 🎉

# 🎉 这是一个简洁直观的 Gradio 界面，让你轻松处理和分析视频。你可以选择默认视频或上传自己的视频进行处理，处理结果将实时展示。🎉
![image](https://github.com/user-attachments/assets/0f9894a0-3273-4032-bf17-ee57ffe24aca)


## 🚀 环境准备

### 1. 安装依赖

## 确保已安装 Python 3.7 及以上版本。

## 然后，使用以下命令安装所需的 Python 库：

```bash
pip install gradio
```

## 📂 项目结构
```bash
├── InferenceGradioV5.py            # 启动 Gradio 界面的脚本
├── InferenceGradioV5.py  # 视频处理与检测的核心脚本
├── file/             # 存放图标、视频文件等资源
│   └── icon.png      # 可自定义的 Logo 图标
└── README.md         # 项目的文档文件

```
## 🌟 页面风格与内容
## 页面风格

- 主题: 使用 Gradio 的 Soft 主题，整体界面简洁、现代，适合用户进行交互操作。
- 布局: 页面分为顶部布局和视频处理区域两部分。

## 顶部布局

- 包含 Logo、标题和提示信息，Logo 以 Base64 编码形式嵌入，确保在不同环境下都能正常显示。
视频处理区域

- 分为视频选择/上传区域和视频播放区域，用户可以在此选择视频、上传视频并查看处理结果。
### 页面内容

- Logo 与标题: Logo 位于页面左上角，标题紧随其后，使用大号字体和蓝色调，突出显示。提示信息位于标题下方，简要介绍了工具的特点和使用提示。
- 视频选择与上传: 用户可以通过单选按钮选择预设的默认视频，或通过文件上传功能上传自己的视频。
- 视频播放区域: 左侧显示原始视频，右侧显示处理后的视频。用户可以通过点击“开始检测”按钮启动视频处理流程，处理后的视频将在右侧区域展示。

## 🛠 使用步骤

### 选择视频:
- 在“选择视频”区域，用户可以从预设的默认视频中选择一个，或选择“上传视频”以上传自定义视频。

### 上传视频（可选）:
- 如果选择了“上传视频”，点击“上传视频”按钮，选择本地视频文件进行上传。

### 开始检测:
- 点击“开始检测”按钮，系统将开始处理视频。处理完成后，处理后的视频将显示在右侧的“处理后的视频”区域。

### 查看结果:
- 处理后的视频会自动播放，用户可以查看处理效果。

## 🛠 自定义与扩展

### 自定义 Logo
- 可以通过替换 file/icon.png 文件来自定义 Logo。
  
### 添加更多默认视频
- 在 DEFAULT_VIDEOS 字典中添加更多预设视频路径。
  
### 修改处理逻辑
- 可以在 inferVedio 函数中修改视频处理的逻辑，以适应不同的需求。

# 🎉就这样！🚀
