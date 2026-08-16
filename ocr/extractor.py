
import pytesseract
from PIL import Image


def extract_text(image_path):
    """
    繁体中文 + 简体中文 + 英文 OCR
    需要环境安装 chi_sim / chi_tra / eng 语言包
    """

    img = Image.open(image_path)

    text = pytesseract.image_to_string(
        img,
        lang="chi_tra+chi_sim+eng"
    )

    return text.strip()
