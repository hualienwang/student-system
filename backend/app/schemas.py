from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class StudentBase(BaseModel):
    """學生基本架構"""
    name: str
    gender: str
    country: str
    email: EmailStr

class StudentCreate(StudentBase):
    """建立學生請求架構"""
    pass

class StudentUpdate(BaseModel):
    """更新學生請求架構"""
    name: Optional[str] = None
    gender: Optional[str] = None
    country: Optional[str] = None
    email: Optional[EmailStr] = None

class StudentResponse(StudentBase):
    """學生回應架構"""
    id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True