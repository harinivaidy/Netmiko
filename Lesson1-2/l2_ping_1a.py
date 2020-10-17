from netmiko import Netmiko
from getpass import getpass

device = {

'host':'cisco4.lasthop.io',
'username':'pyclass',
'password':getpass(),
'device_type':'cisco_ios',
'session_log':'ping1a.txt',
}

net_connection = Netmiko(**device)
print(net_connection.find_prompt())

output = net_connection.send_command_timing("ping")
output1 = net_connection.send_command_timing("\n")
output2 = net_connection.send_command_timing('8.8.8.8', strip_prompt = False, strip_command = False)
output3 = net_connection.send_command_timing("\n")
output4 = net_connection.send_command_timing("\n")
output5 = net_connection.send_command_timing("\n")
output6 = net_connection.send_command_timing('\n', strip_prompt = False, strip_command = False)
print(output)
print(output1)
print(output2)
print(output3)
print(output4)
print(output5)
print(output6)
print(net_connection.find_prompt())


