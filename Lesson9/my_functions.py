from pprint import pprint
from getpass import getpass
from my_devices import cisco3,arista1,nxos1
from Exercise1b import conn,nxos1_device
from napalm import get_network_driver

def create_backup():
    connection_objects1= list(conn())
    for i in  connection_objects1[0:]:
        print(i)
        print("-"*40)
        i.open()
        output1= i.get_config()
        pprint(output1)
        output2 = output1['running']
        filename = input("Enter Filename :")
        f = open(filename, 'w')
        f.write(output2)

def create_checkpoint(device2):
    device = nxos1_device()
    print(device)
    print("\n")
    device.open()
    checkpoint_nxos1 = device._get_checkpoint_file()
    f = open("check_nxos1.txt", "w")
    f.write(checkpoint_nxos1)
create_checkpoint(0)
