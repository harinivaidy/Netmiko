from pprint import pprint
from getpass import getpass
from my_devices import cisco3,arista1
from napalm import get_network_driver

print("Exercise1b")
print("-"*15)
def conn():
    device_type=cisco3.pop("device_type")
    driver = get_network_driver(device_type)
    device = driver(**cisco3)
    print(device)

    return (device, None)
