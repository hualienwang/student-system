# 第一階段：構建階
FROM node:20-alpine as build

# 設置工作目錄
WORKDIR /app

# 複製 package 文件
COPY frontend/package*.json ./

# 安裝依賴（使用 npm ci 以獲得可重複的安裝）
RUN npm ci

# 設定環境變數以配置 API URL
ARG API_BASE_URL=https://student-system-1-q7r4.onrender.com
ENV VITE_API_BASE_URL=$API_BASE_URL

# 複製源代碼
COPY frontend/ .

# 構建應用
RUN npm run build

# 第二階段：運行階段
FROM nginx:alpine

# 複製構建結果到 nginx 目錄
COPY --from=build /app/dist /etc/nginx/html

# 複製 nginx 配置
COPY frontend/nginx.conf /etc/nginx/conf.d/default.conf

# 暴露端口
EXPOSE 80

# 運行 nginx
CMD ["nginx", "-g", "daemon off;"]