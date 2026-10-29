
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "data" / "database" / "banking.db"

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

checks = {
    "Customers": "SELECT COUNT(*) FROM customers",
    "Accounts": "SELECT COUNT(*) FROM accounts",
    "Transactions": "SELECT COUNT(*) FROM transactions",
    "Duplicate transaction IDs": """
        SELECT COUNT(*) FROM (
            SELECT transaction_id
            FROM transactions
            GROUP BY transaction_id
            HAVING COUNT(*) > 1
        )
    """,
    "Invalid transaction amounts": """
        SELECT COUNT(*) FROM transactions WHERE amount <= 0
    """,
    "Missing customer IDs in transactions": """
        SELECT COUNT(*) FROM transactions WHERE customer_id IS NULL
    """
}

for name, query in checks.items():
    cursor.execute(query)
    print(f"{name}: {cursor.fetchone()[0]}")

conn.close()
