from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class Student(SQLModel, table=True):
    """學生資料模型"""
    __tablename__ = "student"
    
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, nullable=False)
    gender: str = Field(max_length=10, nullable=False)
    country: str = Field(max_length=50, nullable=False)
    email: str = Field(max_length=100, nullable=False, unique=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
    
    class Config:
        arbitrary_types_allowed = True