import requests
from datetime import datetime
import os


# Your personal data. Used by Nutritionix to calculate calories.
GENDER = "male"
WEIGHT_KG = 90
HEIGHT_CM = 182
AGE = 47

# Nutritionix APP ID and API Key. Actual values are stored as environment variables.
# APP_ID = os.environ["ENV_NIX_APP_ID"]
# API_KEY = os.environ["ENV_NIX_API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"


exercise_text = input("Tell me which exercises you did: ")

# Nutritionix API Call
headers = {
    "x-app-id": "apiid",
    "x-app-key": "apikey",
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(f"Nutritionix API call: \n {result} \n")

# Adding date and time
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

# Sheety Project API. Check your Google sheet name and Sheety endpoint
GOOGLE_SHEET_NAME = "workout"
sheet_endpoint = "https://api.sheety.co/somecode/myWorkouts/workouts"

# Sheety API Call & Authentication
for exercise in result["exercises"]:
    sheet_inputs = {
        GOOGLE_SHEET_NAME: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Sheety Authentication Option 1: No Auth

    # sheet_response = requests.post(url=sheet_endpoint, json=sheet_inputs)


    # # Sheety Authentication Option 2: Basic Auth
    # sheet_response = requests.post(
    #     sheet_endpoint,
    #     json=sheet_inputs,
    #     auth=(
    #         "APIid",
    #         "APIkey",
    #     )
    # )

    # Sheety Authentication Option 3: Bearer Token
    #
    bearer_headers = {
        "Authorization": "Bearer bearerkey"
    }
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(f"Sheety Response: \n {sheet_response.text}")
