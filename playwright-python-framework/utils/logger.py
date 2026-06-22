import logging
import os

REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)

def get_logger():
    logger = logging.getLogger("playwright-framework")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        file_handler = logging.FileHandler(os.path.join(REPORT_DIR, "automation.log"))
        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger