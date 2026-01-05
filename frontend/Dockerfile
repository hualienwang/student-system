# 第一階段：構建階段
FROM node:18-alpine as build

# 設置工作目錄
WORKDIR /app

# 複製 package 文件
COPY package*.json ./

# 安裝依賴
RUN npm ci --only=production

# 設定環境變數以配置 API URL
ARG API_BASE_URL=
ENV VITE_API_BASE_URL=$API_BASE_URL

# 複製源代碼
COPY frontend/ .

# 構建應用
RUN npm run build

# 第二階段：運行階段
FROM nginx:alpine

# 複製構建結果到 nginx 目錄
COPY --from=build /app/dist /usr/share/nginx/html

# 複製 nginx 配置
COPY nginx.conf /etc/nginx/conf.d/default.conf

# 暴露端口
EXPOSE 80

# 運行 nginx
CMD ["nginx", "-g", "daemon off;"]