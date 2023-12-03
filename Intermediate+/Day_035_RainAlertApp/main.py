# RAIN ALERT APP
# Uses an API to get the current weather and sends you a message if it forsees
# rain
# ----------------------------------------------------------------------------

from pathlib import Path
from configparser import ConfigParser
import requests
from twilio.rest import Client
import os

cwd = Path(__file__).parent

CONFIG_FILE = "config.ini"
# 5 days forecast with intervals of 3 hours
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

config = ConfigParser()
config.read(cwd/CONFIG_FILE)
# Personalization
latitude = config["PERSONAL"]["latitude"]
longitude = config["PERSONAL"]["longitude"]
my_phone = config["PERSONAL"]["phone_number"]
# OpenWeatherMap
api_key = os.environ.get("OWM_API_KEY")
# Twilio
twilio_sid = os.environ.get("TWILIO_SID")
twilio_auth = os.environ.get("TWILIO_AUTH_TOKEN")
twilio_phone = os.environ.get("TWILIO_PHONE")

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


def send_message(message):
    client = Client(twilio_sid, twilio_auth)
    message = client.messages.create(body=message, to=my_phone, from_=twilio_phone)
    print(message.status)


def main():
    weather_data = get_weather_data()
    if is_umbrella_needed(weather_data):
        print("Bring an umbrella ☔")
        send_message("Bring an umbrella ☔")
    else:
        print("No need for an umbrella today!")


if __name__ == "__main__":
    main()
