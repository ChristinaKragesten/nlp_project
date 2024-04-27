from pathlib import Path

import pandas as pd
import yaml


class SetUpData:
    def __init__(self, config_filepath: str, text_filepath: str):
        self.config = self.read_yaml(filepath=config_filepath)
        self.text = self.convert_txt_to_string(txt_filepath=text_filepath)

    @staticmethod
    def read_yaml(filepath):
        with open(filepath) as f:
            try:
                return yaml.safe_load(f)
            except yaml.YAMLError as exc:
                print(exc)

    def convert_txt_to_string(self, txt_filepath):
        with open(txt_filepath, "r") as file:
            text = file.read()
        return text
