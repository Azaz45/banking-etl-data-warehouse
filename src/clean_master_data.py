
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Clean customers
customers = pd.read_csv(RAW_DIR / "customers.csv")
customers = customers.drop_duplicates(subset=["customer_id"])
customers = customers.dropna(subset=["customer_id"])
customers.to_csv(PROCESSED_DIR / "customers_cleaned.csv", index=False)

# Clean accounts
accounts = pd.read_csv(RAW_DIR / "accounts.csv")
accounts = accounts.drop_duplicates(subset=["account_id"])
accounts = accounts.dropna(subset=["account_id", "customer_id"])
accounts.to_csv(PROCESSED_DIR / "accounts_cleaned.csv", index=False)

print("Customers cleaned:", len(customers))
print("Accounts cleaned:", len(accounts))
print("Master data cleaning completed!")
