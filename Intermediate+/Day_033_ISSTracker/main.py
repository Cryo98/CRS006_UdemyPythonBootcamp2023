import requests
from datetime import datetime

ISS_API_ENDPOINT = "http://api.open-notify.org/iss-now.json"
SUN_API_ENDPOINT = "https://api.sunrise-sunset.org/json"
LATITUDE = "45.5"
LONGITUDE = "10"

parameters = {
    "lat": LATITUDE,
    "lng": LONGITUDE,
    "formatted": 0,
}

response_sun = requests.get(url=SUN_API_ENDPOINT, params=parameters)
response_iss = requests.get(url=ISS_API_ENDPOINT)
response_sun.raise_for_status()
response_iss.raise_for_status()

sunrise_str = response_sun.json()["results"]["sunrise"]
sunset_str = response_sun.json()["results"]["sunset"]
sunrise_dt = datetime.strptime(sunrise_str, "%Y-%m-%dT%H:%M:%S%z")
sunset_dt = datetime.strptime(sunset_str, "%Y-%m-%dT%H:%M:%S%z")
print("Sunrise:", sunrise_dt)
print("Sunset:", sunset_dt)
print(sunrise_dt < sunset_dt)
