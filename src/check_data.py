import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

customers = pd.read_csv(RAW_DIR / "customers.csv")
accounts = pd.read_csv(RAW_DIR / "accounts.csv")
transactions = pd.read_csv(RAW_DIR / "transactions.csv")

print("CUSTOMERS:", customers.shape)
print("ACCOUNTS:", accounts.shape)
print("TRANSACTIONS:", transactions.shape)

print("\nTransaction sample:")
print(transactions.head())

print("\nMissing values:")
print(transactions.isnull().sum())

print("\nDuplicate transaction IDs:")
print(transactions["transaction_id"].duplicated().sum())

print("\nNegative transaction amounts:")
print((transactions["amount"] < 0).sum())