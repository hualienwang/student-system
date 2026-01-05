<template>
  <div class="max-w-7xl mx-auto">
    <!-- 標題和搜尋 -->
    <div class="mb-8">
      <div class="flex flex-col md:flex-row md:items-center md:justify-between mb-6 gap-4">
        <div>
          <h1 class="text-3xl font-bold text-gray-800">學生列表</h1>
          <p class="text-gray-600 mt-1">管理所有學生資料</p>
        </div>
        <router-link to="/students/create" class="px-6 py-3 bg-gradient-to-r from-blue-500 to-indigo-600 text-white rounded-lg hover:from-blue-600 hover:to-indigo-700 transition-all duration-300 shadow-md hover:shadow-lg flex items-center justify-center">
          <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
          </svg>
          新增學生
        </router-link>
      </div>
      
      <!-- 搜尋欄 -->
      <div class="bg-white rounded-xl shadow-lg p-6 border border-gray-100">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">搜尋</label>
            <div class="relative">
              <input
                v-model="searchKeyword"
                @input="handleSearch"
                type="text"
                placeholder="搜尋姓名、郵箱或國家..."
                class="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
              />
              <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" />
                </svg>
              </div>
            </div>
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">性別</label>
            <select
              v-model="genderFilter"
              @change="filterStudents"
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
            >
              <option value="">全部性別</option>
              <option value="男">男</option>
              <option value="女">女</option>
              <option value="其他">其他</option>
            </select>
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-2">國家</label>
            <input
              v-model="countryFilter"
              @input="filterStudents"
              type="text"
              placeholder="輸入國家..."
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition-colors"
            />
          </div>
          <div class="flex items-end">
            <button @click="clearFilters" class="w-full px-4 py-3 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition-colors">
              清除篩選
            </button>
          </div>
        </div>
      </div>
    </div>
    
    <!-- 錯誤訊息 -->
    <div v-if="store.error" class="mb-4 p-4 bg-red-50 border border-red-200 text-red-700 rounded-lg">
      <div class="flex items-center">
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        {{ store.error }}
      </div>
    </div>
    
    <!-- 載入中 -->
    <div v-if="store.loading" class="flex flex-col items-center justify-center py-16">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mb-4"></div>
      <p class="text-gray-600">載入學生資料中...</p>
    </div>
    
    <!-- 表格 -->
    <div v-else class="bg-white rounded-xl shadow-lg overflow-hidden border border-gray-100">
      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">ID</th>
              <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">姓名</th>
              <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">性別</th>
              <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">國家</th>
              <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">郵箱</th>
              <th class="px-6 py-4 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">操作</th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="student in filteredStudents" :key="student.id" class="hover:bg-gray-50 transition-colors">
              <td class="px-6 py-4 whitespace-nowrap text-sm font-mono text-gray-900">{{ student.id }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ student.name }}</td>
              <td class="px-6 py-4 whitespace-nowrap">
                <span class="px-3 py-1 inline-flex text-xs leading-5 font-semibold rounded-full" 
                  :class="student.gender === '男' ? 'bg-blue-100 text-blue-800' : 
                         student.gender === '女' ? 'bg-pink-100 text-pink-800' : 
                         'bg-purple-100 text-purple-800'">
                  {{ student.gender }}
                </span>
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ student.country }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-blue-600">{{ student.email }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-right text-sm font-medium">
                <div class="flex justify-end space-x-2">
                  <button @click="editStudent(student.id)" class="p-2 text-blue-600 hover:text-blue-900 hover:bg-blue-50 rounded-lg transition-colors">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                    </svg>
                  </button>
                  <button @click="confirmDelete(student)" class="p-2 text-red-600 hover:text-red-900 hover:bg-red-50 rounded-lg transition-colors">
                    <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                    </svg>
                  </button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      
      <!-- 無資料 -->
      <div v-if="filteredStudents.length === 0" class="text-center py-16">
        <svg class="mx-auto h-16 w-16 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <h3 class="mt-4 text-lg font-medium text-gray-900">沒有學生資料</h3>
        <p class="mt-2 text-gray-600">目前沒有任何學生資料，點擊下方按鈕新增第一筆資料。</p>
        <div class="mt-6">
          <router-link to="/students/create" class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-500 to-indigo-600 text-white rounded-lg hover:from-blue-600 hover:to-indigo-700 transition-all duration-300 shadow-md hover:shadow-lg">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 0v6m0-6h6m-6 0H6" />
            </svg>
            新增學生
          </router-link>
        </div>
      </div>
      
      <!-- 分頁 -->
      <div v-if="filteredStudents.length > 0" class="bg-gray-50 px-6 py-4 border-t border-gray-200">
        <div class="flex items-center justify-between">
          <div class="text-sm text-gray-700">
            顯示第 <span class="font-medium">{{ (currentPage - 1) * pageSize + 1 }}</span> 到 
            <span class="font-medium">{{ Math.min(currentPage * pageSize, store.students.length) }}</span> 筆，
            共 <span class="font-medium">{{ store.students.length }}</span> 筆
          </div>
          <div class="flex space-x-2">
            <button @click="prevPage" :disabled="currentPage === 1" 
              :class="currentPage === 1 ? 'bg-gray-100 text-gray-400 cursor-not-allowed' : 'bg-white text-gray-700 hover:bg-gray-50'"
              class="px-4 py-2 border border-gray-300 rounded-lg transition-colors">
              上一頁
            </button>
            <span class="px-4 py-2 text-gray-700 bg-white border border-gray-300 rounded-lg">
              {{ currentPage }}
            </span>
            <button @click="nextPage" :disabled="currentPage * pageSize >= store.students.length" 
              :class="currentPage * pageSize >= store.students.length ? 'bg-gray-100 text-gray-400 cursor-not-allowed' : 'bg-white text-gray-700 hover:bg-gray-50'"
              class="px-4 py-2 border border-gray-300 rounded-lg transition-colors">
              下一頁
            </button>
          </div>
        </div>
      </div>
    </div>
    
    <!-- 刪除確認 -->
    <div v-if="showDeleteModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
      <div class="bg-white rounded-xl shadow-xl p-6 max-w-md w-full border border-gray-200">
        <div class="flex items-center mb-4">
          <div class="w-10 h-10 bg-red-100 rounded-full flex items-center justify-center mr-3">
            <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.732 16.5c-.77.833.192 2.5 1.732 2.5z" />
            </svg>
          </div>
          <h3 class="text-lg font-semibold text-gray-900">確認刪除</h3>
        </div>
        <p class="text-gray-600 mb-6">確定要刪除學生 <span class="font-semibold text-gray-800">{{ studentToDelete?.name }}</span> 的資料嗎？此操作無法復原。</p>
        <div class="flex justify-end space-x-3">
          <button @click="showDeleteModal = false" class="px-4 py-2 bg-gray-200 text-gray-700 rounded-lg hover:bg-gray-300 transition-colors">
            取消
          </button>
          <button @click="deleteStudent" class="px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors">
            確認刪除
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useStudentStore } from '../store/student'

