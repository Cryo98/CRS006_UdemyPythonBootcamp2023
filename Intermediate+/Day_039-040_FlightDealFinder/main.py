# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
import os


if __name__ == "__main__":
    load_dotenv()
    data_manager = DataManager()
    data_manager.set_authentication(os.environ.get("SHEETY_TOKEN", ""))
    data_manager.set_sheet(os.environ.get("SHEETY_URL", ""))
    data = data_manager.get_data().json()["prices"]

    search = FlightSearch()
    search.set_key(os.environ.get("TEQUILA_API_KEY", ""))
    for city_data, idx in zip(data, range(len(data))):
        iata_code = search.get_city_code(city_data["city"])
        print(data_manager.set_data(idx+1, "iataCode", iata_code).json())
    # print(search.query("London").json()["locations"][0]["code"])
    # print(search.query("Paris").json()["locations"][0]["code"])
