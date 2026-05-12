import logging
from pathlib import Path

def setup_logging():
    """
    Configures logging for the entire application.
    Sets up file logging and console output with a consistent format.
    """
    log_dir = Path('logs')
    if not log_dir.exists():
        log_dir.mkdir(parents=True, exist_ok=True)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s | %(name)s | %(levelname)s | %(message)s',
        datefmt='%Y-%m-%d %H:%M',
        handlers=[
            logging.FileHandler(log_dir / "logs.log", encoding='utf-8', mode='a'),
            logging.StreamHandler()
        ]
    )
