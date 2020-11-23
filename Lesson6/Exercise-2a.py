import pyeapi
import yaml
from pprint import pprint
from getpass import getpass


f = open("Exercise2.yml")
output = yaml.load(f)
print(output)
print("\n")

ARISTA =  output['arista4']
output['arista4']['password'] = getpass()
print(ARISTA)
print("\n")

connection = pyeapi.client.connect(**ARISTA)

device = pyeapi.client.Node(connection)
print(device)

output1 = device.run_commands("show ip arp")
pprint(output1)
print("\n")
print("-"*40)

ENTRIES = output1[0]['ipV4Neighbors']

for i in ENTRIES[0:]:
    IP = i['address']
    MAC = i['hwAddress']
    print(IP,MAC)


