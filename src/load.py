# src/load.py

import pandas as pd
import logging
from sqlalchemy import create_engine, text
from src.config import get_db_uri

#Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

TABLE_NAME = "trading_transactions"  

def load_data_to_postgres(data):
    try:
        if data is None or data.empty:
            logging.warning("No data to load. Skipping database insertion.")
            return

        engine = create_engine(get_db_uri())
        with engine.begin() as conn:
            for _, row in data.iterrows():
                query = text(f"""
                    INSERT INTO {TABLE_NAME} (transaction_id, trade_date, stock_symbol, order_type, quantity, price_per_unit, total_price, currency, month_year)
                    VALUES (:transaction_id, :trade_date, :stock_symbol, :order_type, :quantity, :price_per_unit, :total_price, :currency, :month_year)
                    ON CONFLICT (month_year) DO UPDATE 
                    SET quantity = EXCLUDED.quantity,
                        price_per_unit = EXCLUDED.price_per_unit,
                        total_price = EXCLUDED.total_price;
                """)
                
                conn.execute(query, row.to_dict())

        logging.info(f"Successfully loaded {len(data)} rows into {TABLE_NAME} with UPSERT.")

    except Exception as e:
        logging.error(f"Error loading data into PostgreSQL: {e}")
