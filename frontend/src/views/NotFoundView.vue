<template>
  <div class="min-h-screen bg-gradient-to-br from-indigo-50 via-white to-blue-50 flex items-center justify-center py-12">
    <div class="container mx-auto px-4">
      <div class="max-w-lg mx-auto text-center">
        <!-- 圖示 -->
        <div class="mb-10">
          <div class="w-32 h-32 bg-gradient-to-r from-blue-100 to-indigo-100 rounded-full flex items-center justify-center mx-auto shadow-lg">
            <svg class="w-16 h-16 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
          </div>
        </div>

        <!-- 錯誤訊息 -->
        <h1 class="text-8xl font-bold text-gray-800 mb-6 tracking-tight">404</h1>
        <h2 class="text-3xl font-bold text-gray-800 mb-6">頁面未找到</h2>
        
        <p class="text-gray-600 text-lg mb-10 max-w-md mx-auto">
          抱歉，您要訪問的頁面不存在或已被移除。
          請檢查網址是否正確，或返回首頁繼續瀏覽。
        </p>

        <!-- 操作按鈕 -->
        <div class="flex flex-col sm:flex-row gap-4 justify-center mb-12">
          <button
            @click="$router.back()"
            class="px-8 py-4 border border-gray-300 rounded-xl text-gray-700 hover:bg-gray-50 transition-colors font-medium shadow-sm hover:shadow-md"
          >
            <svg class="w-5 h-5 mr-2 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
            </svg>
            返回上一頁
          </button>
          <router-link
            to="/"
            class="px-8 py-4 bg-gradient-to-r from-blue-500 to-indigo-600 text-white rounded-xl hover:from-blue-600 hover:to-indigo-700 transition-all duration-300 shadow-lg hover:shadow-xl inline-flex items-center justify-center font-medium"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
            </svg>
            返回首頁
          </router-link>
        </div>

        <!-- 快速連結 -->
        <div class="bg-white rounded-2xl p-8 shadow-lg border border-gray-100">
          <p class="text-gray-700 font-medium mb-6">您可能對以下功能感興趣：</p>
          <div class="grid grid-cols-1 sm:grid-cols-3 gap-4">
            <router-link to="/students" class="flex flex-col items-center p-4 rounded-xl bg-gray-50 hover:bg-blue-50 transition-colors border border-gray-200 hover:border-blue-300 group">
              <div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center mb-3 group-hover:bg-blue-200 transition-colors">
                <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.67 3.137l-5.52-3.185a1 1 0 00-1.3 0l-5.52 3.185a1 1 0 00-.3.345l-2.5 4.33a1 1 0 00.866 1.5h13.656a1 1 0 00.866-1.5l-2.5-4.33a1 1 0 00-.302-.345z" />
                </svg>
              </div>
              <span class="text-gray-700 font-medium group-hover:text-blue-700">學生列表</span>
            </router-link>
            <router-link to="/students/create" class="flex flex-col items-center p-4 rounded-xl bg-gray-50 hover:bg-green-50 transition-colors border border-gray-200 hover:border-green-300 group">
              <div class="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center mb-3 group-hover:bg-green-200 transition-colors">
                <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
              </div>
              <span class="text-gray-700 font-medium group-hover:text-green-700">新增學生</span>
            </router-link>
            <router-link to="/about" class="flex flex-col items-center p-4 rounded-xl bg-gray-50 hover:bg-purple-50 transition-colors border border-gray-200 hover:border-purple-300 group">
              <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center mb-3 group-hover:bg-purple-200 transition-colors">
                <svg class="w-6 h-6 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
              </div>
              <span class="text-gray-700 font-medium group-hover:text-purple-700">關於系統</span>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()
</script>