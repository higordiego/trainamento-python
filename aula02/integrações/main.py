import requests

url = "https://viacep.com.br/ws/01001000/json/"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
