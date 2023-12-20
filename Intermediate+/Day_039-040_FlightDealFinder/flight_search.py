import requests
from datetime import datetime, timedelta

TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com/"


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self) -> None:
        self.api_key: str
        self.header: dict

    def set_key(self, key) -> None:
        self.api_key = key
        self.header = {"apikey": key}

    def get_city_code(self, city) -> str:
        response = self.query(term=city)
        return response.json()["locations"][0]["code"]
    
    def get_cheapest_flight(
            self,
            from_city_iata: str,
            to_city_iata: str,
            from_date: datetime = datetime.today(),
            to_date: datetime | timedelta = timedelta(weeks=4)
            ) -> dict:
        # TODO: missing check if `to_date` is before `from_date`
        # TODO: missing datatype validation
        to_date = from_date + to_date if type(to_date) is timedelta else to_date
        param = {
            "fly_from": from_city_iata,
            "fly_to": to_city_iata,
            "date_from": from_date.strftime("%d/%m/%Y"),
            "date_to": to_date.strftime("%d/%m/%Y"),
            "one_for_city": 1
        }
        response = requests.get(
            url=TEQUILA_ENDPOINT + "search",
            params=param,
            headers=self.header
            )
        return response.json()["data"][0]

    @staticmethod
    def pprint_flight_data(flight_info: dict) -> None:
        departure_city = f"{flight_info['cityFrom']}"
        arrival_city = f"{flight_info['cityTo']}"
        departure_location = f"{flight_info['cityFrom']} ({flight_info['flyFrom']})"
        arrival_location = f"{flight_info['cityTo']} ({flight_info['flyTo']})"
        departure_time = datetime.fromtimestamp(flight_info['dTime']).strftime('%Y-%m-%d %H:%M:%S')
        arrival_time = datetime.fromtimestamp(flight_info['aTime']).strftime('%Y-%m-%d %H:%M:%S')
        flight_duration = flight_info['fly_duration']
        airline_company = ', '.join(flight_info['airlines'])
        flight_cost = flight_info['price']

        print(f"{departure_city} -> {arrival_city}")
        print("============================================")
        print(f"Departure Location: {departure_location}")
        print(f"Arrival Location: {arrival_location}")
        print(f"Local Time of Departure: {departure_time}")
        print(f"Local Time of Arrival: {arrival_time}")
        print(f"Flight Duration: {flight_duration}")
        print(f"Airline Company: {airline_company}")
        print(f"Flight Cost: €{flight_cost}")
        print("============================================")

    def query(self, term) -> requests.Response:
        params = {
            "term": term,
            "location_types": "city",
            "limit": 1,
        }
        response = requests.get(
            url=TEQUILA_ENDPOINT + "locations/query",
            params=params,
            headers=self.header
            )
        return response
