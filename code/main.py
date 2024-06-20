import requests
from datetime import datetime

#link: https://pixe.la/v1/users/charvisgood/graphs/graphical24.html

USERNAME = "charvisgood"
TOKEN = "fefergergeggrfrg33"
GRAPH_ID = "graphical24"

pixela_endpoint = "https://pixe.la/v1/users"
u_params = {
    "token": "fefergergeggrfrg33",
    "username": "charvisgood",
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}
#response=requests.post(url=pixela_endpoint, json=u_params)
#print(response.text)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_co = {
    "id": GRAPH_ID,
    "name": "Goal Graph",
    "unit": "Kms",
    "type": "float",
    "color": "ajisai"

}

headers = {
    "X-USER-TOKEN": TOKEN
}
#response=requests.post(url=graph_endpoint, json=graph_co, headers=headers)

#print(response.text)
pixel_crea_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime(year=2024, month=6, day=4)
print(today.strftime("%Y%m%d"))
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "145",
}
response = requests.post(url=pixel_crea_endpoint, json=pixel_data, headers=headers)

print(response.text)
