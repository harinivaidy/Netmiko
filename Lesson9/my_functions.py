from pprint import pprint
from getpass import getpass
from my_devices import device,nxos1
from Exercise1b import conn,nxos1_device
from napalm import get_network_driver

connection_objects= list(conn())
device = nxos1_device()

def create_backup(*i):
    for j in  connection_objects[0:]:
        print(j)
        print("-"*40)
        j.open()
        output1= j.get_config()
        pprint(output1)
        output2 = output1['running']
        filename = input("Enter Filename :")
        f = open(filename, 'w')
        f.write(output2)

def create_checkpoint(i):
    device.open()
    checkpoint_nxos1 = device._get_checkpoint_file()
    f = open("check_nxos1.txt", "w")
    f.write(checkpoint_nxos1)
create_checkpoint(device)
