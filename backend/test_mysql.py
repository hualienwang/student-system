import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

def test_mysql_connection():
    """測試 MySQL 連接"""
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "3306")),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "1234"),
            database=os.getenv("DB_NAME", "student_db")
        )
        
        if connection.is_connected():
            print("✅ MySQL 連接成功！")
            
            # 檢查資料庫是否存在
            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            
            print("📁 可用資料庫：")
            for db in databases:
                print(f"  - {db[0]}")
            
            # 嘗試建立資料庫
            db_name = os.getenv("DB_NAME", "student_db")
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
            print(f"✅ 資料庫 {db_name} 已建立/確認存在")
            
            cursor.close()
            connection.close()
            print("✅ 連接已關閉")
            
    except Error as e:
        print(f"❌ MySQL 連接錯誤: {e}")
        print("\n🔧 故障排除步驟：")
        print("1. 確認 MySQL 服務是否啟動：")
        print("   - Windows: 打開服務管理器，檢查 MySQL 服務狀態")
        print("   - 命令提示字元: net start mysql")
        print("\n2. 確認 root 密碼：")
        print("   - 如果您忘記了密碼，可以重置：")
        print("   - 停止 MySQL 服務: net stop mysql")
        print("   - 啟動無驗證模式: mysqld --skip-grant-tables")
        print("   - 重新設定密碼: UPDATE mysql.user SET authentication_string=PASSWORD('新密碼') WHERE User='root';")
        print("\n3. 建立新用戶（如果 root 有問題）：")
        print("   CREATE USER 'student_user'@'localhost' IDENTIFIED BY 'password123';")
        print("   GRANT ALL PRIVILEGES ON student_db.* TO 'student_user'@'localhost';")

if __name__ == "__main__":
    test_mysql_connection()