from etl.extract.get_raw_data import get_raw_nbp_api_data
from src.utils.logging_setup import setup_logging

if __name__ == '__main__':
    setup_logging()
    get_raw_nbp_api_data('main')
    get_raw_nbp_api_data('alt')
    get_raw_nbp_api_data('buy_sell')
                       
