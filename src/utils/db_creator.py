import duckdb
from src.utils.load_config import get_config
import logging

# Create logger dedicated for this module
logger = logging.getLogger(__name__)

config = get_config()

def create_db():

    db_create_path = config['paths']['db_path']

    con = duckdb.connect(db_create_path)

    con.execute('''
        CREATE OR REPLACE TABLE raw_nbp_api_data (
        endpoint_type VARCHAR,
        extraction_date DATE,
        raw_content JSON,
        loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(endpoint_type, extraction_date)
        );
    '''
    )

    con.close()

def insert_raw_data(con, endpoint_type, extraction_date, file_path):

    con.execute("""
                INSERT INTO raw_nbp_api_data (endpoint_type, extraction_date, raw_content)
                VALUES (?, ?, ?) 
                ON CONFLICT DO NOTHING;"""
              , [endpoint_type, extraction_date, file_path]
    )