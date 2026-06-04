import yaml

def get_config() -> dict:

    with open('config.yaml', 'r') as f:
        return yaml.full_load(f)