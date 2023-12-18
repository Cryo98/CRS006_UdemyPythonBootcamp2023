# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
import os


TOKENLESS = True


if __name__ == "__main__":
    load_dotenv()
    data_manager = DataManager()
    data_manager.set_authentication(os.environ.get("SHEETY_TOKEN", ""))
    data_manager.set_sheet(os.environ.get("SHEETY_URL", ""))
    if TOKENLESS:
        data = [
            {'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
            {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
            {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
            {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
            {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
            {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
            {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8},
            {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
            {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}
            ]
    else:
        data = data_manager.get_data().json()["prices"]

    search = FlightSearch()
    search.set_key(os.environ.get("TEQUILA_API_KEY", ""))

    # Set the IATA code for each city in the list if it is missing
    for city_data, idx in zip(data, range(len(data))):
        if city_data["iataCode"] == "":
            iata_code = search.get_city_code(city_data["city"])
            data[idx]["iataCode"] = iata_code
            if not TOKENLESS:
                data_manager.set_data(idx+2, "iataCode", iata_code)
