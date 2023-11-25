# AUTOMATIC BIRTHDAY WISHER
# Uses SMTP and datetime to send a mail to the contacts within a csv on the
# specified date
# -------------------------------------------------------------------------
# - [X] Load data from csv
# - [X] Start SMTP connection
# - [X] Prepare email text
# - [X] Date check to send mail

import pandas as pd
import smtplib
import datetime as dt
from pathlib import Path
import configparser
import random

# CSV containing birthdays and contacts
BIRTHDAYS_CSV = "birthdays.csv"
# Config file with credentials
ACCOUNT_DATA = "email.ini"
# Hour after which to send the email
SENDING_HOUR = 7
# List of email templates
LIST_TEMPLATES = ["Letter_1.txt", "Letter_2.txt", "Letter_3.txt"]
# Location of templates
TEMPLATED_DIR = "letter_templates"
# Name placeholder in templates
NAME_PLACEHOLDER = "[NAME]"


cwd = Path(__file__).parent

# Load credentials
config = configparser.ConfigParser()
config.read(cwd/ACCOUNT_DATA)
sender_email = config["SENDER"]["email"]
sender_password = config["SENDER"]["password"]

# Read birthdays from file
data = pd.read_csv(cwd/BIRTHDAYS_CSV, header=0)


def main():
    while True:
        is_birthday, name, email = check_date()
        if is_birthday:
            send_birthday_email(name, email)


def send_birthday_email(name: str, email: str) -> None:
    """Sends an email with text from one of the available templates

    Choses randomly between the available templates, updating the name within
    the template and sending the updated text through mail.
    Finally the last year at which the birthday email has been sent is updated
    within the dataframe.

    Parameters
    ----------
    name : str
        Name of the person receiving the email.
    email : str
        Email to which send the birthday message.
    """
    print(f"Sending email to {name}...")
    template_path = cwd/TEMPLATED_DIR/random.choice(LIST_TEMPLATES)
    with open(template_path, "r") as f:
        template = f.read()
    letter = template.replace(NAME_PLACEHOLDER, name, 1)

    with smtplib.SMTP("smtp.gmail.com") as server:
        server.starttls()
        server.login(user=sender_email, password=sender_password)
        message = f"Subject:Happy Birthday!\n\n{letter}"
        server.sendmail(from_addr=sender_email, to_addrs=email, msg=message)
        print(f"Email sent at {email}.")
    update_last_sent(name, email)


def update_last_sent(name, email):
    """Updates the last sent with the current year for the given contact."""
    idx_row = data.index[(data["name"] == name) & (data["email"] == email)][0]
    data.at[idx_row, "last_sent"] = dt.datetime.now().year
    data.to_csv(cwd/BIRTHDAYS_CSV, index=False)


def check_date() -> tuple[bool, str, str]:
    """Checks if the date is the same as the birthday.

    If the current day and month is equal to the birthdate of any of the
    contacts within the data, if the hour is after the prescribed minimum hour
    and if the last birthday message sent is not on this year, it returns a
    flag with True and the name and email of the birthday person, else it
    returns a False and empty strings.

    Returns
    -------
    tuple[bool, str, str] :
        The first is the flag if the current moment is a valid birthday moment,
        the second is the name of the birthday person, the third is their email
    """
    now = dt.datetime.now()
    for idx, row in data.iterrows():
        is_correct_month = row["month"] == now.month
        is_correct_day = row["day"] == now.day
        is_after_hour = now.hour >= SENDING_HOUR
        if row["last_sent"] == now.year:
            continue
        elif is_correct_month and is_correct_day and is_after_hour:
            return True, row["name"], row["email"]
    return False, "", ""


if __name__ == "__main__":
    main()
