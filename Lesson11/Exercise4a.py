from pprint import pprint
import requests
import json
import os

token = os.environ['NETBOX_TOKEN']

url = "https://netbox.lasthop.io/api/ipam/ip-addresses/"
http_headers = {

"accept" : "application/json; version=2.4;",
"Authorization" : f"Token {token}",
"Content-Type" : "application/json; version=2.4;"
}

info = {"address": "192.0.2.88/32"}

response = requests.get(url, headers = http_headers, verify = False)
response1 = requests.post(url , headers = http_headers, data = json.dumps(info), verify = False)

print("\n")
print("GET REQUEST")
print("-"*15)
pprint(response.json())

print("\n")
print("POSTING REQUEST")
print("-"*20)
print(response1.status_code)
pprint(response1.json())

print("\n")
print("GET REQUEST")
print("-"*15)
pprint(response.json())



