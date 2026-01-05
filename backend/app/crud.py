from sqlmodel import Session, select
from typing import List, Optional
from .models import Student
from .schemas import StudentCreate, StudentUpdate
from datetime import datetime

def create_student(session: Session, student: StudentCreate) -> Student:
    """建立學生資料"""
    db_student = Student(**student.model_dump())
    session.add(db_student)
    session.commit()
    session.refresh(db_student)
    return db_student

def get_student(session: Session, student_id: int) -> Optional[Student]:
    """取得單一學生資料"""
    return session.get(Student, student_id)

def get_students(session: Session, skip: int = 0, limit: int = 100) -> List[Student]:
    """取得所有學生資料"""
    statement = select(Student).offset(skip).limit(limit)
    result = session.exec(statement)
    return result.all()

def update_student(session: Session, student_id: int, student_update: StudentUpdate) -> Optional[Student]:
    """更新學生資料"""
    db_student = session.get(Student, student_id)
    if not db_student:
        return None
    
    student_data = student_update.model_dump(exclude_unset=True)
    for key, value in student_data.items():
        setattr(db_student, key, value)
    
    db_student.updated_at = datetime.now()
    session.add(db_student)
    session.commit()
    session.refresh(db_student)
    return db_student

def delete_student(session: Session, student_id: int) -> bool:
    """刪除學生資料"""
    db_student = session.get(Student, student_id)
    if not db_student:
        return False
    
    session.delete(db_student)
    session.commit()
    return True

def search_students(session: Session, keyword: str) -> List[Student]:
    """搜尋學生資料"""
    statement = select(Student).where(
        (Student.name.contains(keyword)) |
        (Student.email.contains(keyword)) |
        (Student.country.contains(keyword))
    )
    result = session.exec(statement)
    return result.all()