# 使用 Python 官方鏡像作為基礎鏡像
FROM python:3.10-slim

# 設置工作目錄
WORKDIR /app

# 複製依賴文件
COPY backend/requirements.txt .

# 安裝系統依賴和 Python 包
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gcc \
        default-libmysqlclient-dev \
        pkg-config \
        && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 複製應用代碼
COPY . .

# 暴露端口
EXPOSE 8000

# 設置環境變數默認值
ENV PORT=8000

# 運行應用
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}"]