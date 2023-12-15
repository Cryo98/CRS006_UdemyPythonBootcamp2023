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
    # print(data_manager.get_data().json())
    search = FlightSearch()
    search.set_key(os.environ.get("TEQUILA_API_KEY", ""))
    print(search.query("London").status_code)
