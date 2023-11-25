import smtplib
import datetime as dt
from pathlib import Path
import random
import configparser


# CONSTANTS
MOTIVATION_WEEKDAY = 5
QUOTES_FILE = "quotes.txt"
ACCOUNT_DATA = "email.ini"


cwd = Path(__file__).parent

config = configparser.ConfigParser()
config.read(cwd/ACCOUNT_DATA)

sender_email = config["SENDER"]["email"]
sender_password = config["SENDER"]["password"]
recipient_email = config["TEST_RECIPIENT"]["email"]

now = dt.datetime.now()
if now.weekday() == MOTIVATION_WEEKDAY:
    with open(cwd/QUOTES_FILE, "r") as f:
        quotes = f.readlines()
        quote = random.choice(quotes)
    print(f"Sending quote to {recipient_email}...")
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Encription for the connection
        connection.starttls()
        # NOTE: Need to set 2-step verification and then get an "App password" to use for this
        connection.login(user=sender_email, password=sender_password)
        message = f"Subject:{now.strftime('%A')} quote\n\n{quote}"
        print(connection.sendmail(from_addr=sender_email, to_addrs=recipient_email, msg=message))
