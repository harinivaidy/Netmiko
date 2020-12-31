from pprint import pprint
import requests
import json
import os

token = os.environ['NETBOX_TOKEN']

url = "https://netbox.lasthop.io/api/ipam/ip-addresses/"
print("\n")
Address_ID = input("Enter the ID that needs to be deleted : ")
http_headers = {

'Authorization' : f"Token {token}",
'Content_type' : "application/json; version=2.4;"
}

print("\n")
print("GET Requesta for a specific ID")
print("*" * 30)
response = requests.get(f"{url}{Address_ID}/", headers = http_headers, verify = False)
pprint(response.json())

print("\n")
print("DELETE IP 192.0.2.88/32")
print("*" * 20)
response1 = requests.delete(f"{url}{Address_ID}/", headers = http_headers, verify = False)

if response.ok:
    print("Device Deleted")

