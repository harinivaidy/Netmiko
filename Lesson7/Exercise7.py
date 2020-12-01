from pprint import pprint
from getpass import getpass
from nxapi_plumbing import Device
from lxml import etree

device = Device(
 
    api_format="xml",
    host = "nxos1.lasthop.io",
    username ="pyclass",
    password = getpass(),
    transport = "https",
    port = 8443,
    verify = False
)
print("Exercise - 7a")
print("-"*20)
my_xml = device.show("show interface Ethernet1/1")
pprint(my_xml)

output = etree.tostring(my_xml).decode()
pprint(output)

INT = my_xml.findall(".//interface")[0].text
STATE = my_xml.findall(".//state")[0].text
MTU = my_xml.findall(".//eth_mtu")[0].text

print("\n")
pprint("Interface: {}; State: {}; MTU: {}".format(INT, STATE, MTU))
print("\n")


print("Exercise 7b - Run the following two show commands on the nxos1 device")
print("-"*40)
cmd = ["show system uptime", "show system resources"]
for i in cmd:
    
    print(i)    
    print("-"*20)
    my_xml1 = device.show_list(i)   
    print(my_xml1)
    STRING = etree.tostring(my_xml1[0]).decode()
    print(STRING)

print("Exercise 7c - Configure Loopbacks on the nxos1 device")
print("-"*30)

cmd = ['interface Loopback 187','description Loopback187', 'interface Loopback 189', 'description Loopback188']


my_xml2 = device.config_list(cmd)
print(my_xml2)
CONFIG = etree.tostring(my_xml2[0]).decode()
print(CONFIG)








