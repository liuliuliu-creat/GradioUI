import base64

def image_to_base64(image_path):
    """
    将图片文件转换为 Base64 编码字符串。

    参数:
        image_path (str): 图片文件的路径。

    返回:
        str: Base64 编码的字符串。
    """
    try:
        with open(image_path, "rb") as image_file:
            # 读取图片文件的二进制数据
            image_data = image_file.read()
            # 将二进制数据编码为 Base64 字符串
            base64_encoded = base64.b64encode(image_data).decode("utf-8")
            return base64_encoded
    except Exception as e:
        print(f"Error converting image to Base64: {e}")
        return None