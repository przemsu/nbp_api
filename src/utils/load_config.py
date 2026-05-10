import yaml

def get_curr_code() -> dict:

    with open('config.yaml', 'r') as f:
        return yaml.full_load(f)