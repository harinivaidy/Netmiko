from pprint import pprint
from getpass import getpass
from my_devices import cisco3, arista1
from Exercise1b import conn
#from napalm import network_driver

my_connections = list(conn())
filename = ['cisco3.lasthop.io-loopbacks.conf', 'arista1.lasthop.io-loopbacks.conf']

for (my_file,my_device) in zip(filename[0:], my_connections[0:]):
    print("\n")
    print("Configuration File")
    print("-"*20)
    print(my_file)
    print("\n")
    print(my_device)
    my_device.open()
    my_device.load_merge_candidate(my_file)
    print("3b.Compare Config")
    print("-"*15)
    print(my_device.compare_config())
    my_device.commit_config()
    print("\n")
    print("Compare Config After Commit")
    print("-"*20)
    print(my_device.compare_config())
