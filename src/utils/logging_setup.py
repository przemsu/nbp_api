import logging
import time
from pathlib import Path

def setup_logging():
    """
    Configures logging for the entire application.
    Sets up file logging and console output with a consistent format using local time.
    """
    log_dir = Path('logs')
    if not log_dir.exists():
        log_dir.mkdir(parents=True, exist_ok=True)

    # Force logging to use local time instead of UTC
    logging.Formatter.converter = time.localtime

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S %z',
        handlers=[
            logging.FileHandler(log_dir / "logs.log", encoding='utf-8', mode='a'),
            logging.StreamHandler()
        ]
    )

