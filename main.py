import requests

USERNAME = "bsaydin"
TOKEN = "treyuiyu75o0oifrjbhlj"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config={
    "id": "graph1",
    "name": "",
    "unit": "",
    "type": "",
    "color": ""

}