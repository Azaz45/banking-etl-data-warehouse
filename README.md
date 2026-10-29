# Banking ETL Pipeline & Data Warehouse

## Project Overview
A Python-based ETL pipeline that generates synthetic banking data, cleans and validates transaction records, and loads the processed data into a SQLite database for analytical queries.

## Tech Stack
- **Python** — ETL workflow and automation
- **Pandas & NumPy** — Data processing
- **SQLite** — Data storage
- **SQL** — Analytical queries
- **Git & GitHub** — Version control

## Project Workflow
1. Generate synthetic customers, accounts, and transaction data.
2. Inspect raw data for quality issues.
3. Clean duplicate transactions, missing values, and invalid amounts.
4. Load cleaned datasets into SQLite.
5. Validate records and run analytical SQL queries.

## Dataset Summary
- Customers: 5,000
- Accounts: 8,000
- Cleaned transactions: 49,920

## Data Quality Checks
- Duplicate transaction IDs: 0
- Invalid transaction amounts: 0
- Missing customer IDs in transactions: 0

## Project Structure
```text
BANKING-ETL-DATA-WAREHOUSE/
├── data/
│   ├── raw/
│   ├── processed/
│   └── database/
├── src/
│   ├── generate_data.py
│   ├── check_data.py
│   ├── clean_data.py
│   ├── clean_master_data.py
│   ├── load_database.py
│   ├── validate_database.py
│   └── run_pipeline.py
├── sql/
│   ├── schema.sql
│   └── analytics_queries.sql
└── README.md
```

## How to Run
1. Create and activate a Python virtual environment.
2. Install dependencies:
   `python -m pip install pandas numpy faker sqlalchemy psycopg2-binary`
3. Run the pipeline:
   `python src/run_pipeline.py`

## Disclaimer
This project uses synthetic banking data for educational purposes. It does not contain real customer or financial information.
