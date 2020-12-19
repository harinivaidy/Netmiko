from pprint import pprint
from getpass import getpass
from my_functions import create_backup,connection_objects
from Exercise1b import conn

pprint(connection_objects)

def arp_ntp():

    for i in connection_objects[0:]:
        print(i)
        print("-"*40)
        i.open()
        output = i.get_arp_table()
        pprint(output)
        print("\n")
        try:
            print("GET NTP PEERS")
            print("-"*15)
            output1 = i.get_ntp_peers()
            print(output1)
            print("\n")
        except NotImplementedError:
            print("Exception Raised")
            print("\n")


def main():
 
    arp_ntp()
    print("\n")
    print("Creating Backup")
    print("-"*20)
    create_backup(connection_objects)

main()

