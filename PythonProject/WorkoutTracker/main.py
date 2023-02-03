import requests
from datetime import datetime
import os

# APP_ID = "f2e208c8"
# API_KEY = "85a05f858ddcaba9838464a3ee34e80f"
# GENDER = "male"
# WEIGHT_KG = 78
# HEIGHT_CM = 178
# AGE = 32
# BEARER_TOKEN = "Bearer 12390zxcknm90230%2BuSeid%2BULvsea4JtiGRiSDSJSIasljkdnasldknasdlkn76ZC9Ub0wnz4XsNiRVBChTYbJcE3F"

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
GENDER = os.environ["GENDER"]
WEIGHT_KG = os.environ["WEIGHT_KG"]
HEIGHT_CM = os.environ["HEIGHT_CM"]
AGE = os.environ["AGE"]
BEARER_TOKEN = os.environ["BEARER_TOKEN"]

# Which exercises?
exercise_input = input("Which exercise you did? ")

# Calories?
nutritionix_exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"
nutritionix_body = {
    "query": exercise_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=nutritionix_exercise_url, json=nutritionix_body, headers=nutritionix_headers)
result = response.json()["exercises"]
# response.raise_for_status()




# Add to google sheet
workout_url = "https://api.sheety.co/714305910239e5787bf0d55849d16ac1/trackingMyWorkout/workouts"
time = datetime.now().strftime("%H:%M:%S")
date = datetime.now().strftime("%m/%d/%Y")
for index in range(0, len(result)):
    workout_body = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": result[index]["user_input"],
            "duration": result[index]["duration_min"],
            "calories": result[index]["nf_calories"]
        }
    }
    workout_header = {
        "Authorization": BEARER_TOKEN
    }
    response = requests.post(url=workout_url, json=workout_body, headers=workout_header)
    print(response.text)






