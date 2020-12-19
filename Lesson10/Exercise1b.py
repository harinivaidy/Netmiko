from netmiko import Netmiko
from pprint import pprint
from Exercise1a import device
from datetime import datetime

start_time = datetime.now()
print(start_time)
print("\n")


def version(*j, cmd):
        for k in device:
            net_conn = Netmiko(**k)
            print(net_conn.find_prompt())
            output = net_conn.send_command(cmd)
            print(output)
version(device, cmd = "show version")   

    
end_time = datetime.now()
print("\n")
print(end_time)
print("\n")
print("Execution Time : {}".format((datetime.now()- start_time)))
print("\n")
