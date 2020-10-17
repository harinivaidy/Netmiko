

from netmiko import Netmiko
from getpass import getpass

device ={

    'host':'cisco4.lasthop.io',
    'username' :'pyclass',
    'password':getpass(),
    'device_type':'cisco_ios'

    }

net_connection = Netmiko(**device)
print(net_connection.find_prompt())

command1 = "show lldp neighbors"
command2 = "show version"
output1 = net_connection.send_command(command1, use_textfsm=True)
output2 = net_connection.send_command(command2)
print(output1)
print(type(output1))
print("-"*150)
print(output2)
print("-"*150)
j = list(output1[0].values())[3]
print(j)
print(net_connection.find_prompt())

