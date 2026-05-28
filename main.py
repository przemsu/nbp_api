from etl.extract.get_raw_data import get_raw_nbp_api_data
from src.utils.logging_setup import setup_logging
from etl.transform.raw_to_bronze import insert_into_bronze_layer

if __name__ == '__main__':
    # Logging setup
    setup_logging()
    # API call
    get_raw_nbp_api_data('main')
    get_raw_nbp_api_data('alt')
    get_raw_nbp_api_data('buy_sell')
    get_raw_nbp_api_data('gold')
    # In memory database loading
    insert_into_bronze_layer()