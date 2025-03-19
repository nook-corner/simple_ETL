# src/utils.py
import pandas as pd
import logging

def validate_data(data):
    """
    ฟังก์ชันนี้ใช้ในการตรวจสอบคุณภาพของข้อมูล
    ตรวจสอบข้อมูลที่ขาดหาย, ค่าผิดปกติ, และค่าซ้ำ
    """
    if data.empty:
        logging.warning("Data is empty.")
        raise Exception("Data is empty, cannot proceed.")

    # ตรวจสอบ Missing Values (ค่าที่หายไป)
    missing_data = data.isnull().sum()
    if missing_data.any():
        logging.warning(f"Missing data detected: {missing_data}")
        # อาจจะสามารถจัดการได้ เช่น การแทนที่ค่าที่หายไป หรือการลบข้อมูลที่มีค่าหายไป
        data = data.dropna()  # ลบแถวที่มีค่า missing

    # ตรวจสอบค่าผิดปกติ (เช่น อายุเป็นลบ)
    if 'age' in data.columns:
        if (data['age'] < 0).any():
            logging.warning("Negative values found in 'age' column.")
            data = data[data['age'] >= 0]  # ลบแถวที่มีอายุเป็นลบ

    # ตรวจสอบค่าซ้ำ (duplicate values)
    duplicates = data.duplicated().sum()
    if duplicates > 0:
        logging.warning(f"Found {duplicates} duplicate rows.")
        data = data.drop_duplicates()  # ลบแถวที่ซ้ำ

    # ตรวจสอบค่าที่ไม่สมเหตุสมผล เช่น อายุคนที่มากเกินไป
    if 'age' in data.columns:
        if (data['age'] > 120).any():  # สมมติว่าอายุคนไม่เกิน 120
            logging.warning("Age value greater than 120 found.")
            data = data[data['age'] <= 120]

    # สามารถเพิ่มการตรวจสอบอื่น ๆ ได้ตามที่ต้องการ
    logging.info("Data validation completed successfully.")
    return data

def setup_logging(log_file='etl_log.log'):
    """ ตั้งค่าการบันทึก Log """
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )