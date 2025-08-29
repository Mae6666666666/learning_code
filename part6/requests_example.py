from http.client import responses

import requests

response = requests.get("https://catfact.ninja/fact")
print(response.json())