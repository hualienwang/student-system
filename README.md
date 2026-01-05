# 學生資料查詢系統

一個完整的學生資料管理系統，採用前後端分離架構，使用現代化的技術棧構建。

## 🚀 功能特色

- **完整 CRUD 功能**：新增、讀取、更新、刪除學生資料
- **智慧搜尋與篩選**：支援多欄位搜尋功能
- **響應式設計**：支援桌面、平板和手機等各種裝置
- **API 版本控制**：使用 `/api/v1/` 路徑進行版本控制
- **安全配置**：CORS 設置、資料驗證等安全措施
- **日誌記錄**：詳細的應用程式日誌記錄
- **分頁支援**：支援學生列表分頁功能

## 🛠 技術棧

### 後端技術

- **FastAPI**：高效能 Python Web 框架
- **SQLModel**：SQL 資料庫 ORM
- **MySQL**：關聯式資料庫
- **Pydantic**：資料驗證
- **Uvicorn**：ASGI 伺服器

### 前端技術

- **Vue 3**：現代化響應式前端框架
- **Vue Router**：前端路由管理
- **Pinia**：狀態管理庫
- **Tailwind CSS**：實用優先的 CSS 框架
- **Axios**：HTTP 客戶端

## 📋 API 端點

### 學生相關端點

- `GET /api/v1/students/` - 取得學生列表（支援分頁）
- `POST /api/v1/students/` - 建立新學生
- `GET /api/v1/students/{id}` - 取得特定學生
- `PUT /api/v1/students/{id}` - 更新學生資料
- `DELETE /api/v1/students/{id}` - 刪除學生
- `GET /api/v1/students/search/?keyword={keyword}` - 搜尋學生

### 系統端點

- `GET /` - 根路徑
- `GET /health` - 健康檢查
- `GET /docs` - API 文件
- `GET /redoc` - API 文件（Redoc）

## 🚀 快速開始

### 環境要求

- Node.js 16+ 與 npm
- Python 3.8+
- MySQL 5.7+ 或 MariaDB 10.3+

### 安裝步驟

#### 1. 克隆專案

```bash
git clone https://github.com/your-repo/student-system.git
cd student-system
```

#### 2. 設置後端

```bash
cd backend
pip install -r requirements.txt
# 或使用 poetry
poetry install

# 初始化數據庫
python init_db.py

# 啟動後端服務
python run.py
# 或使用 uvicorn
uvicorn app.main:app --reload
```

#### 注意：後端先進入虛擬環境 

   先啟動虛擬環境，目前是backend_env

    開啟cmd

#### 3. 設置前端

```bash
cd frontend
npm install

# 啟動前端服務
npm run dev
```

#### 4. 使用 Docker Compose（推薦）

```bash
# 在根目錄下執行
docker-compose up --build
```

## 🏗 項目結構

```
student-system/
├── backend/              # 後端代碼
│   ├── app/              # 應用程式代碼
│   │   ├── main.py       # 主應用程式
│   │   ├── models.py     # 資料模型
│   │   ├── schemas.py    # 資料驗證模型
│   │   ├── crud.py       # 資料庫操作
│   │   └── database.py   # 資料庫配置
│   ├── logs/             # 日誌文件
│   ├── requirements.txt  # Python 依賴
│   ├── pyproject.toml    # Python 項目配置
│   ├── .env             # 環境變數
│   └── Dockerfile       # Docker 配置
├── frontend/             # 前端代碼
│   ├── src/              # 前端源碼
│   ├── public/           # 靜態資源
│   ├── package.json      # Node.js 依賴
│   └── Dockerfile       # Docker 配置
├── docker-compose.yml    # Docker Compose 配置
└── README.md            # 項目說明文件
```

## 🔧 配置說明

### 環境變數

在 `backend/.env` 文件中配置：

```env
# 數據庫配置
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=1234
DB_NAME=student_db

# API 配置
API_VERSION=v1
ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

## 🧪 測試

### 單元測試

```bash
# 後端測試
cd backend
python -m pytest test_api.py

# 前端測試
cd frontend
npm run test
```

## 🚢 部署

### Docker 部署

```bash
# 構建並啟動所有服務
docker-compose up --build -d

# 檢查服務狀態
docker-compose ps

# 查看日誌
docker-compose logs -f
```

## 🔒 安全措施

1. **CORS 配置**：限制允許的來源，避免使用 `allow_origins=["*"]`
2. **資料驗證**：使用 Pydantic 進行請求和響應資料驗證
3. **API 版本控制**：使用 `/api/v1/` 路徑進行版本控制
4. **錯誤處理**：適當的錯誤處理和用戶友好提示
5. **日誌記錄**：詳細的應用程式日誌記錄

## 📊 性能優化

1. **數據庫查詢優化**：使用索引和適當的查詢方式
2. **分頁支援**：支援大量數據的分頁顯示
3. **API 緩存**：可選的 API 響應緩存
4. **前端優化**：組件懶加載和代碼分割

## 📝 日誌記錄

應用程式會在 `backend/logs/` 目錄下生成日誌文件，包含：

- API 請求日誌
- 數據庫操作日誌
- 錯誤和異常日誌
- 應用程式狀態日誌

## 🤝 貢獻

1. Fork 專案
2. 創建功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

## 📄 授權

此專案採用 MIT 授權 - 詳情請見 [LICENSE](LICENSE) 檔案

## 📞 支援

如有問題或建議，請聯繫開發團隊。

---

學生資料查詢系統 &copy; 2023 - 專為學習現代化 Web 開發而設計
