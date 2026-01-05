<template>
  <div class="min-h-full">
    <!-- 歡迎區 -->
    <div class="text-center mb-12">
      <h1 class="text-4xl font-bold text-gray-800 mb-4">學生資料管理系統</h1>
      <p class="text-lg text-gray-600 max-w-2xl mx-auto">高效管理學生資料，提供完整的學生資訊新增、編輯、搜尋和刪除功能，讓您輕鬆管理學生資訊</p>
    </div>
    
    <!-- 功能卡片 -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-12">
      <div class="bg-white rounded-xl shadow-lg p-8 hover:shadow-xl transition-shadow duration-300 border border-gray-100">
        <div class="w-16 h-16 bg-blue-100 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-8 h-8 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4.354a4 4 0 110 5.292M15 21H3v-1a6 6 0 0112 0v1zm0 0h6v-1a6 6 0 00-9-5.197m13.67 3.137l-5.52-3.185a1 1 0 00-1.3 0l-5.52 3.185a1 1 0 00-.3.345l-2.5 4.33a1 1 0 00.866 1.5h13.656a1 1 0 00.866-1.5l-2.5-4.33a1 1 0 00-.302-.345z" />
          </svg>
        </div>
        <h3 class="text-xl font-semibold text-center text-gray-800 mb-3">學生管理</h3>
        <p class="text-gray-600 text-center mb-6">輕鬆管理所有學生資料，支援編輯、刪除和查看詳細資訊</p>
        <router-link to="/students" class="block w-full text-center py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white rounded-lg hover:from-blue-600 hover:to-blue-700 transition-all duration-300 shadow-md hover:shadow-lg">
          開始使用
        </router-link>
      </div>
      
      <div class="bg-white rounded-xl shadow-lg p-8 hover:shadow-xl transition-shadow duration-300 border border-gray-100">
        <div class="w-16 h-16 bg-green-100 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-8 h-8 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
          </svg>
        </div>
        <h3 class="text-xl font-semibold text-center text-gray-800 mb-3">智慧搜尋</h3>
        <p class="text-gray-600 text-center mb-6">快速搜尋和篩選學生資料，支援多條件篩選功能</p>
        <router-link to="/students" class="block w-full text-center py-3 bg-gradient-to-r from-green-500 to-green-600 text-white rounded-lg hover:from-green-600 hover:to-green-700 transition-all duration-300 shadow-md hover:shadow-lg">
          搜尋學生
        </router-link>
      </div>
      
      <div class="bg-white rounded-xl shadow-lg p-8 hover:shadow-xl transition-shadow duration-300 border border-gray-100">
        <div class="w-16 h-16 bg-purple-100 rounded-full flex items-center justify-center mx-auto mb-6">
          <svg class="w-8 h-8 text-purple-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
          </svg>
        </div>
        <h3 class="text-xl font-semibold text-center text-gray-800 mb-3">新增資料</h3>
        <p class="text-gray-600 text-center mb-6">快速新增學生資料，支援完整的資料驗證機制</p>
        <router-link to="/students/create" class="block w-full text-center py-3 bg-gradient-to-r from-purple-500 to-purple-600 text-white rounded-lg hover:from-purple-600 hover:to-purple-700 transition-all duration-300 shadow-md hover:shadow-lg">
          新增學生
        </router-link>
      </div>
    </div>
    
    <!-- 快速連結 -->
    <div class="flex flex-wrap justify-center gap-4">
      <router-link to="/students/create" class="px-8 py-4 bg-gradient-to-r from-blue-500 to-indigo-600 text-white rounded-xl hover:from-blue-600 hover:to-indigo-700 transition-all duration-300 shadow-lg hover:shadow-xl text-lg font-medium">
        <span class="flex items-center">
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
          </svg>
          新增學生
        </span>
      </router-link>
      <router-link to="/students" class="px-8 py-4 bg-gradient-to-r from-gray-600 to-gray-700 text-white rounded-xl hover:from-gray-700 hover:to-gray-800 transition-all duration-300 shadow-lg hover:shadow-xl text-lg font-medium">
        <span class="flex items-center">
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h8a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
          </svg>
          瀏覽列表
        </span>
      </router-link>
    </div>
  </div>
</template>

<script setup>
// 極簡首頁
</script>