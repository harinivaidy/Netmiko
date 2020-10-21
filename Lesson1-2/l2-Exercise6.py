

from netmiko import Netmiko
from getpass import getpass
import time

password = getpass()
device = {
    "host": "cisco4.lasthop.io",
    "username": "pyclass",
    "password": password,
    "secret": password,
    "device_type": "cisco_ios",
    "session_log": "my_output_l2-ex6.txt",
}


net_connection = Netmiko(**device)
print(net_connection.find_prompt())

net_connection.config_mode()
print(net_connection.find_prompt())
net_connection.exit_config_mode()
print(net_connection.find_prompt())

net_connection.write_channel("disable\n")
time.sleep(2)
output = net_connection.read_channel()
print(output)

print("Enter enable mode")
net_connection.enable()
print(net_connection.find_prompt())

net_connection.disconnect()
print()

