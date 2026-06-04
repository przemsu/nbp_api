from pathlib import Path
from datetime import datetime, date

def create_dir_daily_load(raw_dir_path, load_date: date = None) -> Path:

    if not load_date:
        load_date = datetime.now().date()

    year = load_date.year 
    month = f'{load_date.month:02d}'
    day = f'{load_date.day:02d}'
    
    path = (
        Path(raw_dir_path)
        / f"year={year}"
        / f"month={month}"
        / f"day={day}"
    )

    path.mkdir(parents=True, exist_ok=True)

    return path