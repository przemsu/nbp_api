import requests
import json
from src.utils.load_config import get_curr_code
from src.utils.daily_dir_creation import create_dir_daily_load
import logging

# Create logger dedicated for this project
logger = logging.getLogger(__name__)

def get_raw_nbp_api_data(currency_type: str) -> None:
    """
    Function to get data from official Polish NBP API about main and alt cureencies.
    Data about name, code and mid rate for given date. 
    Saved as plain JSON in raw folder.
    """

    # Load API configuration from yaml file
    try:
        config = get_curr_code()
        logger.info("Config file loaded.")
        
        # Endpoints
        currency_endpoint = config['endpoints'][currency_type]
        # NBP API url
        api_path = config['paths']['nbp_api_url']
        # Path for raw data to create dirs per daily load - snapshots
        raw_data_dir_path = config['paths']['raw_data_dir']
        logger.debug(f"Variables for {currency_type} created from config.")

        # Call API based on input parameter and save json file in raw data folder - BRONZE layer
        response = requests.get(
            f"{api_path}{currency_endpoint}",
            timeout=10
            )
        response.raise_for_status()
        logger.info(f"Request to API for {currency_type} successful.")

        # Path variable for result files
        path_to_save_file = create_dir_daily_load(raw_data_dir_path)

        # Saving raw data into location - bronze layer
        with open(f"{path_to_save_file}/{currency_type}.json", 'w', encoding='utf-8') as file:
            json.dump(response.json()[0], file, ensure_ascii=False)
            logger.info(f"Raw data for {currency_type} saved at {path_to_save_file}")
            
    except requests.exceptions.RequestException as err:
        logger.error(f"Error during API request for {currency_type}: {err}")
    except Exception as err:
        logger.exception(f"Unexpected error occurred while processing {currency_type}")
