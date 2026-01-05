<template>
  <div class="min-h-screen flex flex-col bg-gradient-to-b from-gray-50 to-gray-100">
    <!-- 美化導航列 -->
    <nav class="bg-white shadow-md py-3 px-4">
      <div class="max-w-7xl mx-auto">
        <div class="flex items-center justify-between">
          <!-- Logo -->
          <div class="flex items-center space-x-3">
            <div class="w-8 h-8 bg-gradient-to-r from-blue-500 to-indigo-600 rounded-lg flex items-center justify-center shadow-md">
              <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
              </svg>
            </div>
            <router-link to="/" class="text-xl font-bold text-gray-800">
              學生管理系統
            </router-link>
          </div>
          
          <!-- 導航連結 -->
          <div class="hidden sm:flex items-center space-x-1">
            <router-link to="/" class="px-4 py-2 text-sm text-gray-600 hover:text-blue-600 hover:bg-blue-50 rounded-lg transition-colors">
              <span class="flex items-center">
                <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
                </svg>
                首頁
              </span>
            </router-link>
            <router-link to="/students" class="px-4 py-2 text-sm text-gray-600 hover:text-blue-600 hover:bg-blue-50 rounded-lg transition-colors">
              <span class="flex items-center">
                <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.67 3.137l-5.52-3.185a1 1 0 00-1.3 0l-5.52 3.185a1 1 0 00-.3.345l-2.5 4.33a1 1 0 00.866 1.5h13.656a1 1 0 00.866-1.5l-2.5-4.33a1 1 0 00-.302-.345z" />
                </svg>
                學生列表
              </span>
            </router-link>
            <router-link to="/students/create" class="px-4 py-2 text-sm text-gray-600 hover:text-blue-600 hover:bg-blue-50 rounded-lg transition-colors">
              <span class="flex items-center">
                <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
                </svg>
                新增
              </span>
            </router-link>
            <router-link to="/about" class="px-4 py-2 text-sm text-gray-600 hover:text-blue-600 hover:bg-blue-50 rounded-lg transition-colors">
              <span class="flex items-center">
                <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                關於
              </span>
            </router-link>
          </div>
          
          <!-- 行動選單按鈕 -->
          <button class="sm:hidden p-2 rounded-lg hover:bg-gray-100" @click="toggleMenu">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
            </svg>
          </button>
        </div>
        
        <!-- 行動選單 -->
        <div v-if="menuOpen" class="sm:hidden mt-2 pt-2 border-t border-gray-200">
          <div class="flex flex-col space-y-1">
            <router-link to="/" class="py-2 px-3 text-sm text-gray-600 hover:text-blue-600 hover:bg-blue-50 rounded-lg flex items-center" @click="menuOpen = false">
              <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
              </svg>
              首頁
            </router-link>
            <router-link to="/students" class="py-2 px-3 text-sm text-gray-600 hover:text-blue-600 hover:bg-blue-50 rounded-lg flex items-center" @click="menuOpen = false">
              <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.67 3.137l-5.52-3.185a1 1 0 00-1.3 0l-5.52 3.185a1 1 0 00-.3.345l-2.5 4.33a1 1 0 00.866 1.5h13.656a1 1 0 00.866-1.5l-2.5-4.33a1 1 0 00-.302-.345z" />
              </svg>
              學生列表
            </router-link>
            <router-link to="/students/create" class="py-2 px-3 text-sm text-gray-600 hover:text-blue-600 hover:bg-blue-50 rounded-lg flex items-center" @click="menuOpen = false">
              <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
              </svg>
              新增
            </router-link>
            <router-link to="/about" class="py-2 px-3 text-sm text-gray-600 hover:text-blue-600 hover:bg-blue-50 rounded-lg flex items-center" @click="menuOpen = false">
              <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              關於
            </router-link>
          </div>
        </div>
      </div>
    </nav>
    
    <!-- 主要內容 -->
    <main class="flex-1 p-4 md:p-6">
      <router-view />
    </main>
    
    <!-- 美化頁尾 -->
    <footer class="bg-gradient-to-r from-gray-800 to-gray-900 text-white py-6 px-4">
      <div class="max-w-7xl mx-auto text-center">
        <p class="text-sm">學生管理系統 © {{ new Date().getFullYear() }}</p>
        <p class="text-xs text-gray-400 mt-1">現代化學生資料管理平台</p>
      </div>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const menuOpen = ref(false)

const toggleMenu = () => {
  menuOpen.value = !menuOpen.value
}
</script>