const router = useRouter()
const store = useStudentStore()

const searchKeyword = ref('')
const genderFilter = ref('')
const countryFilter = ref('')
const currentPage = ref(1)
const pageSize = 10
const showDeleteModal = ref(false)
const studentToDelete = ref(null)

const filteredStudents = computed(() => {
  let result = store.students
  
  if (searchKeyword.value) {
    const keyword = searchKeyword.value.toLowerCase()
    result = result.filter(s => 
      s.name.toLowerCase().includes(keyword) ||
      s.email.toLowerCase().includes(keyword) ||
      s.country.toLowerCase().includes(keyword)
    )
  }
  
  if (genderFilter.value) result = result.filter(s => s.gender === genderFilter.value)
  if (countryFilter.value) result = result.filter(s => s.country.includes(countryFilter.value))
  
  const start = (currentPage.value - 1) * pageSize
  return result.slice(start, start + pageSize)
})

onMounted(() => store.fetchStudents())

const handleSearch = () => currentPage.value = 1
const filterStudents = () => currentPage.value = 1
const clearFilters = () => {
  searchKeyword.value = ''
  genderFilter.value = ''
  countryFilter.value = ''
  currentPage.value = 1
}
const editStudent = (id) => router.push(`/students/${id}/edit`)
const confirmDelete = (student) => {
  studentToDelete.value = student
  showDeleteModal.value = true
}
const deleteStudent = async () => {
  if (studentToDelete.value) {
    await store.deleteStudent(studentToDelete.value.id)
    showDeleteModal.value = false
    studentToDelete.value = null
  }
}
const nextPage = () => { if (filteredStudents.value.length === pageSize) currentPage.value++ }
const prevPage = () => { if (currentPage.value > 1) currentPage.value-- }
</script>