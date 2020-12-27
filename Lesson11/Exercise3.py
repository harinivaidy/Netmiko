from pprint import pprint
import requests
import os

token = os.environ["NETBOX_TOKEN"]
url = "https://netbox.lasthop.io/api/dcim/devices/"
http_headers = {
'Authorization' : f'Token {token}',
'accept' : "application/json; version=2.4;"
}
response = requests.get(url, headers = http_headers, verify = False)
k = response.json()

print("\n")
print("Exercise 3a")
print("Response in JSON")
print("-"*20)
pprint(k)
print("\n")

print("Results")
print("-"*10)
RESULTS = k['results']
pprint(RESULTS)
print("\n")

print("Display Names")
print("-" * 15)
for i in RESULTS:
    print(i['display_name'])

print("\n")
print("Exercise 3b")

for i in RESULTS:
    print("-"*30)
    print(i['display_name'])
    print("-"*10)
    print("Location : {}".format(i['site']['name']))
    print("Vendor : {}".format(i['device_type']['manufacturer']['name']))
    print("Status : {}".format(i['status']['label']))
    print("\n")


