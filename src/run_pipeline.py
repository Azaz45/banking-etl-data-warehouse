
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

scripts = [
    "src/generate_data.py",
    "src/check_data.py",
    "src/clean_data.py",
    "src/clean_master_data.py",
    "src/load_database.py",
    "src/validate_database.py",
]

for script in scripts:
    print(f"\n{'=' * 45}")
    print(f"Running: {script}")
    print("=" * 45)

    result = subprocess.run(
        [sys.executable, str(BASE_DIR / script)],
        cwd=BASE_DIR
    )

    if result.returncode != 0:
        print(f"Pipeline failed at: {script}")
        sys.exit(result.returncode)

print("\nBanking ETL pipeline completed successfully!")
