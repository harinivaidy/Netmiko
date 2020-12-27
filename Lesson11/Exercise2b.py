from pprint import pprint
import requests

url = "https://netbox.lasthop.io/api/"
http_headers = {
'accept' : "application/json; version=2.4;"
}

response = requests.get(url, headers = http_headers, verify = False)

def Exercise2b():
    
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

Exercise2b()
