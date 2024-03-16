import requests
import datetime

USERNAME = "yourusername"
TOKEN = "yourtoken"
TODAY = (datetime.date.today()).strftime('%Y%m%d')
pixela_endpoint = "https://pixe.la/v1/users"

# user_params = {
# 	"token": TOKEN,
# 	"username": USERNAME,
# 	"agreeTermsOfService": "yes",
# 	"notMinor": "yes"
# }

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
# 	"id": "graph1",
# 	"name": "Data Science Study",
# 	"unit": "minutes",
# 	"type": "int",
# 	"color": "sora"
# }
#
headers = {
	"X-USER-TOKEN": TOKEN
}
# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"

# pixel_config = {
# 	"date": TODAY,
# 	"quantity": "180"
# }
put_config = {
	"quantity": "180"
}
# response = requests.post(pixel_endpoint, json=pixel_config, headers=headers)
put_endpoint = f"{pixel_endpoint}/20230429"
response = requests.put(put_endpoint, json=put_config, headers=headers)
# del_endpoint = f"{pixel_endpoint}/20230429"
# response = requests.delete(del_endpoint, headers=headers)

print(response.text)
