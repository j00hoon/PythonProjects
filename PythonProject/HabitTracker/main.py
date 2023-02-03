import requests
from datetime import datetime

USERNAME = "j00hoon1101"
TOKEN = "qortmdgnsabc"
GRAPH_ID = "graph1"





# Create a user
pixela_url = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# response = requests.post(url=pixela_url, json=user_params)
# print(response.text)









# Create a graph
pixela_graph_url = f"{pixela_url}/{USERNAME}/graphs"

graph_body = {
    "id": GRAPH_ID,
    "name": "Seunghoon graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN.encode('utf-8')
}
# response = requests.post(url=pixela_graph_url, json=graph_body, headers=headers)
# print(response.text)










# Create a pixel
pixela_pixel_url = f"{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}"
date = datetime(year=2023, month=2, day=1).strftime("%Y%m%d")

create_pixel_body = {
    "date": date,
    "quantity": "5"
}
# response = requests.post(url=pixela_pixel_url, json=create_pixel_body, headers=headers)
# print(response.text)








# Update a pixel
pixela_update_pixel_url = f"{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

update_pixel_body = {
    "quantity": "15"
}
# response = requests.put(url=pixela_update_pixel_url, json=update_pixel_body, headers=headers)
# print(response.text)





# Delete a pixel
pixela_delete_pixel_url = f"{pixela_url}/{USERNAME}/graphs/{GRAPH_ID}/{date}"

response = requests.delete(url=pixela_delete_pixel_url, headers=headers)
print(response.text)

