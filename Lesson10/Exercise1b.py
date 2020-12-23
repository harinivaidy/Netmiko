from netmiko import Netmiko
from pprint import pprint
from Exercise1a import device
from datetime import datetime

start_time = datetime.now()
print(start_time)
print("\n")

cmd = "show version"

for i in device:
    print("#" * 80)
    net_connection = Netmiko(**i)
    print(net_connection.find_prompt())
    output = net_connection.send_command(cmd)
    net_connection.disconnect()
    print(output)
    print("#" * 80)

end_time = datetime.now()
print("\n")
print(end_time)
print("\n")
print("Execution Time : {}".format((datetime.now()- start_time)))
print("\n")


    
