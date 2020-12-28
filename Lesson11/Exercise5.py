from pprint import pprint
import requests
import json
import os

token = os.environ['NETBOX_TOKEN']
url = "https://netbox.lasthop.io/api/ipam/ip-addresses/241/"

http_headers = {

"accept" : "application/json; version=2.4;",
"Authorization" : f"Token {token}",
"Content-Type" : "application/json; version=2.4;"
}

response = requests.get(url, headers = http_headers, verify = False)
print("\n")
print("Existing IP Address info for the ID")
print("-"*25)
k = response.json()
pprint(k)

put_data ={
'address' : '192.0.2.88/32',
'description' : "IP_address"
}

print("\n")
print("PUT OPERATION")
print("-"*15)
response1 = requests.put(url, headers = http_headers, data = json.dumps(put_data), verify = False)
pprint(response1.json())
print("\n")




