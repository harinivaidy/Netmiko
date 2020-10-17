from netmiko import Netmiko
from getpass import getpass

device = {

'host':'cisco4.lasthop.io',
'username':'pyclass',
'password':getpass(),
'device_type':'cisco_ios',
'session_log':'ping1b.txt'

}

net_connection = Netmiko(**device)
print(net_connection.find_prompt())

output = net_connection.send_command("ping", expect_string=":", strip_prompt = False, strip_command = False)
output1= net_connection.send_command("\n", expect_string=":", strip_prompt = False, strip_command = False)
output2= net_connection.send_command("8.8.8.8", expect_string=":", strip_prompt = False, strip_command = False)
output3 = net_connection.send_command('\n', expect_string=":", strip_prompt = False, strip_command = False)
output4 = net_connection.send_command('\n', expect_string=":", strip_prompt = False, strip_command = False)
output5 = net_connection.send_command('\n', expect_string=":", strip_prompt = False, strip_command = False)
output6 = net_connection.send_command('\n', strip_prompt = False, strip_command = False)
print(output)
print(output1)
print(output2)
print(output3)
print(output4)
print(output5)
#print(output6)
print(net_connection.find_prompt())
