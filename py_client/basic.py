import requests

endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"


# Application programming interface

get_response = requests.get(endpoint, json={"query": "Hello world"}) # HTTP Request
print(get_response.json) # print raw text response

print(get_response.json())
