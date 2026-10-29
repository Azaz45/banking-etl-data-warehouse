
import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "processed"
DB_DIR = BASE_DIR / "data" / "database"
DB_DIR.mkdir(parents=True, exist_ok=True)

db_path = DB_DIR / "banking.db"
conn = sqlite3.connect(db_path)

for table in ["customers", "accounts", "transactions"]:
    file_path = DATA_DIR / f"{table}_cleaned.csv"
    df = pd.read_csv(file_path)

    df.to_sql(table, conn, if_exists="replace", index=False)
    print(f"{table}: {len(df)} rows loaded")

conn.close()
print("Database loading completed!")
