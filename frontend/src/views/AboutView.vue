<template>
  <div class="min-h-full">
    <div class="text-center mb-12">
      <div class="w-24 h-24 bg-gradient-to-r from-blue-500 to-indigo-600 rounded-full flex items-center justify-center mx-auto mb-6 shadow-lg">
        <svg class="w-12 h-12 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
        </svg>
      </div>
      <h1 class="text-4xl font-bold text-gray-800 mb-3">關於學生管理系統</h1>
      <p class="text-lg text-gray-600 max-w-2xl mx-auto">一個現代化、易用的學生資料管理平台，幫助教育機構高效管理學生資訊</p>
    </div>
    
    <div class="grid grid-cols-1 md:grid-cols-2 gap-8 max-w-6xl mx-auto">
      <div class="bg-white rounded-2xl shadow-xl p-8 border border-gray-100">
        <div class="w-12 h-12 bg-blue-100 rounded-lg flex items-center justify-center mb-6">
          <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
          </svg>
        </div>
        <h2 class="text-2xl font-bold text-gray-800 mb-4">系統資訊</h2>
        <div class="space-y-4">
          <div class="flex items-center">
            <div class="w-3 h-3 bg-blue-500 rounded-full mr-3"></div>
            <div>
              <p class="text-gray-500 text-sm">版本</p>
              <p class="font-medium">v2.0.0</p>
            </div>
          </div>
          <div class="flex items-center">
            <div class="w-3 h-3 bg-blue-500 rounded-full mr-3"></div>
            <div>
              <p class="text-gray-500 text-sm">開發團隊</p>
              <p class="font-medium">現代化教育系統開發團隊</p>
            </div>
          </div>
          <div class="flex items-center">
            <div class="w-3 h-3 bg-blue-500 rounded-full mr-3"></div>
            <div>
              <p class="text-gray-500 text-sm">建立日期</p>
              <p class="font-medium">{{ new Date().getFullYear() }} 年</p>
            </div>
          </div>
        </div>
      </div>
      
      <div class="bg-white rounded-2xl shadow-xl p-8 border border-gray-100">
        <div class="w-12 h-12 bg-green-100 rounded-lg flex items-center justify-center mb-6">
          <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
          </svg>
        </div>
        <h2 class="text-2xl font-bold text-gray-800 mb-4">核心功能</h2>
        <ul class="space-y-3">
          <li class="flex items-start">
            <svg class="w-5 h-5 text-green-500 mr-3 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            <span class="text-gray-700">新增學生資料 - 快速建立學生個人檔案</span>
          </li>
          <li class="flex items-start">
            <svg class="w-5 h-5 text-green-500 mr-3 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            <span class="text-gray-700">編輯學生資料 - 靈活修改學生資訊</span>
          </li>
          <li class="flex items-start">
            <svg class="w-5 h-5 text-green-500 mr-3 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            <span class="text-gray-700">刪除學生資料 - 安全移除學生記錄</span>
          </li>
          <li class="flex items-start">
            <svg class="w-5 h-5 text-green-500 mr-3 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            <span class="text-gray-700">搜尋學生資料 - 智慧搜尋與篩選功能</span>
          </li>
          <li class="flex items-start">
            <svg class="w-5 h-5 text-green-500 mr-3 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            <span class="text-gray-700">資料統計 - 提供詳細的資料分析</span>
          </li>
        </ul>
      </div>
    </div>
    
    <div class="max-w-4xl mx-auto mt-12 bg-gradient-to-r from-blue-50 to-indigo-50 rounded-2xl p-8 border border-blue-100">
      <div class="text-center">
        <h2 class="text-2xl font-bold text-gray-800 mb-4">系統特色</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="bg-white p-6 rounded-xl shadow-md">
            <div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center mx-auto mb-4">
              <svg class="w-5 h-5 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <h3 class="font-semibold text-gray-800 mb-2">快速高效</h3>
            <p class="text-sm text-gray-600">優化的系統架構，提供流暢的使用體驗</p>
          </div>
          <div class="bg-white p-6 rounded-xl shadow-md">
            <div class="w-10 h-10 bg-green-100 rounded-lg flex items-center justify-center mx-auto mb-4">
              <svg class="w-5 h-5 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z" />
              </svg>
            </div>
            <h3 class="font-semibold text-gray-800 mb-2">安全可靠</h3>
            <p class="text-sm text-gray-600">多重安全機制，保護學生隱私資料</p>
          </div>
          <div class="bg-white p-6 rounded-xl shadow-md">
            <div class="w-10 h-10 bg-purple-100 rounded-lg flex items-center justify-center mx-auto mb-4">
              <svg class="w-5 h-5 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 21a4 4 0 01-4-4V5a2 2 0 012-2h4a2 2 0 012 2v12a4 4 0 01-4 4zm0 0h12a2 2 0 002-2v-4a2 2 0 00-2-2h-2.343M11 7.343l1.657-1.657a2 2 0 012.828 0l2.829 2.829a2 2 0 010 2.828l-8.486 8.485M7 17h.01" />
              </svg>
            </div>
            <h3 class="font-semibold text-gray-800 mb-2">易於使用</h3>
            <p class="text-sm text-gray-600">直觀的介面設計，簡化操作流程</p>
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