#src/config.py

import os
from dotenv import load_dotenv

# โหลดตัวแปรจาก .env
load_dotenv()

DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'port': int(os.getenv('DB_PORT', 5432)),
    'user': os.getenv('DB_USER', 'default_user'),
    'password': os.getenv('DB_PASSWORD', 'default_password'),
    'db_name': os.getenv('DB_NAME', 'default_db')
}

API_CONFIG = {
    'url': os.getenv('API_URL', 'https://api.example.com/data'),
    'headers': {'Authorization': f"Bearer {os.getenv('API_KEY', 'default_api_key')}"}
}

def get_db_uri():
    """สร้าง PostgreSQL Database URI"""
    return f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['db_name']}"

