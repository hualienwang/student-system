from sqlmodel import SQLModel, create_engine, Session
from typing import Generator
import os
from dotenv import load_dotenv

load_dotenv()

# 資料庫連接配置 - 使用更穩定的配置
DB_TYPE = os.getenv("DB_TYPE", "sqlite")  # 默認為 SQLite，如果沒有 MySQL

if DB_TYPE == "mysql":
    # MySQL 配置
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DB_PORT = os.getenv("DB_PORT", "3306")
    DB_USER = os.getenv("DB_USER", "root")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "1234")
    DB_NAME = os.getenv("DB_NAME", "student_db")
    
    # 修正連接字串
    DATABASE_URL = f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
else:
    # 使用 SQLite 作為備用選項，但在Render環境中使用絕對路徑
    import os
    DATABASE_URL = f"sqlite:///{os.path.join(os.getcwd(), 'student_system.db')}"

# 建立資料庫引擎
engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)

def create_db_and_tables():
    """建立資料庫和表格"""
    try:
        SQLModel.metadata.create_all(engine)
        print("✅ 資料庫表格建立成功！")
    except Exception as e:
        print(f"❌ 資料庫連接錯誤: {e}")
        print("請檢查以下設置：")
        print(f"1. MySQL 服務是否啟動 (net start mysql)")
        print(f"2. 帳號密碼是否正確")
        print(f"3. 資料庫 {DB_NAME} 是否存在")

def get_session() -> Generator[Session, None, None]:
    """取得資料庫會話"""
    with Session(engine) as session:
        yield session