import requests
from config.config import BASE_URL


class APIClient:
    def __init__(self):
        self.base_url = BASE_URL

    def get(self, endpoint, headers=None):
        return requests.get(f"{self.base_url}{endpoint}", headers=headers)

    def post(self, endpoint, payload, headers=None):
        return requests.post(f"{self.base_url}{endpoint}", json=payload, headers=headers)