# AUTOMATIC BIRTHDAY WISHER
# Uses SMTP and datetime to send a mail to the contacts within a csv on the
# specified date
# -------------------------------------------------------------------------
# - [X] Load data from csv
# - [X] Start SMTP connection
# - [ ] Prepare email text
# - [ ] Date check to send mail

import pandas as pd
import smtplib
import datetime as dt
from pathlib import Path
import configparser

# CSV containing birthdays and contacts
BIRTHDAYS_CSV = "birthdays.csv"
ACCOUNT_DATA = "email.ini"

cwd = Path(__file__).parent

# Load credentials
config = configparser.ConfigParser()
config.read(cwd/ACCOUNT_DATA)
sender_email = config["SENDER"]["email"]
sender_password = config["SENDER"]["password"]

# Read birthdays from file
data = pd.read_csv(cwd/BIRTHDAYS_CSV, header=0)

with smtplib.SMTP("smtp.gmail.com") as server:
    server.starttls()
    server.login(user=sender_email, password=sender_password)
