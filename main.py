import requests
from datetime import datetime

today = datetime.now()
formatted_today = today.strftime("%Y%m%d")
USERNAME = "bsaydin"
TOKEN = "treyuiyu75o0oifrjbhlj"
pixela_endpoint = "https://pixe.la/v1/users"
graph_id = "graph1"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
headers = {
    "X-USER-TOKEN": TOKEN,
}
graph_config={
    "id": graph_id,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "momiji"
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

pixel_params = {
    "date": formatted_today,
    "quantity": "100",
}
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"

#response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
#print(response.text)

update_pixel_params = {
    "quantity": "50"

}


update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{formatted_today}"
#response = requests.put(url=update_pixel_endpoint, json=update_pixel_params, headers=headers)
#print(response.text)

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{formatted_today}"
response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)