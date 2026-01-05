import logging
import sys
from datetime import datetime
from pathlib import Path

# 創建日誌目錄
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# 設置日誌格式
log_format = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# 設置控制台處理器
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(log_format)

# 設置文件處理器
file_handler = logging.FileHandler(
    log_dir / f"app_{datetime.now().strftime('%Y%m%d')}.log",
    encoding='utf-8'
)
file_handler.setFormatter(log_format)

# 設置根日誌記錄器
logging.basicConfig(
    level=logging.INFO,
    handlers=[console_handler, file_handler]
)

# 專門用於應用程序的日誌記錄器
app_logger = logging.getLogger("student_system")
app_logger.setLevel(logging.INFO)

# 添加處理器（如果尚未添加）
if not app_logger.handlers:
    app_logger.addHandler(console_handler)
    app_logger.addHandler(file_handler)

# 專門用於數據庫操作的日誌記錄器
db_logger = logging.getLogger("database")
db_logger.setLevel(logging.INFO)

# 專門用於API請求的日誌記錄器
api_logger = logging.getLogger("api")
api_logger.setLevel(logging.INFO)

def get_logger(name: str) -> logging.Logger:
    """
    獲取指定名稱的日誌記錄器
    """
    return logging.getLogger(name)