from src.utils.db_creator import create_db, insert_raw_data
from src.utils.load_config import get_config
from pathlib import Path
import json
import logging
import duckdb


logger = logging.getLogger(__name__)

def insert_into_bronze_layer():

    config = get_config()
    db_path = config['paths']['db_path']

    create_db()

    con = duckdb.connect(db_path)

    p = Path(config['paths']['raw_data_dir'])
    files = list(p.rglob('*.json'))
    logger.info(f"Found {len(files)} files in {p}")

    success_count = 0
    error_count = 0
   
    for f in files:
        try:
            # Wyciąganie metadanych ze ścieżki
            extraction_date = f"{f.parts[2].split('=')[-1]}-{f.parts[3].split('=')[-1]}-{f.parts[4].split('=')[-1]}"
            endpoint_type = f.stem
            
            # Wczytywanie treści
            with open(f, 'r', encoding='utf-8') as file:
                json_content = json.load(file)

            # Ładowanie do bazy
            insert_raw_data(con, endpoint_type, extraction_date, json_content)
            success_count += 1
            
        except Exception as e:
            logger.error(f"Failed to process file {f}: {e}")
            error_count += 1
            continue

    con.close()
    logger.info(f"Bronze layer load finished. Success: {success_count}, Errors: {error_count}")