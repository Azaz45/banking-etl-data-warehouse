import pandas as pd
import numpy as np
from faker import Faker
from pathlib import Path

# -----------------------------
# Project paths
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "data" / "raw"

RAW_DIR.mkdir(parents=True, exist_ok=True)

# -----------------------------
# Setup
# -----------------------------
fake = Faker()
np.random.seed(42)

# Number of records
NUM_CUSTOMERS = 5000
NUM_ACCOUNTS = 8000
NUM_TRANSACTIONS = 50000

# -----------------------------
# 1. Generate Customers
# -----------------------------
customers = []

for i in range(1, NUM_CUSTOMERS + 1):
    customers.append({
        "customer_id": i,
        "customer_name": fake.name(),
        "email": fake.email(),
        "country": fake.country(),
        "customer_type": np.random.choice(
            ["Individual", "Business"]
        ),
        "created_date": fake.date_between(
            start_date="-5y",
            end_date="today"
        )
    })

customers_df = pd.DataFrame(customers)

# -----------------------------
# 2. Generate Accounts
# -----------------------------
accounts = []

for i in range(1, NUM_ACCOUNTS + 1):
    customer_id = np.random.randint(1, NUM_CUSTOMERS + 1)

    accounts.append({
        "account_id": i,
        "customer_id": customer_id,
        "account_type": np.random.choice(
            ["Savings", "Current", "Credit"]
        ),
        "branch_id": np.random.randint(1, 101),
        "open_date": fake.date_between(
            start_date="-5y",
            end_date="today"
        ),
        "currency": np.random.choice(
            ["INR", "USD", "GBP", "EUR"]
        )
    })

accounts_df = pd.DataFrame(accounts)

# -----------------------------
# 3. Generate Transactions
# -----------------------------
transactions = []

for i in range(1, NUM_TRANSACTIONS + 1):

    account_id = np.random.randint(
        1, NUM_ACCOUNTS + 1
    )

    customer_id = accounts_df.loc[
        accounts_df["account_id"] == account_id,
        "customer_id"
    ].iloc[0]

    transactions.append({
        "transaction_id": i,
        "transaction_date": fake.date_between(
            start_date="-2y",
            end_date="today"
        ),
        "customer_id": customer_id,
        "account_id": account_id,
        "transaction_type": np.random.choice(
            [
                "Deposit",
                "Withdrawal",
                "Transfer",
                "Payment"
            ]
        ),
        "amount": round(
            np.random.uniform(10, 100000),
            2
        ),
        "currency": np.random.choice(
            ["INR", "USD", "GBP", "EUR"]
        ),
        "channel": np.random.choice(
            [
                "Online",
                "ATM",
                "Branch",
                "Mobile"
            ]
        ),
        "status": np.random.choice(
            [
                "Success",
                "Failed",
                "Pending"
            ],
            p=[0.90, 0.05, 0.05]
        ),
        "branch_id": np.random.randint(1, 101)
    })

transactions_df = pd.DataFrame(transactions)

# -----------------------------
# 4. Add intentional data quality issues
# -----------------------------

# Duplicate transactions
duplicate_rows = transactions_df.sample(
    100,
    random_state=42
)

transactions_df = pd.concat(
    [transactions_df, duplicate_rows],
    ignore_index=True
)

# Missing customer IDs
missing_indexes = transactions_df.sample(
    50,
    random_state=42
).index

transactions_df.loc[
    missing_indexes,
    "customer_id"
] = np.nan

# Invalid transaction amounts
invalid_indexes = transactions_df.sample(
    30,
    random_state=24
).index

transactions_df.loc[
    invalid_indexes,
    "amount"
] = -100

# -----------------------------
# 5. Save Raw Data
# -----------------------------

customers_df.to_csv(
    RAW_DIR / "customers.csv",
    index=False
)

accounts_df.to_csv(
    RAW_DIR / "accounts.csv",
    index=False
)

transactions_df.to_csv(
    RAW_DIR / "transactions.csv",
    index=False
)

# -----------------------------
# 6. Print Results
# -----------------------------

print("====================================")
print("Banking Data Generation Completed")
print("====================================")

print(f"Customers: {len(customers_df):,}")
print(f"Accounts: {len(accounts_df):,}")
print(f"Transactions: {len(transactions_df):,}")

print("\nFiles created:")

print(RAW_DIR / "customers.csv")
print(RAW_DIR / "accounts.csv")
print(RAW_DIR / "transactions.csv")