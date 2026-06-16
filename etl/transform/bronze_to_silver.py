from src.utils.load_config import get_config
import duckdb
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

def insert_into_silver_layer():

    config = get_config()
    db_path = config['paths']['db_path']
    con = duckdb.connect(db_path)

    p = Path(config['paths']['sql_files_path']['ddl'])
    files = sorted(list(p.rglob('*.sql')))

    for f in files:
        with open(f, 'r') as ddl:
            q_sql = ddl.read()

        try:
            con.execute(q_sql)
            logger.info(f"View {f.stem.upper()} created.")
        except Exception as e:
            logger.error(f"Failed to process: {e}")
    
    con.close()
    logger.info(f"Silver layer load finished. {len(files)} views added to db.")