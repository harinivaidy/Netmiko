from pprint import pprint
from getpass import getpass
from my_devices import cisco3,arista1,nxos1
from napalm import get_network_driver

def conn():
    device_type3=cisco3.pop("device_type")
    driver3 = get_network_driver(device_type3)
    device3 = driver3(**cisco3)
    
    device_type1=arista1.pop("device_type")
    driver1 = get_network_driver(device_type1)
    device1 = driver1(**arista1)
    print("\n")
    return device3,device1

def nxos1_device():
    device_type2=nxos1.pop("device_type")
    driver = get_network_driver(device_type2)
    device2 = driver(**nxos1)
    return device2
