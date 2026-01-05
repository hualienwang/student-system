<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 py-8">
    <div class="container mx-auto px-4 max-w-4xl">
      <!-- 返回按鈕 -->
      <button
        @click="$router.back()"
        class="flex items-center text-gray-700 hover:text-gray-900 mb-8 px-4 py-2 rounded-lg hover:bg-white/50 transition-colors"
      >
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        返回列表
      </button>

      <!-- 標題 -->
      <div class="text-center mb-10">
        <h1 class="text-4xl font-bold text-gray-800 mb-3">新增學生資料</h1>
        <p class="text-gray-600">填寫學生詳細資訊，所有標記 * 的欄位為必填</p>
      </div>

      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <!-- 表單卡片 -->
        <div class="bg-white rounded-2xl shadow-xl p-8 border border-gray-100">
          <!-- 錯誤訊息 -->
          <div v-if="errorMessage" class="mb-6 p-4 bg-red-50 border border-red-200 text-red-700 rounded-xl flex items-start">
            <svg class="w-5 h-5 mr-3 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <div>
              <p class="font-medium">新增失敗</p>
              <p>{{ errorMessage }}</p>
            </div>
          </div>

          <!-- 成功訊息 -->
          <div v-if="successMessage" class="mb-6 p-4 bg-green-50 border border-green-200 text-green-700 rounded-xl flex items-start">
            <svg class="w-5 h-5 mr-3 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <div>
              <p class="font-medium">新增成功</p>
              <p>{{ successMessage }}</p>
            </div>
          </div>

          <!-- 表單 -->
          <form @submit.prevent="submitForm" class="space-y-6">
            <!-- 姓名 -->
            <div>
              <label for="name" class="block text-sm font-medium text-gray-700 mb-2">
                學生姓名 <span class="text-red-500">*</span>
              </label>
              <input
                v-model="form.name"
                type="text"
                id="name"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
                placeholder="請輸入學生姓名"
              />
              <p v-if="errors.name" class="mt-2 text-sm text-red-600 flex items-center">
                <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                {{ errors.name }}
              </p>
            </div>

            <!-- 性別 -->
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-3">
                性別 <span class="text-red-500">*</span>
              </label>
              <div class="grid grid-cols-3 gap-4">
                <label 
                  class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer hover:bg-blue-50 transition-colors"
                  :class="form.gender === '男' ? 'border-blue-500 bg-blue-50' : 'border-gray-300'"
                >
                  <input
                    v-model="form.gender"
                    type="radio"
                    value="男"
                    required
                    class="h-5 w-5 text-blue-600 focus:ring-blue-500"
                  />
                  <span class="text-gray-700 font-medium">男</span>
                </label>
                <label 
                  class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer hover:bg-pink-50 transition-colors"
                  :class="form.gender === '女' ? 'border-pink-500 bg-pink-50' : 'border-gray-300'"
                >
                  <input
                    v-model="form.gender"
                    type="radio"
                    value="女"
                    required
                    class="h-5 w-5 text-pink-600 focus:ring-pink-500"
                  />
                  <span class="text-gray-700 font-medium">女</span>
                </label>
                <label 
                  class="flex items-center space-x-3 p-4 border rounded-lg cursor-pointer hover:bg-purple-50 transition-colors"
                  :class="form.gender === '其他' ? 'border-purple-500 bg-purple-50' : 'border-gray-300'"
                >
                  <input
                    v-model="form.gender"
                    type="radio"
                    value="其他"
                    required
                    class="h-5 w-5 text-purple-600 focus:ring-purple-500"
                  />
                  <span class="text-gray-700 font-medium">其他</span>
                </label>
              </div>
              <p v-if="errors.gender" class="mt-2 text-sm text-red-600 flex items-center">
                <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                {{ errors.gender }}
              </p>
            </div>

            <!-- 國家 -->
            <div>
              <label for="country" class="block text-sm font-medium text-gray-700 mb-2">
                國家/地區 <span class="text-red-500">*</span>
              </label>
              <select
                v-model="form.country"
                id="country"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
              >
                <option value="" disabled>請選擇國家/地區</option>
                <option value="台灣">台灣</option>
                <option value="中國">中國</option>
                <option value="香港">香港</option>
                <option value="澳門">澳門</option>
                <option value="日本">日本</option>
                <option value="韓國">韓國</option>
                <option value="美國">美國</option>
                <option value="英國">英國</option>
                <option value="加拿大">加拿大</option>
                <option value="澳洲">澳洲</option>
                <option value="其他">其他</option>
              </select>
              <p v-if="errors.country" class="mt-2 text-sm text-red-600 flex items-center">
                <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                {{ errors.country }}
              </p>
            </div>

            <!-- 電子郵件 -->
            <div>
              <label for="email" class="block text-sm font-medium text-gray-700 mb-2">
                電子郵件 <span class="text-red-500">*</span>
              </label>
              <input
                v-model="form.email"
                type="email"
                id="email"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
                placeholder="example@email.com"
              />
              <p v-if="errors.email" class="mt-2 text-sm text-red-600 flex items-center">
                <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                {{ errors.email }}
              </p>
            </div>

            <!-- 表單操作按鈕 -->
            <div class="flex justify-end space-x-4 pt-6 border-t border-gray-200">
              <button
                type="button"
                @click="$router.back()"
                class="px-6 py-3 border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors"
              >
                取消
              </button>
              <button
                type="submit"
                :disabled="store.loading"
                :class="{'opacity-50 cursor-not-allowed': store.loading}"
                class="px-6 py-3 bg-gradient-to-r from-blue-500 to-indigo-600 text-white rounded-lg hover:from-blue-600 hover:to-indigo-700 transition-all duration-300 shadow-md hover:shadow-lg flex items-center"
              >
                <svg v-if="store.loading" class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
                </svg>
                {{ store.loading ? '新增中...' : '新增學生' }}
              </button>
            </div>
          </form>
        </div>

        <!-- 表單預覽 -->
        <div class="bg-white rounded-2xl shadow-xl p-8 border border-gray-100">
          <div class="flex items-center mb-6">
            <div class="w-10 h-10 bg-blue-100 rounded-lg flex items-center justify-center mr-3">
              <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <h2 class="text-2xl font-bold text-gray-800">資料預覽</h2>
          </div>
          <div class="space-y-6">
            <div class="p-4 bg-gray-50 rounded-lg">
              <p class="text-sm text-gray-500 mb-1">姓名</p>
              <p class="text-lg font-semibold text-gray-800">{{ form.name || '尚未輸入' }}</p>
            </div>
            <div class="p-4 bg-gray-50 rounded-lg">
              <p class="text-sm text-gray-500 mb-1">性別</p>
              <p class="text-lg font-semibold text-gray-800">{{ form.gender || '尚未選擇' }}</p>
            </div>
            <div class="p-4 bg-gray-50 rounded-lg">
              <p class="text-sm text-gray-500 mb-1">國家/地區</p>
              <p class="text-lg font-semibold text-gray-800">{{ form.country || '尚未選擇' }}</p>
            </div>
            <div class="p-4 bg-gray-50 rounded-lg">
              <p class="text-sm text-gray-500 mb-1">電子郵件</p>
              <p class="text-lg font-semibold text-gray-800">{{ form.email || '尚未輸入' }}</p>
            </div>
          </div>
          <div class="mt-8 p-4 bg-blue-50 border border-blue-200 rounded-lg">
            <div class="flex items-start">
              <svg class="w-5 h-5 text-blue-600 mr-2 mt-0.5 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              <p class="text-sm text-blue-700">確認所有資料無誤後，點擊「新增學生」按鈕完成新增。</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { useRouter } from 'vue-router'
