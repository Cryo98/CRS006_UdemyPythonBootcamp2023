# ISS TRACKER
# This script gets using an API the current sunrise/sunset time, the ISS
# position, and sends an email if the ISS might be visible

import requests
from datetime import datetime
import smtplib
from configparser import ConfigParser
from pathlib import Path
from time import sleep

# API endpoints
ISS_API_ENDPOINT = "http://api.open-notify.org/iss-now.json"
SUN_API_ENDPOINT = "https://api.sunrise-sunset.org/json"
# Personal info location
CONFIG_PATH = "config.ini"
# Angular range within which the notice is sent
ANGLE_RANGE = 5.0
# Delays in seconds
CHECK_TIME_DELAY = 60
CHECK_ISS_DELAY = 60
NOTIFICATION_DELAY = 60

cwd = Path(__file__).parent
config = ConfigParser()
config.read(cwd/CONFIG_PATH)
# Coordinates to be used for current location
latitude = config.getfloat("LOCATION", "latitude")
longitude = config.getfloat("LOCATION", "longitude")
# Email stuff
recipient_email = config["EMAIL"]["recipient_email"]
sending_email = config["EMAIL"]["sending_email"]
password = config["EMAIL"]["sending_password"]

# Parameters used to retrieve the local sunrise and sunset
parameters = {
    "lat": latitude,
    "lng": longitude,
    "formatted": 0,
}


def is_currently_night() -> bool:
    """Evaluates if the current time is during the night.

    Returns
    -------
    bool
        True if the current time is not within the sunrise and sunset, else
        False
    """
    # Get API response
    response_sun = requests.get(url=SUN_API_ENDPOINT, params=parameters)
    response_sun.raise_for_status()
    # Convert to local timezone
    sunrise_str = response_sun.json()["results"]["sunrise"]
    sunset_str = response_sun.json()["results"]["sunset"]
    sunrise_utc = datetime.strptime(sunrise_str, "%Y-%m-%dT%H:%M:%S%z")
    sunset_utc = datetime.strptime(sunset_str, "%Y-%m-%dT%H:%M:%S%z")
    # Compare current time to sunrise/sunset
    sunrise_time_local = sunrise_utc.astimezone().time()
    sunset_time_local = sunset_utc.astimezone().time()
    current_time_local = datetime.now().time()

    return not (sunrise_time_local < current_time_local < sunset_time_local)


def get_iss_location() -> tuple[float, float]:
    """Obtains from an API the current location in geographic coordinates of
    the ISS

    Returns
    -------
    tuple[float, float]
        Tuple containing latitude and longitude of the ISS's position.
    """
    # Get API response
    response_iss = requests.get(url=ISS_API_ENDPOINT)
    response_iss.raise_for_status()
    # Extract latitude and longitude
    latitude = float(response_iss.json()["iss_position"]["latitude"])
    longitude = float(response_iss.json()["iss_position"]["longitude"])

    return (latitude, longitude)


def is_object_close(
        your_position: tuple[float, float],
        obj_position: tuple[float, float],
        ) -> bool:
    """
    Determine if an object is within a specified angle range of your current
    position.

    This function checks whether the latitude and longitude of an object's
    position fall within a defined angular range from your current latitude
    and longitude.
    The ANGLE_RANGE constant defines the allowable range.

    Parameters
    ----------
    your_position : tuple[float, float]
        A tuple representing your current position, where the first element is
        the latitude and the second element is the longitude.
    obj_position : tuple[float, float]
        A tuple representing the object's position, where the first element is
        the latitude and the second element is the longitude.

    Returns
    -------
    bool
        Returns True if the object is within the angle range of your position,
        otherwise returns False.
    """
    obj_lat = obj_position[0]
    obj_lng = obj_position[1]
    max_lat = your_position[0] + ANGLE_RANGE
    min_lat = your_position[0] - ANGLE_RANGE
    max_lng = your_position[1] + ANGLE_RANGE
    min_lng = your_position[1] - ANGLE_RANGE
    return (min_lat < obj_lat < max_lat) and (min_lng < obj_lng < max_lng)


def send_notification(iss_position: tuple[float, float]):
    """
    Sends an email notification about the current position of the
    International Space Station (ISS).

    This function prepares an email message indicating that the ISS is
    currently passing nearby the recipient's location. It includes the current
    time and the latitude and longitude of the ISS. The function then opens a
    transmission channel using SMTP to send this message to a predefined
    recipient.

    Parameters
    ----------
    iss_position : tuple[float, float]
        A tuple representing the current position of the ISS, where the first
        element is the latitude and the second element is the longitude.
    """
    # Preparing message
    header = "Subject:ISS overhead!\n\n"
    current_time = datetime.now()
    message = "The ISS is currently passing nearby your location!\n"
    message += f"Its position at time {current_time.strftime('%H:%M:%S')}:\n"
    message += f"\tLatitude: {iss_position[0]}\n"
    message += f"\tLongitude: {iss_position[1]}\n"

    # Opening transmission channel
    with smtplib.SMTP("smtp.gmail.com") as server:
        server.starttls()
        server.login(user=sending_email, password=password)
        server.sendmail(
            from_addr=sending_email,
            to_addrs=recipient_email,
            msg=header+message)

    print("Notification sent!")


def main():
    while True:
        is_night = is_currently_night()
        if not is_night:
            sleep(CHECK_TIME_DELAY)
            continue
        iss_position = get_iss_location()
        while is_object_close((latitude, longitude), iss_position):
            send_notification(iss_position)
            sleep(NOTIFICATION_DELAY)
        sleep(CHECK_ISS_DELAY)


if __name__ == "__main__":
    main()
