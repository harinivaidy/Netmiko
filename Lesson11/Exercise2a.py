import requests
from pprint import pprint


url = "https://netbox.lasthop.io/api/"
response = requests.get(url, verify = False)

def Exercise2a():

    print("\n")
    print("Status Code")
    print("-"*10)
    pprint(response.status_code)
    print("\n")
    print("JSON")
    print("-"*5)
    pprint(response.json())
    print("\n")
    print("Text")
    print("-"*5)
    pprint(response.text)
    print("\n")
    print("Headers")
    print("-"*10)
    pprint(dict(response.headers))
    print("\n")

Exercise2a()
