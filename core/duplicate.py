import hashlib
from pathlib import Path


def image_hash(path):
    data = Path(path).read_bytes()
    return hashlib.md5(data).hexdigest()


def check_image(path):
    h = image_hash(path)

    # 第二阶段先完成图片接收和Hash入口
    # 后续接AI相似搜索数据库

    print("图片Hash:", h)

    return None
