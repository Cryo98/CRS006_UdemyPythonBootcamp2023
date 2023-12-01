# RAIN ALERT APP
# Uses an API to get the current weather and sends you a message if it forsees
# rain
# ----------------------------------------------------------------------------

from pathlib import Path
from configparser import ConfigParser
import requests

cwd = Path(__file__).parent

CONFIG_FILE = "config.ini"
# 5 days forecast with intervals of 3 hours
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
# current weather
# API_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"

config = ConfigParser()
config.read(cwd/CONFIG_FILE)
latitude = config["LOCATION"]["latitude"]
longitude = config["LOCATION"]["longitude"]
api_key = config["OPENWEATHER"]["api_key"]

params = {
    "lat": latitude,
    "lon": longitude,
    "appid": api_key,
    "units": "metric",
    # Number of values to return
    "cnt": 4,
}


def get_weather_data():
    response = requests.get(url=API_ENDPOINT, params=params)
    response.raise_for_status()
    return response.json()


def is_umbrella_needed(weather_data):
    for forecast in weather_data["list"]:
        if forecast["weather"][0]["id"] < 700:
            return True
    return False


def main():
    weather_data = get_weather_data()
    if is_umbrella_needed(weather_data):
        print("Bring an umbrella ☔")
    else:
        print("No need for an umbrella today!")


if __name__ == "__main__":
    main()
