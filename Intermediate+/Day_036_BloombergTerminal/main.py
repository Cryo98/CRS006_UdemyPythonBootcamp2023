# [X] STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day
# before yesterday then print("Get News").
# [X] STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for
# the COMPANY_NAME.
# [X] STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title
# and description to your phone number.

import os
import requests
from twilio.rest import Client
from datetime import datetime, timedelta

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# Threshold at which the message is sent
THRESHOLD = 0.005

ALPHAVANTAGE_DAILY_ENDPOINT = "https://www.alphavantage.co/query"
NEWSAPI_ENDPOINT = "https://newsapi.org/v2/everything"

alphavantage_api_key = os.environ.get("ALPHAVANTAGE_API_KEY", "")
newsapi_key = os.environ.get("NEWSAPI_KEY", "")
twilio_sid = os.environ.get("TWILIO_SID", "")
twilio_auth = os.environ.get("TWILIO_AUTH_TOKEN", "")
twilio_phone = os.environ.get("TWILIO_PHONE", "")

my_phone = os.environ.get("PERSONAL_PHONE", "")


def get_stock_variation(stock: str) -> float:
    """Gets percentual increase of last two consecutive days for the given
    stock from AlphaVantage.

    Parameters
    ----------
    stock : str
        Stock symbol

    Returns
    -------
    float
        Change in percentual
    """
    # API call
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": stock,
        "apikey": alphavantage_api_key
    }
    response = requests.get(url=ALPHAVANTAGE_DAILY_ENDPOINT, params=params)
    stock_data = response.json()

    # Get valid date-based keys for 1 day difference
    yesterday = datetime.today() - timedelta(days=1)
    while yesterday.weekday() in [0, 5, 6]:
        yesterday -= timedelta(days=1)
    before_yesterday = yesterday - timedelta(days=1)
    yesterday_key = yesterday.strftime("%Y-%m-%d")
    before_yesterday_key = before_yesterday.strftime("%Y-%m-%d")

    # Extract and calculate daily increase
    yesterday_stock = float(
        stock_data["Time Series (Daily)"][yesterday_key]["4. close"]
        )
    before_yesterday_stock = float(
        stock_data["Time Series (Daily)"][before_yesterday_key]["4. close"]
        )
    return (yesterday_stock - before_yesterday_stock)/before_yesterday_stock


def get_company_news(company):
    params = {
        "apiKey": newsapi_key,
        "q": company,
        "pageSize": 3,
    }
    response = requests.get(url=NEWSAPI_ENDPOINT, params=params)
    articles = response.json()["articles"]
    return articles


def send_message(message: str):
    """Sends a message using the twilio.rest Client

    Parameters
    ----------
    message : str
        The message to send to the phone
    """
    client = Client(twilio_sid, twilio_auth)
    message_response = client.messages.create(
        body=message,
        to=my_phone,
        from_=twilio_phone
        )
    print(message_response.status)


if __name__ == "__main__":
    increase_prc = get_stock_variation(STOCK)
    if abs(increase_prc) >= THRESHOLD:
        articles = get_company_news(COMPANY_NAME)
        message = f"{STOCK}: {'📈' if increase_prc > 0 else '📉'} "
        message += f"{'+' if increase_prc > 0 else ''}{increase_prc*100:.3f}%"
        message += "\n\n"
        for article in articles:
            message += f"\nTitle: {article['title']}\n"
            message += f"Brief: {article['description']}\n"
        send_message(message)
    print(f"{STOCK}: {'+' if increase_prc > 0 else ''}{increase_prc*100:.3f}%")
