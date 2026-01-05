## 執行步驟總結

1. **設置後端** ：

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><code class="language-bash">cd backend
   # 修改 .env 檔案設定 MySQL 連接
   python init_db.py  # 初始化資料庫
   python run.py      # 啟動後端服務</code></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

1. **設置前端** ：

<pre class="ybc-pre-component ybc-pre-component_not-math"><div class="hyc-common-markdown__code"><div class="hyc-common-markdown__code__hd"></div><pre class="hyc-common-markdown__code-lan"><div class="hyc-code-scrollbar"><div class="hyc-code-scrollbar__view"><code class="language-bash">cd frontend
   npm install        # 安裝依賴
   npm run dev        # 啟動前端開發伺服器</code></div><div class="hyc-code-scrollbar__track"><div class="hyc-code-scrollbar__thumb"></div></div><div><div></div></div></div></pre></div></pre>

1. **訪問系統** ：

* 前端：**http://localhost:5173**
* 後端 API：**http://localhost:8000**
* API 文件：**http://localhost:8000/docs**

現在您有了完整的 Vue 3 前端應用程式，包含導航列、頁面切換和完整的學生資料管理功能！

**AI搜尋**

**AI閱讀**

**AI寫作**

**AI畫圖**

# frontend

This template should help get you started developing with Vue 3 in Vite.

## Recommended IDE Setup

[VS Code](https://code.visualstudio.com/) + [Vue (Official)](https://marketplace.visualstudio.com/items?itemName=Vue.volar) (and disable Vetur).

## Recommended Browser Setup

- Chromium-based browsers (Chrome, Edge, Brave, etc.):
  - [Vue.js devtools](https://chromewebstore.google.com/detail/vuejs-devtools/nhdogjmejiglipccpnnnanhbledajbpd)
  - [Turn on Custom Object Formatter in Chrome DevTools](http://bit.ly/object-formatters)
- Firefox:
  - [Vue.js devtools](https://addons.mozilla.org/en-US/firefox/addon/vue-js-devtools/)
  - [Turn on Custom Object Formatter in Firefox DevTools](https://fxdx.dev/firefox-devtools-custom-object-formatters/)

## Customize configuration

See [Vite Configuration Reference](https://vite.dev/config/).

## Project Setup

```sh
npm install
```

### Compile and Hot-Reload for Development

```sh
npm run dev
```

### Compile and Minify for Production

```sh
npm run build
```
