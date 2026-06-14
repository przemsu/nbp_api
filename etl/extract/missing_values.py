from datetime import datetime, timedelta
from src.utils.load_config import get_config
from pathlib import Path
import logging

# Create logger dedicated for this module
logger = logging.getLogger(__name__)

def get_missing_data() -> list:

    config = get_config()
    p = Path(config['paths']['raw_data_dir'])
    files = list(p.rglob('*.json'))

    processed_dates = sorted(set([
        datetime.strptime(f"{f.parts[2].split('=')[-1]}-{f.parts[3].split('=')[-1]}-{f.parts[4].split('=')[-1]}", "%Y-%m-%d").date()
        for f in files
    ]))

    start_date = datetime.now() - timedelta(days=14)

    list_of_dates = [
        (start_date + timedelta(days=i)).date() 
        for i in range(15)
        if (start_date + timedelta(days=i)).weekday() < 5]

    return [
        i 
        for i in list_of_dates 
        if i not in processed_dates
        ]