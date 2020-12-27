from pprint import pprint
import requests
import json
import os

token = os.environ['NETBOX_TOKEN']
url = "https://netbox.lasthop.io/api/ipam/ip-addresses/"

http_headers ={

"accept" : "application/json; version=2.4;",
"Authorization" : f"Token {token}"
}

response = requests.get(url, headers = http_headers, verify = False)
k = response.json()
pprint(k)
print("\n")
print("RESULTS")
print("-"*10)
RESULTS = (k['results'])
pprint(RESULTS)

for i in RESULTS:
    if i['address'] == '192.0.2.88/32':
        print("\n")
        ID = (i['id'])
        print("ID of the IP :{}".format(ID))
        break

    
url1 = "https://netbox.lasthop.io/api/ipam/ip-addresses/241/"
response1 = requests.get(url1, headers = http_headers, verify = False)

print("\n")
print("RESPONSE from the new IP Address ID")
print("-"*20)
pprint(response1.json())
print("\n")

