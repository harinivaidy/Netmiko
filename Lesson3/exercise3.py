from pprint import pprint
import json

ipv4 =[]
ipv6 = []

f = open("exercise3.json")
output= f.read()
print("Printing JSON file")
print(output)

f=open("exercise3.json")
output1 = json.load(f)
print("Printing python format")
pprint(output1)

for i in output1.values():
    try:
        ipv4.append(i['ipv4'])
    except KeyError:
        print()
    try:
        ipv6.append(i['ipv6'])
    except KeyError:
        print()
    
print("\n")
print("Ipv4 addresses")
print("^"*60)
pprint(ipv4)


print("\n")
print("Ipv6 addresses")
print("*"*60)
pprint(ipv6)


