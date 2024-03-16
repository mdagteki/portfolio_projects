import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
ALPHA_API_KEY = "APIKEY"
NEWS_API_KEY = "NEWSAPIKEY"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = "youraccounsid"
auth_token = "yourauthorizationtoken"
my_number = "senderphonenumber"

STOCK_PARAMS = {
	"function": "GLOBAL_QUOTE",
	"symbol": STOCK_NAME,
	"datatype": "json",
	"apikey": ALPHA_API_KEY
}

NEWS_PARAMS = {
	"q": COMPANY_NAME,
	"language": "en",
	"apiKey": NEWS_API_KEY
}

response_stock = requests.get(url=STOCK_ENDPOINT, params=STOCK_PARAMS)
response_stock.raise_for_status()
stock_data = response_stock.json()
change_percent = stock_data["Global Quote"]["10. change percent"]
change_percentage = float(change_percent[0:5])

if change_percentage > 5 or change_percentage < -5:
	response_news = requests.get(url=NEWS_ENDPOINT, params=NEWS_PARAMS)
	response_news.raise_for_status()
	news_data = response_news.json()
	news_list = news_data["articles"][0:3]

	for n in range(3):
		news_title = news_list[n]["title"]
		news_description = news_list[n]["description"]
		client = Client(account_sid, auth_token)
		message = client.messages \
			.create(
			body=f"TSLA : %{change_percentage}\n ,Title :{news_title}\n ,Body: {news_description}",
			from_="senderphonenumber",
			to="recieverphonenumber"
		)
		print(message.status)

print(change_percentage)
