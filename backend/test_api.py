"""
API 測試文件
用於測試學生管理系統的 API 端點
"""
import pytest
import requests
from fastapi.testclient import TestClient
from app.main import app
from app.database import create_db_and_tables
from app.models import Student

client = TestClient(app)

def test_root_endpoint():
    """測試根路徑端點"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "學生資料查詢系統 API"
    assert data["status"] == "running"

def test_health_check():
    """測試健康檢查端點"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"

def test_create_student():
    """測試創建學生"""
    student_data = {
        "name": "測試學生",
        "gender": "男",
        "country": "台灣",
        "email": "test@example.com"
    }
    response = client.post("/api/v1/students/", json=student_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "測試學生"
    assert data["email"] == "test@example.com"
    student_id = data["id"]
    
    # 清理測試數據
    client.delete(f"/api/v1/students/{student_id}")

def test_get_students():
    """測試取得學生列表"""
    response = client.get("/api/v1/students/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_get_student_by_id():
    """測試取得特定學生"""
    # 首先創建一個學生
    student_data = {
        "name": "測試學生2",
        "gender": "女",
        "country": "台灣",
        "email": "test2@example.com"
    }
    create_response = client.post("/api/v1/students/", json=student_data)
    assert create_response.status_code == 200
    created_student = create_response.json()
    student_id = created_student["id"]
    
    # 獲取該學生
    response = client.get(f"/api/v1/students/{student_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "測試學生2"
    
    # 清理測試數據
    client.delete(f"/api/v1/students/{student_id}")

def test_update_student():
    """測試更新學生"""
    # 首先創建一個學生
    student_data = {
        "name": "原學生",
        "gender": "男",
        "country": "台灣",
        "email": "original@example.com"
    }
    create_response = client.post("/api/v1/students/", json=student_data)
    assert create_response.status_code == 200
    created_student = create_response.json()
    student_id = created_student["id"]
    
    # 更新學生資料
    update_data = {
        "name": "更新學生",
        "email": "updated@example.com"
    }
    response = client.put(f"/api/v1/students/{student_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "更新學生"
    assert data["email"] == "updated@example.com"
    
    # 清理測試數據
    client.delete(f"/api/v1/students/{student_id}")

def test_delete_student():
    """測試刪除學生"""
    # 首先創建一個學生
    student_data = {
        "name": "待刪除學生",
        "gender": "女",
        "country": "台灣",
        "email": "todelete@example.com"
    }
    create_response = client.post("/api/v1/students/", json=student_data)
    assert create_response.status_code == 200
    created_student = create_response.json()
    student_id = created_student["id"]
    
    # 刪除學生
    response = client.delete(f"/api/v1/students/{student_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    
    # 驗證學生確實被刪除
    get_response = client.get(f"/api/v1/students/{student_id}")
    assert get_response.status_code == 404

def test_search_students():
    """測試搜尋學生"""
    # 首先創建一個學生
    student_data = {
        "name": "搜尋測試學生",
        "gender": "男",
        "country": "台灣",
        "email": "search@example.com"
    }
    create_response = client.post("/api/v1/students/", json=student_data)
    assert create_response.status_code == 200
    created_student = create_response.json()
    student_id = created_student["id"]
    
    # 搜尋學生
    response = client.get("/api/v1/students/search/", params={"keyword": "搜尋測試"})
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) >= 1
    
    # 清理測試數據
    client.delete(f"/api/v1/students/{student_id}")

if __name__ == "__main__":
    # 在運行測試前先初始化數據庫
    create_db_and_tables()
    
    # 運行所有測試
    pytest.main([__file__])