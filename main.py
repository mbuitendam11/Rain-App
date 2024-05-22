import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = ""
MY_LAT = -35.280937
MY_LNG = 149.130005

account_sid = ""
auth_token = ""

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
                     from_='+',
                     body="It is going to rain! I would bring an umbrella",
                     to='+61437432481'
                 )

        print(message.sid)
    else:
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                     from_='+',
                     body="No rain is forecast, you are good to go!",
                     to='+'
                 )

        print(message.sid)
        print(message.status)

weatherForecast()