import requests
from datetime import datetime
import smtplib

MY_LAT = 28.704060 # Your latitude
MY_LONG = 77.102493 # Your longitude
EMAIL = "test@gmail.com"
PASSWORD = "test@123"


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    print(data)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0]) + 5
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0]) + 5

    time_now = datetime.now()
    current_hour = time_now.hour
    if current_hour < sunrise - 2 or current_hour > sunset + 2:
        return True


if is_night() and is_iss_overhead():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(to_addrs="test@gmail.com",
                            from_addr=EMAIL,
                            msg="Subject:Alert!\n\nWake up! The ISS is visible from your location.")

