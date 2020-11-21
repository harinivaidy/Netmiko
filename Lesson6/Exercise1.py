import pyeapi
from pprint import pprint
from getpass import getpass


connection = pyeapi.client.connect(
    transport = "https",
    host = "arista3.lasthop.io",
    username="pyclass",
    password=getpass(),
    port="443",
)


#enable = getpass("Enable:")
device = pyeapi.client.Node(connection)
output = device.run_commands("show ip arp")
print(device)
print("-"*20)
pprint(output)
print("\n")
print("-"*40)
h = output[0]['ipV4Neighbors']
for i in h[0:]:
    IP = (i['address'])
    MAC = (i['hwAddress'])
    print(IP, MAC)







#arista3:
#  device_type: arista_eos
#  host: arista3.lasthop.io
#  username: pyclass
#  password: 88newclass
#  global_delay_factor: 1
