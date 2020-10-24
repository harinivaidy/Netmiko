from pprint import pprint
import json

f = open("exercise3.json")
output= f.read()
print("Printing JSON file")
print(output)

f=open("exercise3.json")
output1 = json.load(f)
print("Printing python format")
pprint(output1)

IP1_v4 = (output1['Ethernet2/1']['ipv4'])
print(IP1_v4)
IP2_v4 = (output1['Ethernet2/2']['ipv4'])
print(IP2_v4)
IP3_v4 = (output1['Ethernet2/3']['ipv4'])
print(IP3_v4)

IP1_v6 = (output1['Ethernet2/3']['ipv6'])
print(IP1_v6)
IP2_v6 = (output1['Ethernet2/4']['ipv6'])
print(IP2_v6)

ipv4 = []
ipv6 = []

ipv4.append(IP1_v4)
ipv4.append(IP2_v4)
ipv4.append(IP3_v4)
print("\n")
print("Ipv4 addresses")
print("^"*60)
pprint(ipv4)

ipv6.append(IP1_v6)
ipv6.append(IP2_v6)

print("\n")
print("Ipv6 addresses")
print("*"*60)
pprint(ipv6)


