from netmiko import Netmiko
from pprint import pprint
from getpass import getpass

nxos1 = {
        'host': 'nxos1.lasthop.io',
        'device_type':'cisco_nxos',
        'username': 'pyclass',
        'password': getpass(),
        'session_log':'nxos1.txt'
    }

nxos2 = {
            
        'host': 'nxos2.lasthop.io',
        'device_type':'cisco_nxos',
        'username': 'pyclass',
        'password': getpass(),
        'session_log':'nxos2.txt'

    }

for i in (nxos1,nxos2):

    ssh_connection = Netmiko(**i)
    print(ssh_connection.find_prompt())
    ssh_connection.disconnect()
