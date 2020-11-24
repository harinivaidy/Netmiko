from pprint import pprint
from getpass import getpass
from my_func import func1
import pyeapi

Koke = func1()
pprint(Koke)

ARISTA =  Koke['arista4']
pprint(ARISTA)
 
Koke['arista4']['password'] = getpass()
print("\n")
 
connection = pyeapi.client.connect(**ARISTA)
  
device = pyeapi.client.Node(connection)
print(device)

output = device.run_commands("show ip route")
pprint(output)
print("\n")

struct = output[0]['vrfs']['default']['routes']
print("\n")

for i,v in struct.items():
    pprint("{} --> {}".format(i,v['routeType']))
    if v['directlyConnected'] is False:
        vias = (v['vias'][0]['nexthopAddr'])
        print("Next Hop is {}".format(vias))
