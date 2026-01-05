from fastapi import FastAPI, Depends, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Session
from typing import List, Optional
import uvicorn
import os
from dotenv import load_dotenv
import logging

# 加載環境變數
load_dotenv()

# 導入日誌配置
from app.logging_config import app_logger, api_logger

from .database import create_db_and_tables, get_session
from .models import Student
from .schemas import StudentCreate, StudentUpdate, StudentResponse
from .crud import (
    create_student, get_student, get_students, 
    update_student, delete_student, search_students
)

# 從環境變數獲取允許的來源
allowed_origins = os.getenv("ALLOWED_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173,https://student-system-frontend.onrender.com,https://student-system-backend.onrender.com").split(",")

# 建立 FastAPI 應用程式
app = FastAPI(
    title="學生資料查詢系統 API",
    description="學生資料管理系統後端 API",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 設置 CORS - 改進安全性
app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["*"],
    # 添加額外的安全選項
    allow_origin_regex=None,
    expose_headers=["Access-Control-Allow-Origin"]
)

@app.on_event("startup")
def on_startup():
    """應用程式啟動時建立資料庫表格"""
    try:
        create_db_and_tables()
        app_logger.info("資料庫初始化完成")
        print("✅ 資料庫初始化完成")
    except Exception as e:
        app_logger.error(f"資料庫初始化失敗: {e}")
        print(f"❌ 資料庫初始化失敗: {e}")
        print("⚠️ 系統將繼續運行，但資料庫功能可能不可用")
        print("請檢查 MySQL 連接設置")

@app.get("/")
def read_root():
    """根路徑"""
    api_logger.info("根路徑被訪問")
    return {
        "message": "學生資料查詢系統 API",
        "status": "running",
        "version": "1.0.0",
        "docs": "http://localhost:8000/docs",
        "endpoints": {
            "health": "/health",
            "students": "/students",
            "student_detail": "/students/{id}"
        }
    }

@app.get("/health")
def health_check(session: Session = Depends(get_session)):
    """健康檢查端點"""
    api_logger.info("健康檢查端點被訪問")
    try:
        # 嘗試執行一個簡單的查詢來測試數據庫連接
        session.execute("SELECT 1")
        db_status = "connected"
    except Exception as e:
        api_logger.error(f"數據庫連接檢查失敗: {e}")
        db_status = "disconnected"
    
    return {"status": "healthy", "database": db_status}

# API 版本控制 - 學生相關端點
@app.post("/students/", response_model=StudentResponse)
def create_new_student(student: StudentCreate, session: Session = Depends(get_session)):
    """建立新學生"""
    api_logger.info(f"創建新學生: {student.name}")
    try:
        result = create_student(session, student)
        api_logger.info(f"成功創建學生: {result.id}")
        return result
    except Exception as e:
        api_logger.error(f"創建學生失敗: {str(e)}")
        raise HTTPException(status_code=400, detail=f"創建學生失敗: {str(e)}")

@app.get("/students/", response_model=List[StudentResponse])
def read_students(
    skip: int = Query(0, ge=0, description="跳過的記錄數"),
    limit: int = Query(100, ge=1, le=1000, description="返回的記錄數"),
    session: Session = Depends(get_session)
):
    """取得學生列表（支持分頁）"""
    api_logger.info(f"取得學生列表 - 跳過: {skip}, 限制: {limit}")
    students = get_students(session, skip=skip, limit=limit)
    return students

@app.get("/students/{student_id}", response_model=StudentResponse)
def read_student(student_id: int, session: Session = Depends(get_session)):
    """取得單一學生資料"""
    api_logger.info(f"取得學生資料: {student_id}")
    student = get_student(session, student_id)
    if not student:
        api_logger.warning(f"嘗試訪問不存在的學生: {student_id}")
        raise HTTPException(status_code=404, detail="學生不存在")
    return student

@app.put("/students/{student_id}", response_model=StudentResponse)
def update_existing_student(
    student_id: int, 
    student: StudentUpdate, 
    session: Session = Depends(get_session)
):
    """更新學生資料"""
    api_logger.info(f"更新學生資料: {student_id}")
    updated_student = update_student(session, student_id, student)
    if not updated_student:
        api_logger.warning(f"嘗試更新不存在的學生: {student_id}")
        raise HTTPException(status_code=404, detail="學生不存在")
    api_logger.info(f"成功更新學生: {student_id}")
    return updated_student

@app.delete("/students/{student_id}")
def delete_existing_student(student_id: int, session: Session = Depends(get_session)):
    """刪除學生資料"""
    api_logger.info(f"刪除學生資料: {student_id}")
    success = delete_student(session, student_id)
    if not success:
        api_logger.warning(f"嘗試刪除不存在的學生: {student_id}")
        raise HTTPException(status_code=404, detail="學生不存在")
    api_logger.info(f"成功刪除學生: {student_id}")
    return {"message": "學生已成功刪除", "success": True}

@app.get("/students/search/", response_model=List[StudentResponse])
def search_students_endpoint(
    keyword: str = Query(..., min_length=1, description="搜尋關鍵字"),
    session: Session = Depends(get_session)
):
    """搜尋學生（支援姓名、郵箱、國家）"""
    api_logger.info(f"搜尋學生: {keyword}")
    if not keyword:
        api_logger.warning("搜尋關鍵字為空")
        raise HTTPException(status_code=400, detail="搜尋關鍵字不能為空")
    
    results = search_students(session, keyword)
    api_logger.info(f"搜尋結果: 找到 {len(results)} 筆記錄")
    return results

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)