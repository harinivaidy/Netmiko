from jinja2 import FileSystemLoader
from jinja2.environment import Environment
from netmiko import Netmiko
from pprint import pprint
import re


env = Environment()
env.loader =  FileSystemLoader('.')


my_vars = {

    'Interface1':'Ethernet1/4',
    'IP_Address1':'10.1.100.1',
    'Interface2':'Ethernet1/4',
    'IP_Address2':'10.1.100.2',
    'netmask':24,
    'neighbor_Ip1':'10.1.100.2',
    'neighbor_Ip2':'10.1.100.1',
    'AS_number':22

    }

template = env.get_template("Exercise2b.j2")
output = template.render(**my_vars)
print("Generating Template file")
print('$'*25)
pprint(output)

print("Splitting Config for nxos1 from template")
print("^"*35)
nxos1_config = re.search("^##nxos1.*#",output,re.S).group(0)
pprint(nxos1_config) 

print("Splitting Config for nxos2 from template")
print("^"*35)
nxos2_config = re.search("^##nxos2.*$",output,re.S|re.M).group(0)
pprint(nxos2_config)

print("Logging into NXOS devices")
print("-"*25)
from my_devices_exercise2c import nxos1,nxos2

try: 
    ssh_connection1 = Netmiko(**nxos1)
    output1 = ssh_connection1.send_config_set(nxos1_config, cmd_verify = False)
    print(output1)
    output1 += ssh_connection1.exit_config_mode()
    pprint(output1)
except ValueError:
    print("Value Error Occured")
    ssh_connection2 = Netmiko(**nxos2)
    output2 = ssh_connection2.send_config_set(nxos2_config, cmd_verify = False)
    pprint(output2)
except ValueError:
    print("Value Error Occured")
    output3 = ssh_connection1.send_command_timing("show bgp sessions")
    output4 = ssh_connection2.send_command_timing("ping 10.1.100.1")
#    print(output3)
 #   print(output4)
#
#
#
#
#
#


