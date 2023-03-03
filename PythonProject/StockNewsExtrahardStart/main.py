import requests
from twilio.rest import Client
import os

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
# STOCK_API_KEY = os.environ.get("STOCK_API_KEY")
STOCK_API_KEY = "S4KVM25QXX6QI0WH"
STOCK_URL = "https://www.alphavantage.co/query"
STOCK_PARAMETERS = {
    "function" : "TIME_SERIES_DAILY_ADJUSTED",
    "symbol" : STOCK,
    "apikey": STOCK_API_KEY
}

stock_response = requests.get(url=STOCK_URL, params=STOCK_PARAMETERS)
stock_response.raise_for_status()
stock_data = stock_response.json()["Time Series (Daily)"]


# Convert dictionary to list
# two_days_slice = dict(list(stock_data.items())[1:3])
two_days_list = [value for (key, value) in stock_data.items()][1:3]

close_value_list = []
compare_close_values = -1
for day in two_days_list:
    close_value_list.append(day["4. close"])

yesterday_closing_price = float(close_value_list[0])
day_before_yesterday_closing_price = float(close_value_list[1])

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
difference_percentage = round((difference / yesterday_closing_price) * 100, 2)
CHANGE = "🤙"

if difference_percentage > 0.0:
    CHANGE = f"🔺🤙 / {difference_percentage}%"
elif difference_percentage < 0.0:
    CHANGE = f"🔻🤙 / {difference_percentage}%"
else:
    CHANGE = "🤙"


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
# NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
NEWS_API_KEY = "7a214492ea704b81a2b07ebddb04bc4c"
NEWS_URL = "https://newsapi.org/v2/everything"
NEWS_PARAMETERS = {
    "apiKey" : NEWS_API_KEY,
    "q" : COMPANY_NAME,
    "sortBy" : "popularity",
    "from" : close_value_list[0]
}

news_response = requests.get(url=NEWS_URL, params=NEWS_PARAMETERS)
news_response.raise_for_status()
news_data = news_response.json()["articles"][:3]

TWILIO_ACC_ID = "AC1a305ab447847a279048063326d49dba"
TWILIO_AUTH_TOKEN = ""

article_list = [f"{COMPANY_NAME}: {CHANGE}\nHeadline: {data['title']}\nBrief: {data['description']}" for data in news_data]

client = Client(TWILIO_ACC_ID, TWILIO_AUTH_TOKEN)
for article in article_list:
    message = client.messages.create(
        body=article,
        from_="+18777152263",
        to="5073"
    )
    print(message.status)



## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

# TWILIO_ACC_ID = os.environ.get("ACC_ID")
# TWILIO_AUTH_TOKEN = auth_token = os.environ.get("AUTH_TOKEN")
# MY_NUMBER = os.environ.get("MY_NUMBER")





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

