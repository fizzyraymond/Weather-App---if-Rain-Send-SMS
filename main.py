import requests
from twilio.rest import Client
import os

owm_endpoint = "http://api.openweathermap.org/data/2.5/forecast"
api_key = "apikey"
my_lat=33.684422
my_long=73.047882
# TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
# TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')


weather_params={
    "lat": 33.684422,
    "lon": 73.047882,
    "appid":api_key,
    "cnt": 4 #number of timestamps to retreive
}
response = requests.get(owm_endpoint, params = weather_params)
print(response.status_code)
response.raise_for_status()
weather_data=(response.json())
# print(weather_data) 

# Check the weather condition codes for the next 12 hours
bring_umbrella = False
for hour_data in weather_data["list"]:
    weather_condition_code = hour_data["weather"][0]["id"]
    if weather_condition_code < 700:
        bring_umbrella = True
        break

if bring_umbrella:
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    message = client.messages \
        .create(
        body="Bring an Umbrella!",
        from_='+17259990749',
        to='+923175431116')
    print(message.status)