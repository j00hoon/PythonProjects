import requests
import smtplib
import datetime as dt
import time


MY_EMAIL = "j00hoon1101@gmail.com"
PASSWORD = "btpygqgeztdqczhl"
MY_LAT = 40.712776
MY_LONG = -74.005974


def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])

    return (latitude, longitude)


def is_after_sunset():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    # response = requests.get(url=f"https://api.sunrise-sunset.org/json?{MY_LAT}&{MY_LONG}&formatted=0")
    response = requests.get(url=f"https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"]
    sunset = data["results"]["sunset"]
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])

    today = dt.datetime.now()
    current_hour = today.hour
    print(f"{current_hour}   {sunset_hour}    {sunrise_hour}")

    # check if it is dark or not
    if sunset_hour <= current_hour or current_hour <= sunrise_hour:
        print("dark")
        return True
    else:
        return False


def is_iss_position_overhead(iss_position):
    global MY_LAT, MY_LONG
    if (MY_LAT - 5 <= iss_position[0] <= MY_LAT + 5) and (MY_LONG - 5 <= iss_position[1] <= MY_LONG[1] + 5): # check latitude and longitude +- 5 would be okay
        return True
    else:
        return False


def send_email():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="j00hoon1101@gmail.com",
            msg="Subject:ISS comin look up!\n\nYou horse shit look up!"
        )


def whereis_iss():
    iss_position = get_iss_position()

    # check iss is located on my head
    # check if it is after sunset
    if is_iss_position_overhead(iss_position) and is_after_sunset():
        send_email()


while True:
    time.sleep(60)
    whereis_iss()

