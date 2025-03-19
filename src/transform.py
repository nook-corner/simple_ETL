# src/transform.py

import pandas as pd
import logging

#Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

def transform_data(data):

    try:
        if data is None or data.empty:
            logging.warning("Received empty DataFrame for transformation.")
            return None

        data["transaction_id"] = data["transaction_id"].astype(str)
        data["trade_date"] = pd.to_datetime(data["trade_date"], errors="coerce")
        data["stock_symbol"] = data["stock_symbol"].astype(str)
        data["order_type"] = data["order_type"].astype(str)
        data["quantity"] = pd.to_numeric(data["quantity"], errors="coerce").fillna(0).astype(int)
        data["price_per_unit"] = pd.to_numeric(data["price_per_unit"], errors="coerce").fillna(0.0).astype(float)
        data["total_price"] = pd.to_numeric(data["total_price"], errors="coerce").fillna(0.0).astype(float)
        data["currency"] = data["currency"].astype(str)
        data["month_year"] = data["trade_date"].dt.strftime("%Y%m") #format YYYYMM
        data["month_year"] = data["month_year"].astype(str) 

        logging.info("Data transformation completed successfully.")
        return data

    except Exception as e:
        logging.error(f"Error transforming data: {e}")
        return None
