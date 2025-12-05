# Z-Image-JSON-Prompt 🏷️

**一個強大且結構化的 ComfyUI / 節點式 WebUI 提示詞生成器。**

Z-Image-JSON-Prompt 節點旨在解決傳統文字提示詞缺乏組織和難以管理的問題。它將圖像生成的關鍵元素（場景、主體、攝影、燈光、風格）結構化，允許使用者通過清晰的選項列表和預設模板快速生成複雜、高品質的提示詞。

### ✨ 核心功能

* **結構化輸入**：將提示詞分解為五大類 (場景、主體、攝影、燈光、風格) 和十五個子選項，使提示詞的構建邏輯清晰。
* **選項自定義**：節點會自動生成一個名為 `z_image_options` 的目錄，使用者可以輕鬆修改內部的 `.txt` 檔案來**增加或修改提示詞選項**。
* **內建風格模板**：提供十多種預設風格（如賽博朋克、奇幻魔法、電影人像等），可一鍵應用，加速創作流程。
* **多語言輸出**：支援 **中文、英文、雙語** 三種模式輸出，滿足不同模型或使用者需求。
* **多格式輸出**：
    * **`json_prompt`**：輸出包含所有設定的結構化 JSON 資料，方便追溯、存檔或程式化使用。
    * **`positive_text`**：輸出四段式（核心、環境、技術、風格）的純文字提示詞，可直接饋入圖像生成模型。
* **細節等級控制**：可選擇「簡略」、「標準」、「詳細」、「極度詳細」來控制輸出提示詞的豐富度。

### 🚀 安裝與使用

#### 1. 安裝

1.  將 `z_image_json_prompt.py` 檔案放置到您的 ComfyUI 自定義節點目錄下（通常是 `custom_nodes/`）。或在custom_nodes新建一個資料夾(例如`custom_nodes/z_image_json_prompt/`)將z_image_json_prompt.py和__init__.py放入資料夾
2.  重新啟動 ComfyUI。
3.  在節點選單中，您可以在 **`Z-Image`** 類別下找到 **`Z-Image JSON Prompt Generator`** 節點。

#### 2. 第一次運行

當您第一次運行此節點時，它會自動在您的腳本目錄下創建一個名為 **`z_image_options`** 的資料夾，其中包含：

* **五個分類資料夾** (`scene`, `subject`, `photography`, `lighting`, `style`)，每個資料夾內有數個 `.txt` 檔案，用於儲存選項。
* **`templates` 資料夾**，內含預設的 `.json` 模板檔案。

您可以編輯這些 `.txt` 或 `.json` 檔案來擴展您的提示詞庫。

#### 3. 節點輸入參數說明

| 參數名稱 | 類型 | 說明 | 預設值 |
| :--- | :--- | :--- | :--- |
| **`style_template`** | 選擇列表 | 一鍵選擇預設風格模板，將覆蓋對應的選項。 | `無模板 | No Template` |
| **`language_choice`** | 選擇列表 | 決定輸出提示詞的語言（中文/English/雙語）。 | `雙語 | Bilingual` |
| **`detail_level`** | 選擇列表 | 控制輸出提示詞的複雜度及描述詞的豐富度。 | `標準 | Standard` |
| **`negative_prompt`** | 文本輸入 | 負面提示詞，將原樣輸出。 | 預設低品質相關的提示詞。 |
| **`【...】_...`** | 選擇列表 | 各類型的提示詞選項。選擇 **`隨機 | Random`** 將從對應檔案中隨機抽取。 | `隨機 | Random` |

#### 4. 節點輸出

| 輸出名稱 | 類型 | 說明 |
| :--- | :--- | :--- |
| **`json_prompt`** | `STRING` | 完整的結構化 JSON 輸出，包含所有設定和元數據。 |
| **`positive_text`** | `STRING` | 四段式的純文字提示詞，可直接連線到 KSampler 或其他提示詞輸入節點。 |
| **`negative_prompt`** | `STRING` | 負面提示詞文本。 |

### 🤝 貢獻

歡迎提交 Pull Request 或 Issues 來改進本專案。請遵循以下步驟：
1.  Fork 本儲存庫。
2.  建立新的功能分支 (`git checkout -b feature/AmazingFeature`)。
3.  提交您的變更 (`git commit -m 'Add some AmazingFeature'`)。
4.  推送到分支 (`git push origin feature/AmazingFeature`)。
5.  開啟一個 Pull Request。

### 📝 授權許可

本專案採用 [MIT 授權許可](LICENSE) - 詳情請參閱 `LICENSE` 檔案。
