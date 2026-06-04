from src.utils.load_config import get_config
import duckdb
import logging



config = get_config()
db_create_path = config['paths']['db_path']

con = duckdb.connect(db_create_path)

