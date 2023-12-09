# EXERCISE TRACKER
# Uses a NLP API to convert notes about daily activities into data to insert
# into an excel file.

from dotenv import load_dotenv
import requests
from datetime import datetime
import os


NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_ENDPOINT = "https://api.sheety.co/"

load_dotenv()
app_id = os.environ.get("NUTRITIONIX_APP_ID", "")
app_key = os.environ.get("NUTRITIONIX_APP_KEY", "")
sheet_token = os.environ.get("SHEETY_TOKEN", "")
sheet_url = os.environ.get("SHEETY_URL", "")


def main():
    user_input = input("What activity did you do today?\n")
    process_exercise(user_input)


def process_exercise(query: str):
    header = {
        "x-app-id": app_id,
        "x-app-key": app_key,
        "x-remote-user-id": "0"
    }
    data = {
        "query": query
    }
    response = requests.post(
        url=NUTRITIONIX_ENDPOINT,
        headers=header,
        json=data
        )
    try:
        response.raise_for_status()
        for exercise in response.json()["exercises"]:
            add_exercise_to_sheet(sheet_url, exercise)
    except requests.HTTPError:
        print("There was an error processing the activity.")
        print(f"Error <{response.status_code}>: {response.json()['message']}")


def add_exercise_to_sheet(sheet_url: str, exercise: dict):
    url = SHEETY_ENDPOINT + sheet_url
    header = {
        "Authorization": f"Bearer {sheet_token}",
        "Content-Type": "application/json"
    }
    data = {
        "workout": {
            "date": datetime.today().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime('%I:%M:%S %p'),
            "exercise": (activity_name := exercise["name"].title()),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    # This removes the weird ' before dates and times
    params = {
        "valueInputOption": "user_entered"
    }
    response = requests.post(
        url=url,
        headers=header,
        json=data,
        params=params
    )
    try:
        response.raise_for_status()
        print(f"Correctly posted the activity \"{activity_name}\".")
    except requests.HTTPError:
        print(f"There was an error with the posting of the activity \"{activity_name}\".")
        print(f"Error <{response.status_code}>: {response.json()['errors'][0]['detail']}")


if __name__ == "__main__":
    main()
