import requests
from twilio.rest import Client

# Api key and Lat and Long of a location.
LATITUDE = 51.50
LONGITUDE = -0.12
api_key_open_weather_map = ""
# Twilio credentials
twilio_sid = ""
twilio_auth = ""


def is_rainy():
    """Checks the whether and returns true if there is rain in next 12 hours."""
    parameters = {
        "lat": LATITUDE,
        "lon": LONGITUDE,
        "appid": api_key_open_weather_map,
        "exclude": "current,daily,minutely"
    }
    response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall", params=parameters)
    response.raise_for_status()
    weather_data = response.json()
    for hourly_data in weather_data["hourly"][:12]:
        weather_id = hourly_data["weather"][0]["id"]
        if weather_id < 700:
            return True

# If it's gonna rain in next 12 hours text SMS will be send to your number.
if is_rainy():
    client = Client(twilio_sid, twilio_auth)
    message = client.messages \
        .create(
            body="Its gonna rain today. Please take an Umbrella",
            from_="+13166616433",
            to=''
        )
    print(message.status)