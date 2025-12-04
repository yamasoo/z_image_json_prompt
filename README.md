📦 ComfyUI 節點安裝與使用說明
1. 安裝步驟
🔧 前置需求
已安裝 ComfyUI（建議使用最新版）

Python 3.10+

Git（用於下載插件）

📥 安裝方式
進入 ComfyUI 的 custom_nodes 資料夾：

bash
cd ComfyUI/custom_nodes
將此節點專案放入 custom_nodes 目錄下，例如：

bash
git clone https://github.com/your-repo/comfyui-zimage-jsonprompt.git
或者直接將 z_image_json_prompt.py 放入 custom_nodes/ZImageJSONPrompting/ 目錄。

確認結構如下：

程式碼
ComfyUI/
└── custom_nodes/
    └── ZImageJSONPrompting/
        ├── z_image_json_prompt.py
        ├── README.md
        └── (其他資源檔案)
重新啟動 ComfyUI，節點會自動載入。

2. 使用方式
🧩 節點功能
此節點的核心是 ZImageJSONPrompting 類別，提供以下功能：

選項管理：場景、角色、攝影、光線、風格等多維度的雙語選項。

模板系統：內建多種預設模板（如 Cyberpunk、Fantasy Magic、Sci-fi Futuristic…）。

隨機組合：可隨機生成不同的 prompt 組合，適合批量生成或探索多樣化風格。

JSON 輸出：生成結構化的 JSON，方便與其他節點或外部工具整合。

⚙️ 節點輸入/輸出
輸入：

模板名稱（如 cyberpunk、fantasy_magic）

或自定義選項（scene、subject、photography、lighting、style）

輸出：

一個完整的 JSON prompt 字串

可直接餵給 ComfyUI 的 Text-to-Image 節點 或其他 prompt 處理節點

📖 使用範例
1. 使用預設模板
選擇 cyberpunk 模板，輸出 JSON：

json
{
  "scene_description": "霓虹閃爍的賽博朋克街道 | Neon-lit cyberpunk street",
  "time_atmosphere": "深夜的神秘月光 | Mysterious moonlight late at night",
  "color_scheme": "青橙配色方案 | Teal and orange color scheme",
  "art_style": "賽博朋克風格 | Cyberpunk style",
  "light_source_type": "霓虹燈光 | Neon lights",
  "render_effects": "鏡頭光暈效果 | Lens flare effect"
}
2. 隨機生成
可呼叫隨機組合功能，輸出不同場景與角色：

json
{
  "scene_description": "夢幻的童話森林 | Enchanted fairy tale forest",
  "character_features": "美麗的精靈族 | Beautiful elf race",
  "clothing_style": "奇幻的魔法師長袍 | Fantasy mage robe",
  "pose_expression": "舞蹈中的優雅動作 | Elegant movement while dancing",
  "shooting_angle": "低角度仰拍 | Low angle looking up",
  "film_style": "柯達 Portra 柔和膚色 | Kodak Portra soft skin tones"
}
3. 與 ComfyUI 整合
在 Text Prompt 節點 前插入此節點

輸出 JSON → 轉換成文字 prompt → 餵給 Stable Diffusion 節點

可搭配 批量生成 或 隨機化，快速探索不同風格

3. 建議用途
AI 藝術生成：快速構建複雜的場景與角色描述

VTuber/二次元風格探索：結合日式動漫與奇幻模板

系統化工作流：適合 YAML/Excel 管理，批量生成多樣化 prompt
