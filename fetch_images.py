# -*- coding: utf-8 -*-
"""下载模型页面相关图片到 template/images，使用代理 127.0.0.1:18081"""
import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:
    os.system(f'"{sys.executable}" -m pip install requests -q')
    import requests

_base = Path(__file__).resolve().parent
_img = _base / "images"
_img.mkdir(parents=True, exist_ok=True)
proxies = {"http": "http://127.0.0.1:18081", "https": "http://127.0.0.1:18081"}
urls = [
    ("https://cdn-thumbnails.hf-mirror.com/social-thumbnails/models/google/siglip-base-patch16-224.png", str(_img / "siglip_model_page.png")),
    ("https://hf-mirror.com/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/siglip_table.jpeg", str(_img / "siglip_table.jpeg")),
]
for url, path in urls:
    try:
        r = requests.get(url, timeout=30, proxies=proxies)
        r.raise_for_status()
        with open(path, "wb") as f:
            f.write(r.content)
        print("ok:", path)
    except Exception as e:
        print("skip", path, str(e))
