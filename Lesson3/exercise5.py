
from pprint import pprint
import yaml
from netmiko import Netmiko

f = open("/home/harinivaidy2/.netmiko.yml")
output = yaml.load(f)
pprint(output)

print("\n")
print("Print the Dict key Value pairs for Cisco3 device")
print("^"*60)
device = output['cisco3']
pprint(device)

print("\n")
print("Connect to cisco3 using Netmiko")
print("^"*60)
ssh_connection = Netmiko(**device)
print(ssh_connection.find_prompt())

