import json
from faker import Faker
#no-use
class DataFactory:
    def __init__(self):
        self.fake = Faker()

    def get_user_data(self):
        return {
            "username": self.fake.user_name(),
            "password": self.fake.password(),
        }

    def load_test_data(self, file_path):
        with open(file_path, "r") as file:
            return json.load(file)