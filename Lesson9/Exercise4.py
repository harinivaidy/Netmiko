from pprint import pprint
from getpass import getpass
from Exercise1b import nxos1_device
from napalm import get_network_driver

device = nxos1_device()
print(device)
print("\n")
device.open()

print("Load new Config")
print("-"*20)
device.load_replace_candidate("config_nxos1.txt")
print("\n")
print("Compare Config")
print("-"*20)
print(device.compare_config())
print("\n")
print("Discard Config")
print("-"*20)
device.discard_config()
print("\n")
print("Compare Config")
print("-"*20)
print(device.compare_config())



