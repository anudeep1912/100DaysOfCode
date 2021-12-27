import requests
from datetime import datetime

APP_ID = "YOUR_APP_id NUTRITIONIX"      # Authentication details of your nutritionix account
APP_KEY = "YOUR_APP_KEY NUTRITIONIX"

GENDER = "male"
WEIGHT_KG = 88
HEIGHT_CM = 174
AGE = 26

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}


nutritionix_config = {
    "query": input("Please enter the workout you did: "),  # Enter your input in natural language ex: jogging for 2 hrs,
                                                           # Ran for 2 hrs and walked for 1 hour
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

response = requests.post(url=nutritionix_endpoint, json=nutritionix_config, headers=headers)
exercise_data = response.json()["exercises"]


sheety_endpoint = "YOUR SHEETY ENDPOINT"   # Please enter your sheety endpoint here

current_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%X")

headers = {
    "Authorization": "",  # Please fill your authorization details here.
}

for exercise in exercise_data:
    print(exercise)
    json_data = {
        "workout": {
            "date": current_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    response = requests.post(url=sheety_endpoint, json=json_data, headers=headers)
    response.raise_for_status()
    print("Successfully updated the your workout details to your google sheets.")


