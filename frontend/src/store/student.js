import { defineStore } from 'pinia'
import { ref } from 'vue'
import axios from 'axios'

// 建立 Axios 實例
const apiClient = axios.create({
  baseURL: `${import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'}`,
  timeout: 10000,
  headers: {
    'Content-Type': 'application/json',
  }
})

export const useStudentStore = defineStore('student', () => {
  const students = ref([])
  const loading = ref(false)
  const error = ref(null)
  const currentStudent = ref(null)

  // 取得所有學生
  const fetchStudents = async () => {
    loading.value = true
    error.value = null
    try {
      const response = await apiClient.get('/students/')
      students.value = response.data
    } catch (err) {
      error.value = err.response?.data?.detail || '取得學生資料失敗'
      console.error('Error fetching students:', err)
    } finally {
      loading.value = false
    }
  }

  // 取得單一學生
  const fetchStudent = async (id) => {
    loading.value = true
    error.value = null
    try {
      const response = await apiClient.get(`/students/${id}`)
      currentStudent.value = response.data
    } catch (err) {
      error.value = err.response?.data?.detail || '取得學生資料失敗'
      console.error('Error fetching student:', err)
    } finally {
      loading.value = false
    }
  }

  // 新增學生
  const addStudent = async (studentData) => {
    loading.value = true
    error.value = null
    try {
      const response = await apiClient.post('/students/', studentData)
      students.value.push(response.data)
      return { success: true, data: response.data }
    } catch (err) {
      error.value = err.response?.data?.detail || '新增學生失敗'
      console.error('Error adding student:', err)
      return { success: false, error: error.value }
    } finally {
      loading.value = false
    }
  }

  // 更新學生
  const updateStudent = async (id, studentData) => {
    loading.value = true
    error.value = null
    try {
      const response = await apiClient.put(`/students/${id}`, studentData)
      const index = students.value.findIndex(s => s.id === id)
      if (index !== -1) {
        students.value[index] = response.data
      }
      return { success: true, data: response.data }
    } catch (err) {
      error.value = err.response?.data?.detail || '更新學生失敗'
      console.error('Error updating student:', err)
      return { success: false, error: error.value }
    } finally {
      loading.value = false
    }
  }

  // 刪除學生
  const deleteStudent = async (id) => {
    loading.value = true
    error.value = null
    try {
      await apiClient.delete(`/students/${id}`)
      students.value = students.value.filter(s => s.id !== id)
      return { success: true }
    } catch (err) {
      error.value = err.response?.data?.detail || '刪除學生失敗'
      console.error('Error deleting student:', err)
      return { success: false, error: error.value }
    } finally {
      loading.value = false
    }
  }

  // 搜尋學生
  const searchStudents = async (keyword) => {
    loading.value = true
    error.value = null
    try {
      const response = await apiClient.get(`/students/search/?keyword=${keyword}`)
      return { success: true, data: response.data }
    } catch (err) {
      error.value = err.response?.data?.detail || '搜尋失敗'
      console.error('Error searching students:', err)
      return { success: false, error: error.value }
    } finally {
      loading.value = false
    }
  }

  return {
    students,
    loading,
    error,
    currentStudent,
    fetchStudents,
    fetchStudent,
    addStudent,
    updateStudent,
    deleteStudent,
    searchStudents
  }
})