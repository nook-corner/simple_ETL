#src/extract.py

import os
import pandas as pd
import logging
from src.file_handler import move_file_to_trading_txn, LANDING_ZONE

#Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

#Schema config
EXPECTED_COLUMNS = [
    "transaction_id", "trade_date", "stock_symbol", "order_type",
    "quantity", "price_per_unit", "total_price", "currency"
]

def extract_data_from_csv(file_path):

    try:
        if not os.path.exists(file_path):
            logging.error(f"File {file_path} not found.")
            return None

        data = pd.read_csv(file_path, encoding="utf-8" , dtype=str)
        csv_columns = list(data.columns)

        #check col dup 
        if len(csv_columns) != len(set(csv_columns)):
            logging.error(f"Duplicate column names detected in {file_path}. Skipping file.")
            return None

        #chech col
        if set(csv_columns) != set(EXPECTED_COLUMNS):
            logging.error(f"Column names mismatch in {file_path}. Expected {EXPECTED_COLUMNS}, but got {csv_columns}. Skipping file.")
            return None

        #chcek Schema = col
        if csv_columns != EXPECTED_COLUMNS:
            logging.warning(f"Reordering columns in {file_path} to match expected schema.")
            data = data[EXPECTED_COLUMNS]

        logging.info(f"Extracted data from {file_path} successfully.")
        return data

    except Exception as e:
        logging.error(f"Error extracting data from {file_path}: {e}")
        return None

def process_extraction():
    try:
        if not os.path.exists(LANDING_ZONE):
            logging.error(f"Landing zone path '{LANDING_ZONE}' does not exist.")
            return

        files = [f for f in os.listdir(LANDING_ZONE) if f.startswith("txn_") and f.endswith(".csv")]

        if not files:
            logging.info("No CSV files found in landing zone.")
            return

        for file in files:
            file_path = os.path.join(LANDING_ZONE, file)
            data = extract_data_from_csv(file_path)

            if data is not None:
                move_file_to_trading_txn(file_path) 

    except Exception as e:
        logging.error(f"Error processing extraction: {e}")

if __name__ == "__main__":
    process_extraction()
