import json
import os


class JsonParser:

    def __init__(self, json_file):
        self.json_file = os.path.expanduser(json_file)
        with open(self.json_file, 'r') as file:
            self.parsed_data = json.load(file)


    def get_number_of_days(self):
        return len(self.parsed_data["daily_routes"])