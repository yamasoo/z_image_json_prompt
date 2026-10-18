# Z-Image-JSON-Prompt 🏷️

**一個強大且結構化的 ComfyUI 提示詞生成器。**

Z-Image-JSON-Prompt 節點旨在解決傳統文字提示詞缺乏組織和難以管理的問題。它將圖像生成的關鍵元素（場景、主體、攝影、燈光、風格）結構化，讓使用者透過清晰的選項列表和預設模板，快速生成複雜、高品質的提示詞。

### ✨ 核心功能

* **結構化輸入**：將提示詞分解為五大類（場景、主體、攝影、燈光、風格）共十五個子選項，構建邏輯清晰。
* **選項自訂**：所有選項存放在 `z_image_options` 目錄下的 `.txt` 檔案，直接編輯即可**增加或修改提示詞選項**，節點不會覆蓋你修改過的檔案。
* **內建風格模板**：提供二十種風格模板（賽博朋克、奇幻魔法、電影人像、日式動漫系列等），一鍵套用；也可選「隨機模板」。
* **可重現結果**：固定 `seed` 即可重現同一組隨機選擇。
* **多語言輸出**：支援 **中文、英文、雙語** 三種模式，正面與負面提示詞都會依語言切換。
* **多格式輸出**：
    * **`json_prompt`**：包含所有設定的結構化 JSON，方便追溯、存檔或程式化使用。
    * **`positive_text`**：四段式（核心、環境、技術、風格）純文字提示詞，可直接接到文字編碼節點。
* **細節等級控制**：「簡略」、「標準」、「詳細」、「極度詳細」四種豐富度。

### 🚀 安裝與使用

#### 1. 安裝

```bash
cd ComfyUI/custom_nodes
git clone https://github.com/yamasoo/z_image_json_prompt.git
```

重新啟動 ComfyUI 後，可在 **`Z-Image`** 類別下找到 **`Z-Image JSON Prompt Generator`** 節點。本節點只使用 Python 標準函式庫，不需要額外安裝套件。

#### 2. 選項與模板檔案

`z_image_options` 目錄結構如下：

* **五個分類資料夾**（`scene`、`subject`、`photography`、`lighting`、`style`），每個資料夾內有三個 `.txt` 選項檔。
* **`templates` 資料夾**，內含 `.json` 風格模板。

選項檔每行一個選項，格式為 `中文 | English`。若缺少某個檔案，節點啟動時會用內建預設值建立；已存在的檔案永遠不會被改寫。

選項與模板的值都可以使用 `{甲| 乙| 丙}` 語法，每次生成時隨機挑一個；中英文兩半會挑同一個位置，例如：

```text
{黎明| 黃昏| 夜晚}的氛圍 | {Dawn| Dusk| Night} atmosphere
```

#### 3. 自訂模板

在 `templates` 資料夾新增一個 `.json` 檔即可，檔名就是模板 ID：

```json
{
  "name": "我的風格 | My Style",
  "fields": {
    "scene_description": "雨後的都市夜景 | City night scene after rain",
    "color_scheme": "{青橙| 紫藍}配色 | {Teal and orange| Purple-blue} palette"
  }
}
```

`fields` 可用的欄位名稱：

| 分類 | 欄位 |
| :--- | :--- |
| 場景 | `scene_description`、`time_atmosphere`、`environment_setting` |
| 主體 | `character_features`、`clothing_style`、`pose_expression` |
| 攝影 | `lens_parameters`、`shooting_angle`、`film_style` |
| 燈光 | `light_source_type`、`light_effect`、`contrast_level` |
| 風格 | `art_style`、`color_scheme`、`render_effects` |

其他欄位名稱會被忽略，並在主控台提示。

#### 4. 節點輸入參數

| 參數名稱 | 類型 | 說明 | 預設值 |
| :--- | :--- | :--- | :--- |
| **`【...】_...`** | 選擇列表 | 十五個欄位。選 **`隨機 \| Random`** 會從對應檔案隨機抽取，選 **`無 \| None`** 則留空。 | `隨機 \| Random` |
| **`language_choice`** | 選擇列表 | 輸出語言（中文 / English / 雙語）。 | `雙語 \| Bilingual` |
| **`style_template`** | 選擇列表 | 風格模板，或「隨機模板」。 | `無模板 \| No Template` |
| **`detail_level`** | 選擇列表 | 提示詞的豐富度。 | `標準 \| Standard` |
| **`negative_prompt`** | 文字 | 負面提示詞，以逗號分隔，會依語言逐項切換。 | 低品質相關詞 |
| **`seed`** | 整數 | 固定後可重現結果；`0` 表示每次重新隨機。 | `0` |
| **`template_mode`** | 選擇列表 | **模板優先**：模板定義的欄位取代隨機或手選的值。**只填空白**：只填入設為「無」的欄位。 | 模板優先 |

選「隨機模板」時，每個模板欄位約有 70% 機率被套用，保留部分隨機變化。

#### 5. 節點輸出

| 輸出名稱 | 類型 | 說明 |
| :--- | :--- | :--- |
| **`json_prompt`** | `STRING` | 完整的結構化 JSON，包含所有設定與 seed 等元數據。 |
| **`positive_text`** | `STRING` | 四段式純文字提示詞。 |
| **`negative_prompt`** | `STRING` | 依語言處理後的負面提示詞。 |

### 🤝 貢獻

歡迎提交 Pull Request 或 Issues 來改進本專案：

1. Fork 本儲存庫。
2. 建立新的功能分支（`git checkout -b feature/AmazingFeature`）。
3. 提交變更（`git commit -m 'Add some AmazingFeature'`）。
4. 推送到分支（`git push origin feature/AmazingFeature`）。
5. 開啟 Pull Request。

版本紀錄見 [CHANGELOG.md](CHANGELOG.md)。

### 📝 授權

本專案採用 [MIT 授權](LICENSE)。
