```
etl-pipeline-project/
│
├── dags/                        # Apache Airflow DAGs (if using Airflow)
│   ├── etl_pipeline.py          # DAG to schedule ETL process
│
├── data/                         # Data storage
│   ├── landing_zone/             # Users place raw CSV files here
│   ├── trading_txn/              # Processed files move here
│       ├── 2025/                 # Monthly partitioning
│           ├── 01/               # Example partition
│               ├── txn_202501.csv
│
├── src/                          # ETL source code
│   ├── __init__.py               # Marks directory as a Python module
│   ├── extract.py                # Extract process (CSV ingestion)
│   ├── transform.py              # Transform process (add `month_year`, convert types)
│   ├── load.py                   # Load process (PostgreSQL + UPSERT)
│   ├── file_handler.py           # Manage file movements and partitions
│   ├── config.py                 # Configuration settings (DB connection)
│   ├── utils.py                  # Utility functions (Logging, Validation)
│
├── tests/                        # Unit tests
│   ├── test_extract.py           # Test extract process
│   ├── test_transform.py         # Test transform process
│   ├── test_load.py              # Test load process
│   ├── test_file_handler.py      # Test file handling
│
├── config/                       # Configuration files
│   ├── config.yaml               # Database settings
│   ├── logging_config.yaml       # Logging configuration
│
├── requirements.txt              # Python dependencies
├── Dockerfile                    # Docker setup (if needed)
├── .gitignore                    # Ignore unnecessary files
└── README.md                     # Project documentation
```
