import requests
import json
from src.utils.load_config import get_config
from src.utils.daily_dir_creation import create_dir_daily_load
import logging

# Create logger dedicated for this module
logger = logging.getLogger(__name__)

def get_raw_nbp_api_data(endpoint_type: str) -> None:
    """
    Fetch raw data (FX rates or Gold prices) from official NBP API.
    Saves the first element of the response as a JSON file in the bronze layer.
    """
    try:
        config = get_config()
        logger.info("Config file loaded.")
        
        # Get the relative endpoint path directly from config
        currency_endpoint = config['endpoints'][endpoint_type]
        
        # NBP API base url and directory paths
        api_path = config['paths']['nbp_api_url']
        raw_data_dir_path = config['paths']['raw_data_dir']
        
        logger.debug(f"Requesting endpoint: {currency_endpoint}")

        # Call API - snapshot for the current day
        response = requests.get(f"{api_path}{currency_endpoint}", timeout=10)
        response.raise_for_status()
        logger.info(f"API request for {endpoint_type} successful.")

        # Prepare directory and save file
        path_to_save_file = create_dir_daily_load(raw_data_dir_path)
        
        with open(f"{path_to_save_file}/{endpoint_type}.json", 'w', encoding='utf-8') as file:
            # NBP returns a single-element list for both tables and gold (for current day)
            json.dump(response.json()[0], file, indent=4, ensure_ascii=False)
            logger.info(f"Raw data for {endpoint_type} saved at {path_to_save_file}")
            
    except Exception as err:
        # Use logger.exception to capture the full stack trace for debugging
        logger.exception(f"Failed to process {endpoint_type}: {err}")
