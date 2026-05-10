from pathlib import Path
from datetime import datetime

def create_dir_daily_load(dir_path) -> Path:

    now = datetime.now()

    path = (
        Path(dir_path)
        / f"year={now:%Y}"
        / f"month={now:%m}"
        / f"day={now:%d}"
    )

    path.mkdir(parents=True, exist_ok=True)

    return path