import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

def initialize_database():
    """初始化資料庫和表格"""
    try:
        # 先連接到 MySQL 伺服器（不指定資料庫）
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST", "localhost"),
            port=int(os.getenv("DB_PORT", "3306")),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "1234")
        )
        
        if connection.is_connected():
            print("✅ 連接到 MySQL 伺服器成功！")
            
            cursor = connection.cursor()
            
            # 建立資料庫
            db_name = os.getenv("DB_NAME", "student_db")
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name} CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci")
            print(f"✅ 資料庫 {db_name} 已建立")
            
            # 使用資料庫
            cursor.execute(f"USE {db_name}")
            
            # 建立 student 表格
            create_table_query = """
            CREATE TABLE IF NOT EXISTS student (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                gender VARCHAR(10) NOT NULL,
                country VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
            ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
            """
            
            cursor.execute(create_table_query)
            print("✅ 學生表格已建立")
            
            # 插入測試資料
            test_data = [
                ("張小明", "男", "台灣", "ming@example.com"),
                ("李小花", "女", "台灣", "hua@example.com"),
                ("王大明", "男", "中國", "daming@example.com"),
                ("陳小美", "女", "香港", "mei@example.com"),
                ("林志明", "男", "台灣", "zhi@example.com"),
            ]
            
            insert_query = """
            INSERT IGNORE INTO student (name, gender, country, email) 
            VALUES (%s, %s, %s, %s)
            """
            
            cursor.executemany(insert_query, test_data)
            connection.commit()
            print(f"✅ 已插入 {cursor.rowcount} 筆測試資料")
            
            # 顯示表格結構
            cursor.execute("DESCRIBE student")
            columns = cursor.fetchall()
            print("\n📊 表格結構：")
            for column in columns:
                print(f"  {column[0]:<15} {column[1]:<20} {column[2]}")
            
            # 顯示資料
            cursor.execute("SELECT * FROM student")
            students = cursor.fetchall()
            print(f"\n👥 學生資料 ({len(students)} 筆)：")
            for student in students:
                print(f"  ID: {student[0]}, 姓名: {student[1]}, 性別: {student[2]}, 國家: {student[3]}, 郵箱: {student[4]}")
            
            cursor.close()
            connection.close()
            print("\n✅ 資料庫初始化完成！")
            
    except Error as e:
        print(f"❌ 錯誤: {e}")
        print("\n💡 解決方案：")
        print("1. 確認 MySQL 服務已啟動")
        print("2. 確認帳號密碼正確")
        print("3. 可以嘗試使用以下命令啟動 MySQL:")
        print("   - Windows: net start mysql")
        print("   - 或使用 XAMPP 控制面板啟動 MySQL")
        
        if "1045" in str(e):
            print("\n🔐 密碼錯誤！請嘗試：")
            print("   1. 編輯 .env 檔案設定正確密碼")
            print("   2. 或使用空密碼: DB_PASSWORD=")
            print("   3. 或建立新用戶:")
            print("      CREATE USER 'student_user'@'localhost' IDENTIFIED BY 'password123';")
            print("      GRANT ALL PRIVILEGES ON *.* TO 'student_user'@'localhost';")

if __name__ == "__main__":
    print("🚀 開始初始化學生資料庫...")
    initialize_database()