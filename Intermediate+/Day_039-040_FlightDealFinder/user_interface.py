import requests
import os
from dotenv import load_dotenv

load_dotenv()
SHEETY_ENDPOINT = "https://api.sheety.co/"


def register_user(user_name: str, user_surname: str, user_email: str):
    url = SHEETY_ENDPOINT + os.environ.get("SHEETY_USERS_URL", "")
    header = {
        "Authorization": f"Bearer {os.environ.get('SHEETY_TOKEN', '')}",
        "Content-Type": "application/json"
        }
    body = {
        "user": {
            "name": user_name,
            "surname": user_surname,
            "email": user_email,
        }
    }
    response = requests.post(url=url, headers=header, json=body)
    response.raise_for_status()
    print(response.content)


print("Welcome to Alessandro's Flight Deals")
print("We find the best flight deals and email you.")
user_email = ""
user_email_confirmation = "0"
while user_email != user_email_confirmation:
    user_name = input("What is your first name?\n")
    user_surname = input("What is your last name?\n")
    user_email = input("What is your email?\n")
    user_email_confirmation = input("Type your email again.\n")
    if user_email == user_email_confirmation:
        print("You are in the club!")
        register_user(user_name, user_surname, user_email)
        break
    else:
        print("Your email doesn't match. Please try again.")
