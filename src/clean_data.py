import pandas as pd
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"

PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

# Load raw transaction data
df = pd.read_csv(RAW_DIR / "transactions.csv")

print("Before cleaning:", df.shape)

# 1. Remove duplicate transactions
df = df.drop_duplicates(
    subset=["transaction_id"],
    keep="first"
)

# 2. Remove rows with missing required values
df = df.dropna(
    subset=[
        "transaction_id",
        "transaction_date",
        "customer_id",
        "account_id",
        "amount"
    ]
)

# 3. Remove invalid transaction amounts
df = df[df["amount"] > 0]

# 4. Validate transaction types
valid_types = [
    "Deposit",
    "Withdrawal",
    "Transfer",
    "Payment"
]

df = df[df["transaction_type"].isin(valid_types)]

# 5. Validate transaction status
valid_statuses = ["Success", "Failed", "Pending"]

df = df[df["status"].isin(valid_statuses)]

# 6. Save cleaned data
output_file = PROCESSED_DIR / "transactions_cleaned.csv"

df.to_csv(output_file, index=False)

print("After cleaning:", df.shape)
print("Remaining duplicates:", df["transaction_id"].duplicated().sum())
print("Remaining missing values:", df.isnull().sum().sum())
print("Cleaned file saved to:", output_file)