# This file will need to use the DataManager,FlightSearch, FlightData,
# NotificationManager classes to achieve the program requirements.
from dotenv import load_dotenv
from flight_data import FlightData
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta
import os


TOKENLESS = True
IATA_FROM = "MIL"


if __name__ == "__main__":
    load_dotenv()
    data_manager = FlightData()
    data_manager.set_authentication(os.environ.get("SHEETY_TOKEN", ""))
    data_manager.set_sheet(os.environ.get("SHEETY_PRICES_URL", ""))
    if TOKENLESS:
        data = [
            {
                'city': 'Paris',
                'iataCode': 'PAR',
                'lowestPrice': 54,
                'id': 2
                },
            {
                'city': 'Berlin',
                'iataCode': 'BER',
                'lowestPrice': 42,
                'id': 3
                },
            {
                'city': 'Tokyo',
                'iataCode': 'TYO',
                'lowestPrice': 485,
                'id': 4
                },
            {
                'city': 'Sydney',
                'iataCode': 'SYD',
                'lowestPrice': 551,
                'id': 5
                },
            {
                'city': 'Istanbul',
                'iataCode': 'IST',
                'lowestPrice': 95,
                'id': 6
                },
            {
                'city': 'Kuala Lumpur',
                'iataCode': 'KUL',
                'lowestPrice': 414,
                'id': 7
                },
            {
                'city': 'New York',
                'iataCode': 'NYC',
                'lowestPrice': 240,
                'id': 8
                },
            {
                'city': 'San Francisco',
                'iataCode': 'SFO',
                'lowestPrice': 260,
                'id': 9
                },
            {
                'city': 'Cape Town',
                'iataCode': 'CPT',
                'lowestPrice': 378,
                'id': 10
                }
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
                data_manager.set_iata_code(code=iata_code, idx=idx)

    # Start notification manager
    notifier = NotificationManager(
        auth_token=os.environ.get("TWILIO_AUTH_TOKEN", ""),
        account_sid=os.environ.get("TWILIO_ACCOUNT_SID", ""),
        phone_number=os.environ.get("TWILIO_PHONE_NUMBER", ""),
        receiver_number=os.environ.get("PERSONAL_PHONE_NUMBER", "")
    )

    for city_data in data:
        print(f"Checking flights to {city_data['city']}...")
        flight_data = search.get_cheapest_flight(
            from_city_iata=IATA_FROM,
            to_city_iata=city_data["iataCode"],
            from_date=datetime.today() + timedelta(days=1),
            to_date=timedelta(weeks=25)
            )
        if flight_data["price"] > city_data["lowestPrice"]:
            print("Found a cheap flight!\n")
            search.pprint_flight_data(flight_data)
            notifier.price_alert(
                iata_departure=flight_data["flyFrom"],
                departure_city=flight_data["cityFrom"],
                iata_arrival=flight_data["flyTo"],
                arrival_city=flight_data["cityTo"],
                departure_date=datetime.fromtimestamp(flight_data['dTime']).strftime('%Y-%m-%d'),
                flight_cost=flight_data["price"]
            )
        else:
            print("No cheap flight found.")
