
import logging
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(LOG_DIR / "pipeline.log", encoding="utf-8"),
        logging.StreamHandler()
    ]
)

scripts = [
    "src/generate_data.py",
    "src/check_data.py",
    "src/clean_data.py",
    "src/clean_master_data.py",
    "src/load_database.py",
    "src/validate_database.py",
]

logging.info("Banking ETL pipeline started")

for script in scripts:
    logging.info("Running %s", script)

    try:
        result = subprocess.run(
            [sys.executable, str(BASE_DIR / script)],
            cwd=BASE_DIR,
            check=True,
            capture_output=True,
            text=True
        )

        if result.stdout:
            logging.info(result.stdout.strip())

        if result.stderr:
            logging.warning(result.stderr.strip())

        logging.info("%s completed successfully", script)

    except subprocess.CalledProcessError as error:
        logging.error("Pipeline failed at %s", script)

        if error.stdout:
            logging.info(error.stdout.strip())

        if error.stderr:
            logging.error(error.stderr.strip())

        sys.exit(error.returncode)

logging.info("Banking ETL pipeline completed successfully")
