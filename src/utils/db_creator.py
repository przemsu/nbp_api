import duckdb
from src.utils.load_config import get_curr_code

def create_db():

    config = get_curr_code()
    db_create_path = config['paths']['db_path']

    con = duckdb.connect(db_create_path)

    con.execute('''
        CREATE TABLE IF NOT EXISTS nbp_api_data_daily_load (
        endpoint_type VARCHAR,
        extraction_date DATE,
        loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        raw_content JSON,
        UNIQUE(endpoint_type, extraction_date)
        )
    '''
    )

    con.close()
