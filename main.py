from etl.extract.get_raw_data import get_raw_nbp_api_data
from src.utils.logging_setup import setup_logging
from etl.transform.raw_to_bronze import insert_into_bronze_layer
from etl.extract.missing_values import get_missing_data
from src.utils.load_config import get_config
import logging

if __name__ == '__main__':
    # Logging setup
    setup_logging()
    # Create logger dedicated for this module
    logger = logging.getLogger(__name__)
    # Get missing data if any
    missing_dates = get_missing_data()
    logger.info(f"Found {len(missing_dates)} missing dates.")
    config_all = get_config()
    config_endpoints_key_names = config_all["endpoints"]
    endpoints_key = config_endpoints_key_names.keys()
    # Main script
    if missing_dates:
        logger.info(f"Starting Reactive Backfill for {len(missing_dates)} days.")
        for d in missing_dates:
            for k in endpoints_key:
                get_raw_nbp_api_data(k, d)
    else:
        logger.info("Data history on disk is complete.")
    # API call
    logger.info("Starting current rates download (Daily Load)...")
    for k in endpoints_key:
        get_raw_nbp_api_data(k)
    # In memory database loading
    insert_into_bronze_layer()