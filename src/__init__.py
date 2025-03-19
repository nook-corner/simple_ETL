# src/__init__.py
"""
การใช้ไฟล์ __init__.py นี้จะทำให้คุณสามารถ import ฟังก์ชันจากภายในโฟลเดอร์ src/ ได้ง่ายขึ้น เช่น:
from src import extract, transform, load
หรือถ้าต้องการใช้ฟังก์ชันโดยตรง:
from src import extract_data_from_csv, transform_data, load_data_to_postgres
โดยไม่ต้องเรียกใช้เส้นทางที่ลึกกว่าหรือใช้คำสั่ง import แบบเต็มที่ เช่น from src.extract import extract_data_from_csv
การใช้ไฟล์ __init__.py เป็นการทำให้โฟลเดอร์กลายเป็นโมดูลที่สามารถนำไปใช้ในโปรเจคอื่นได้ และช่วยให้การ import ฟังก์ชันต่าง ๆ เป็นระเบียบและสะดวกขึ้น
"""

# นำเข้าฟังก์ชันจากแต่ละโมดูลใน src เพื่อให้สามารถใช้ได้โดยตรง
from .extract import extract_data_from_csv, extract_data_from_api
from .transform import transform_data
from .load import load_data_to_postgres
from .utils import setup_logging, validate_data
from .config import DB_CONFIG, API_CONFIG
