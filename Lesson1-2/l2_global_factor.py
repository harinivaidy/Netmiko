

from netmiko import Netmiko
from getpass import getpass
import datetime

device = {

'host':'nxos1.lasthop.io',
'username':'pyclass',
'password':getpass(),
'device_type':'cisco_nxos',
'session_log':'global_factor.txt',
'global_delay_factor' :2
}

net_connection = Netmiko(**device)
print(net_connection.find_prompt())

begin_time = datetime.datetime.now()
output = net_connection.send_command("show lldp neighbors")
print(output)
print(datetime.datetime.now())
print(datetime.datetime.now() - begin_time)

begin_time = datetime.datetime.now()
output1 = net_connection.send_command("show lldp neighbors", delay_factor = 8)
print(output1)
print(datetime.datetime.now())
print(datetime.datetime.now() - begin_time)

print(net_connection.find_prompt())


