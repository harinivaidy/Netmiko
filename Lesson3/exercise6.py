
from netmiko import Netmiko
import yaml
from pprint import pprint
from ciscoconfparse import CiscoConfParse

f = open("/home/harinivaidy2/.netmiko.yml")
output = yaml.load(f)
pprint(output)

print("\n")
print("Retrieve Device information for Cisco4")
print("^"*50)
device = output['cisco4']
pprint(device)

print("\n")
print("Connecting to a device via SSH")
print("^"*50)
ssh_connection = Netmiko(**device)
print(ssh_connection.find_prompt)
output1 = ssh_connection.send_command("show running ")
print(output1)

j = open("sh_run_cisco4.txt", "w")
j.write(output1)

#print("\n")
#Object = CiscoConfParse("sh_run_cisco4.txt")
#print(Object)
#print("\n")
#
#print("Interface Line: {}".format(Object.find_objects_w_child(r"^interface", r"^\sip")[0].text))
#print("IP Address Line: {}".format(Object.find_objects_w_child(r"^interface", r"^\sip")[0].children))


