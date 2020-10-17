#!/usr/bin/python3

from netmiko import Netmiko
from getpass import getpass

device_list = ['cisco3.lasthop.io', 'cisco4.lasthop.io']

for i in device_list:
    print(i)
    
    device = {
        'username' : 'pyclass',
        'host': i,
        'password' : '88newclass',
        'device_type' : 'cisco_ios'
        }

       
    net_connection = Netmiko(**device)
    print(net_connection.find_prompt())
    output =  net_connection.send_command("show version")
    print(output)
    f = open("output.txt","w")
    f.write(output)
    f.close()
    print(net_connection.find_prompt())
