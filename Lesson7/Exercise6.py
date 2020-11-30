from pprint import pprint
from getpass import getpass
from nxapi_plumbing import Device

    
device = Device(
 
    api_format="jsonrpc",
    host = "nxos1.lasthop.io",
    username ="pyclass",
    password = getpass(),
    transport = "https",
    port = 8443,
    verify = False
)

output = device.show("show interface Ethernet1/1")
pprint(output)
STATS =  output['TABLE_interface']['ROW_interface']
print("\n")
print("Interface: {}; State: {}; MTU: {}".format(STATS['interface'], STATS['state'], STATS['eth_mtu']))
print('\n')
