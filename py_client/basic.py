import requests

endpoint = "http://127.0.0.1:8000/api/"

get_response = requests.post(endpoint, json={"title": "ABC123", "content": "Hello world", "price": 13.22})


print(get_response.json())
