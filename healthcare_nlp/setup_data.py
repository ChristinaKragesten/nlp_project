import yaml
from pathlib import Path

class SetUpData:
    def __init__(self, config_filepath: str):
        self.config = self.read_yaml(config_filepath)


    @staticmethod
    def read_yaml(filepath):
        with open(filepath) as f:
            try:
                return yaml.safe_load(f)
            except yaml.YAMLError as exc:
                print(exc)