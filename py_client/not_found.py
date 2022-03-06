import requests

endpoint = "http://localhost:8000/api/products/99349493493434/"

get_response = requests.get(endpoint)
print(get_response.json())