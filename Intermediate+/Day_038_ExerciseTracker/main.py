# EXERCISE TRACKER
# Uses a NLP API to convert notes about daily activities into data to insert
# into an excel file.

from configparser import ConfigParser
from pathlib import Path
import requests


NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

config = ConfigParser()
config.read(Path(__file__).parent/"config.ini")
app_id = config["NUTRITIONIX"]["app_id"]
app_key = config["NUTRITIONIX"]["app_key"]


def main():
    process_exercise("Ran for 5 km at slow pace")


def process_exercise(query: str):
    header = {
        "x-app-id": app_id,
        "x-app-key": app_key,
        "x-remote-user-id": "0"
    }
    data = {
        "query": query
    }
    response = requests.post(url=NUTRITIONIX_ENDPOINT, headers=header, json=data)
    print(response.content)


if __name__ == "__main__":
    main()
