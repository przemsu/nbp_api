import requests
import json
from src.utils.load_config import get_curr_code
from src.utils.daily_dir_creation import create_dir_daily_load

def get_raw_nbp_api_data(currency_type: str) -> None:
    """
    Function to get data from official Polish NBP API about main and alt cureencies.
    Data about name, code and mid rate for given date. 
    Saved as plain JSON in raw folder.
    """
    # Load API configuration from yaml file
    config = get_curr_code()
    # Endpoints
    currency_endpoint = config['endpoints'][currency_type]
    # NBP API url
    api_path = config['paths']['nbp_api_url']
    # Path for raw data to create dirs per daily load - snapshots
    raw_data_dir_path = config['paths']['raw_data_dir']
    # Call API based on input parameter and save json file in raw data folder - BRONZE layer
    try: 
        response = requests.get(
            f"{api_path}{currency_endpoint}",
            timeout=10
            )
        response.raise_for_status()

        path_to_save_file = create_dir_daily_load(raw_data_dir_path)

        with open(f"{path_to_save_file}/{currency_type}.json", 'w', encoding='utf-8') as file:
            json.dump(response.json()[0], file, ensure_ascii=False)
    except requests.exceptions.HTTPError as err:
        print("HTTP error occurred:", err)

if __name__ == '__main__':
    get_raw_nbp_api_data('main')
    get_raw_nbp_api_data('alt')
    get_raw_nbp_api_data('buy_sell')