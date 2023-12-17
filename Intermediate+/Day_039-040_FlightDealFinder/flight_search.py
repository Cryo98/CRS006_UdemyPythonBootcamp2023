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

    def get_city_code(self, city) -> str:
        response = self.query(term=city)
        return response.json()["locations"][0]["code"]

    def query(self, term) -> requests.Response:
        params = {
            "term": term,
            "location_types": "city",
            "limit": 1,
        }
        response = requests.get(url=TEQUILA_ENDPOINT + "locations/query", params=params, headers=self.header)
        return response
