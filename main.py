from etl.extract.get_raw_data import get_raw_nbp_api_data

if __name__ == '__main__':
  get_raw_nbp_api_data('main')
  get_raw_nbp_api_data('alt')
  get_raw_nbp_api_data('buy_sell')
                       
