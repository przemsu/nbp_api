import requests
import dlt
import duckdb
from datetime import date, timedelta

@dlt.resource(name="currency_daily", write_disposition="append")
def API_call():
    
    data_complete = []
    endpoints = ['A', 'B', 'C']

    conn = duckdb.connect('nbp_currency.duckdb')
    query = f"""
    SELECT count(*)
    FROM currency_nbp.currency_daily
    WHERE db_start = '{date.today()}'
    """
    result = conn.execute(query).fetchone()
    if result[0] == 0:
        for endpoint in endpoints:
            path = f'https://api.nbp.pl/api/exchangerates/tables/{endpoint}'
            try:
                response = requests.get(path)
                rates = response.json()[0]['rates']
            except requests.exceptions.RequestException as e:
                print(f"Error while fetching data from API for endpoint {endpoint}: {e}")
                continue

            for rate in rates:
                data = {
                    'id': f"{rate['code']}_{endpoint}",
                    'endpoint': endpoint,
                    'currency_name': rate['currency'],
                    'currency_code': rate['code'],
                    **(
                        {'currency_mid_price': rate['mid']}
                        if endpoint != 'C'
                        else {
                            'currency_bid_price': rate['bid'],
                            'currency_ask_price': rate['ask']
                        }
                    ),
                    'db_start': date.today(),
                    'db_end': date.today()+ timedelta(1)
                }
                data_complete.append(data)
            yield data_complete
    else: 
        print(f'Data for {date.today()} already exists in databes.')

if __name__ == "__main__":
    pipeline = dlt.pipeline(
        pipeline_name="nbp_currency",
        destination="duckdb",
        dataset_name="currency_nbp"
    )
    load_info = pipeline.run(API_call())
    print(load_info)
