import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "" ## Your API key with openweather map
MY_LAT = -35.280937 ## Replace with your Latitude
MY_LNG = 149.130005 ## Replace with your Longitude

account_sid = "" ## Twilio Messaging account ID
auth_token = "" ## Twilio API Key

def weatherForecast():
    parameters = {
        "lat": MY_LAT,
        "lon": MY_LNG,
        "appid": API_KEY,
        "cnt": 8,
    }

    response = requests.get(url=OWM_ENDPOINT, params=parameters)
    response.raise_for_status()

    data = response.json()
    print(data["list"][0]["weather"][0]["id"])

    will_rain = False

    for hour_data in data["list"]:
        condition = hour_data["weather"][0]["id"]
        if int(condition) < 700:
            will_rain = True

    if will_rain:
        client = Client(account_sid, auth_token)

        message = client.messages \
                .create(
                     from_='+', ## Your Twilio Number
                     body="It is going to rain! I would bring an umbrella",
                     to='+' ## Your verified number
                 )

        print(message.sid)
    else:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                     from_='+', ## Your Twilio Number
                     body="No rain is forecast, you are good to go!",
                     to='+' ## Your verified number
                 )

        print(message.sid)
        print(message.status)

weatherForecast()