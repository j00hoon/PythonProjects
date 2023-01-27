import requests
from twilio.rest import Client
import os


url_parameters = {
    "lat": 40.712776,
    "lon": -74.005974,
    "appid": os.environ.get("OWM_API_KEY"),
    "exclude": "current,minutely,daily"
}

account_sid = os.environ.get("ACC_ID")
auth_token = os.environ.get("AUTH_TOKEN")

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=url_parameters)
response.raise_for_status()
data = response.json()

# for _ in range(0, 12):
#     if data["hourly"][_]["weather"][0]["id"] < 700:
#         need_umbrella = True

need_umbrella = True
weather_slice = data["hourly"][:12]
for hour in weather_slice:
    if hour["weather"][0]["id"] < 700:
        need_umbrella = True
        break

if need_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Fuck you rain today.",
        from_="+18777152263",
        to=os.environ.get("MY_NUMBER")
    )

    print(message.status)

