import requests
from twilio.rest import Client

endpoint = "http://api.weatherapi.com/v1/forecast.json"
api_key = "writeyourapikeyhere"
zip_code = 37174
no_days = 1
account_sid = "writeaccountsidhere"
auth_token = "writeauthorizationtokenhere"
my_number = "senderphonenumberwithcountrycode"

response = requests.get(url=f"{endpoint}?key={api_key}&q={zip_code}&days={no_days}&aqi=no&alerts=no")
response.raise_for_status()
weather_data = response.json()
rain_possibility = (weather_data["forecast"]["forecastday"][0]["day"]["daily_chance_of_rain"])
will_rain = False

if int(rain_possibility) > 50:
	will_rain = True

if will_rain:
	client = Client(account_sid, auth_token)

	message = client.messages \
		.create(
		body="Do not forget to bring an umbrella. ☂️",
		from_="senderphonenumberwithcountrycode",
		to="receiverphonenumberwithcountrycode"
	)

	print(message.status)
