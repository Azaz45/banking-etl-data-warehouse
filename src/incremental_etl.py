
import sqlite3
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "database" / "banking.db"
CSV_PATH = BASE_DIR / "data" / "processed" / "transactions_cleaned.csv"

conn = sqlite3.connect(DB_PATH)

df = pd.read_csv(CSV_PATH)

# Read transaction IDs already present in the database
existing_ids = pd.read_sql_query(
    "SELECT transaction_id FROM transactions",
    conn
)["transaction_id"]

# Keep only new transaction records
new_df = df[~df["transaction_id"].isin(existing_ids)]

if not new_df.empty:
    new_df.to_sql(
        "transactions",
        conn,
        if_exists="append",
        index=False
    )
    print(f"New transactions loaded: {len(new_df)}")
else:
    print("No new transactions to load.")

conn.close()
print("Incremental ETL completed!")
