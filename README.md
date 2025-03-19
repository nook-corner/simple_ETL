File stucture

etl-pipeline-project/
│
├── dags/                        # Apache Airflow DAGs (ถ้ามีการใช้ Airflow)
│   ├── etl_pipeline.py          # DAG สำหรับรัน ETL Process
│
├── data/                         # โฟลเดอร์สำหรับจัดการไฟล์ข้อมูล
│   ├── landing_zone/             # ผู้ใช้วางไฟล์ที่ต้องการประมวลผล
│   ├── trading_txn/              # โฟลเดอร์ปลายทางสำหรับไฟล์ที่จัดการแล้ว
│       ├── 2025/                 # โฟลเดอร์แบ่งตามเดือน (YYYY-MM)
│           ├── 01/               # ตัวอย่างโฟลเดอร์พาร์ทิชัน
│               ├── txn_202501.csv
│
├── src/                          # โค้ดหลักของ ETL Pipeline
│   ├── __init__.py               # บอกว่าโฟลเดอร์นี้เป็นโมดูล
│   ├── extract.py                # ฟังก์ชันดึงข้อมูลจาก CSV
│   ├── transform.py              # ฟังก์ชันแปลงข้อมูล (เพิ่ม `month_year` และเปลี่ยน Data Type)
│   ├── load.py                   # ฟังก์ชันโหลดข้อมูลลง PostgreSQL (รองรับ UPSERT)
│   ├── file_handler.py           # จัดการไฟล์ CSV และโฟลเดอร์พาร์ทิชัน
│   ├── config.py                 # ค่าตั้งค่าต่าง ๆ (Database URI)
│   ├── utils.py                  # ฟังก์ชันเสริม เช่น Logging และ Data Validation
│
├── tests/                        # ไฟล์ทดสอบสำหรับตรวจสอบการทำงาน
│   ├── test_extract.py           # ทดสอบ Extract Process
│   ├── test_transform.py         # ทดสอบ Transform Process
│   ├── test_load.py              # ทดสอบ Load Process
│   ├── test_file_handler.py      # ทดสอบ File Handling Process
│
├── config/                       # ไฟล์การตั้งค่าระบบ
│   ├── config.yaml               # ตั้งค่าต่างๆ เช่น Database, File Path
│   ├── logging_config.yaml       # ตั้งค่าระบบ Logging
│
├── requirements.txt              # รายการ Dependencies ที่ต้องติดตั้ง
├── Dockerfile                    # Dockerfile สำหรับการใช้งานใน Container (ถ้ามี)
├── .gitignore                    # ไฟล์ที่ไม่ต้องการให้ Git track
└── README.md                     # รายละเอียดโปรเจค (วิธีติดตั้งและใช้งาน)
