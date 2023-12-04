STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## [ ] STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

## [ ] STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## [ ] STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

import os
import requests
from datetime import datetime, timedelta

ALPHAVANTAGE_DAILY_ENDPOINT = "https://www.alphavantage.co/query"

alphavantage_api_key = os.environ["ALPHAVANTAGE_API_KEY"]


def get_stock_variation(stock):
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
    yesterday_stock = float(stock_data["Time Series (Daily)"][yesterday_key]["4. close"])
    before_yesterday_stock = float(stock_data["Time Series (Daily)"][before_yesterday_key]["4. close"])
    return (yesterday_stock - before_yesterday_stock)/before_yesterday_stock


if __name__ == "__main__":
    increase_prc = get_stock_variation(STOCK)
    if increase_prc >= 0.05 or increase_prc <= -0.05:
        print("Get news.")
    print(f"{STOCK}: {'+' if increase_prc > 0 else ''}{increase_prc*100:.3f}%")
