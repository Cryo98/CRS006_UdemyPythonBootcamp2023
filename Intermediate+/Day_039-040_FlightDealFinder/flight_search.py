import requests

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.api_key = ""
        self.header = ""

    def set_key(self, key) -> None:
        self.api_key = key
        self.header = {"apikey": key}

    def query(self, term) -> requests.Response:
        params = {
            "term": term,
            "location_types": "city",
            "limit": 1,
        }
        response = requests.get(url=TEQUILA_ENDPOINT, params=params, headers=self.header)
        return response