import { useStudentStore } from '../store/student'

const router = useRouter()
const store = useStudentStore()

// 表單資料
const form = reactive({
  name: '',
  gender: '',
  country: '',
  email: ''
})

// 錯誤訊息
const errors = reactive({
  name: '',
  gender: '',
  country: '',
  email: ''
})

// 狀態訊息
const errorMessage = ref('')
const successMessage = ref('')

// 表單驗證
const validateForm = () => {
  let isValid = true

  // 清除之前的錯誤訊息
  Object.keys(errors).forEach(key => errors[key] = '')

  // 驗證姓名
  if (!form.name.trim()) {
    errors.name = '姓名為必填欄位'
    isValid = false
  }

  // 驗證性別
  if (!form.gender) {
    errors.gender = '請選擇性別'
    isValid = false
  }

  // 驗證國家
  if (!form.country) {
    errors.country = '請選擇國家/地區'
    isValid = false
  }

  // 驗證電子郵件
  if (!form.email.trim()) {
    errors.email = '電子郵件為必填欄位'
    isValid = false
  } else if (!/\S+@\S+\.\S+/.test(form.email)) {
    errors.email = '請輸入有效的電子郵件地址'
    isValid = false
  }

  return isValid
}

// 提交表單
const submitForm = async () => {
  if (!validateForm()) {
    return
  }

  errorMessage.value = ''
  successMessage.value = ''

  const result = await store.addStudent(form)

  if (result.success) {
    successMessage.value = '學生資料新增成功！'
    
    // 清空表單
    Object.keys(form).forEach(key => form[key] = '')
    
    // 3秒後返回列表
    setTimeout(() => {
      router.push('/students')
    }, 3000)
  } else {
    errorMessage.value = result.error || '新增失敗，請稍後再試'
  }
}
</script>