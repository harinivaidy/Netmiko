from pprint import pprint
import requests

url = "https://netbox.lasthop.io/api/dcim/"

response = requests.get(url, verify = False)
k = response.json()
print("\n")
pprint(k)
print("\n")


