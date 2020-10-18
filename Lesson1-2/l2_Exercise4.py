from netmiko import Netmiko
from pprint import pprint
from getpass import getpass

device = {
'host':'cisco3.lasthop.io',
'username':'pyclass',
'password':'88newclass',
'device_type':'cisco_ios',
'session_log':'l2ex4.txt',
'fast_cli':True
}

net_connection = Netmiko(**device)
print(net_connection.find_prompt())

command = ('sh ip name-server')
output = net_connection.send_command(command, expect_string = "#")
command = ('ping google.com')
output +=  net_connection.send_command(command)
print(output)

config = [
'ip name-server 1.1.1.1',
'ip name-server 1.0.0.1',
'ip domain-lookup'
]

output = net_connection.send_config_set(config, strip_command=False, strip_prompt=False)
print(output)


command = ('sh ip name-server')
output = net_connection.send_command(command, expect_string = "#")
command = ('ping google.com')
output +=  net_connection.send_command(command)
print(output)
