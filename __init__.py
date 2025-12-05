# __init__.py

# 從您的主程式檔案中導入節點類別和映射
from .z_image_json_prompt import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

# 匯出這些映射，讓 ComfyUI 可以正確讀取
__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']