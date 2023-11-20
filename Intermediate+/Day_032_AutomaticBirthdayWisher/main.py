# AUTOMATIC BIRTHDAY WISHER
# Uses SMTP and datetime to send an automatic email with birthday wishes

import smtplib


# CONSTANTS
MY_EMAIL = "test1@gmail.com"
TEST_EMAIL = "test2@gmail.com"
PASS = "this_is_a_fake_password"

connection = smtplib.SMTP("smtp.gmail.com")
# Encription for the connection
connection.starttls()
# NOTE: Need to set 2-step verification and then get an "App password" to use for this
connection.login(user=MY_EMAIL, password=PASS)
# connection.sendmail(from_addr=MY_EMAIL, to_addrs=TEST_EMAIL, msg="Test")
connection.close()
