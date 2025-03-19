import os
import shutil
import re
import logging

#Logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

LANDING_ZONE = "data/landing_zone/"
TARGET_FOLDER = "data/trading_txn/monthly/"

def detect_partition_from_filename(file_name):
    try:
        match = re.match(r"txn_(\d{6})\.csv", file_name)
        if match:
            year_month = match.group(1)
            partition = f"{year_month[:4]}-{year_month[4:]}" 
            return partition
        return None
    except Exception as e:
        logging.error(f"Error detecting partition from filename {file_name}: {e}")
        return None

def move_file_to_trading_txn(file_path):
    try:
        file_name = os.path.basename(file_path)
        partition = detect_partition_from_filename(file_name)

        if partition:
            destination_dir = os.path.join(TARGET_FOLDER, partition)
            os.makedirs(destination_dir, exist_ok=True)  #Create folder

            destination_path = os.path.join(destination_dir, file_name)
            shutil.move(file_path, destination_path)  #Replace existing file
            logging.info(f"Moved {file_name} to {destination_path}")
        else:
            logging.warning(f"Skipping {file_name} - Invalid filename format")
    except Exception as e:
        logging.error(f"Error moving file {file_name}: {e}")

def process_landing_zone():
    try:
        if not os.path.exists(LANDING_ZONE):
            logging.error(f"Landing zone path '{LANDING_ZONE}' does not exist.")
            return
        
        #Selected file txn_ and .csv
        files = [f for f in os.listdir(LANDING_ZONE) if re.match(r"txn_\d{6}\.csv", f)]
        
        if not files:
            logging.info("No files found in landing zone.")
            return

        for file in files:
            file_path = os.path.join(LANDING_ZONE, file)
            move_file_to_trading_txn(file_path)

    except Exception as e:
        logging.error(f"Error processing landing zone: {e}")

if __name__ == "__main__":
    process_landing_zone()
