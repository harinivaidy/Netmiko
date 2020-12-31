from pprint import pprint
import requests

url = "https://netbox.lasthop.io/api/"

response = requests.get(f"{url}dcim/", verify = False)
k = response.json()
print("\n")
pprint(k)
print("\n")


