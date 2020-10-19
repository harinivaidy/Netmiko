
from netmiko import Netmiko
from getpass import getpass 

devices = ['nxos1.lasthop.io', 'nxos2.lasthop.io'] 
for i in devices:

    net_device = { 
    'host':i,
    'username':'pyclass',
    'password':'88newclass',
    'device_type':'cisco_nxos',
    'session_log':'l2ex5.txt',
    }

    net_connection = Netmiko(**net_device)
    print(net_connection.find_prompt())
    
    command = "show version"
    output = net_connection.send_command(command)
    print(output)
    output1 = net_connection.send_config_from_file('vlan-exercise5.txt')
    print(output1)
    output2 = net_connection.save_config()
    print(output2)
