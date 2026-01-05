import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

// 強制添加全局樣式
const style = document.createElement('style')
style.textContent = `
  /* 強制限制所有 SVG 尺寸 */
  svg {
    max-width: 24px !important;
    max-height: 24px !important;
    width: auto !important;
    height: auto !important;
  }
  
  /* 強制限制按鈕中的圖標 */
  button svg {
    max-width: 16px !important;
    max-height: 16px !important;
  }
  
  /* 強制限制導航中的圖標 */
  nav svg {
    max-width: 16px !important;
    max-height: 16px !important;
  }
  
  /* 移除所有可能導致圖標變大的樣式 */
  * {
    box-sizing: border-box;
  }
`
document.head.appendChild(style)

// 創建應用
const app = createApp(App)
app.use(createPinia())
app.use(router)
app.mount('#app')