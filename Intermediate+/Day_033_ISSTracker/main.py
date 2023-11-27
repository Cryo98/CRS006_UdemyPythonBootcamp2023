import requests

ISS_API_ENDPOINT = "http://api.open-notify.org/iss-now.json"

response = requests.get(url=ISS_API_ENDPOINT)
response.raise_for_status()

data = response.json()["iss_position"]
print(data)
