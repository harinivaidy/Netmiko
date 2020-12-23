from pprint import pprint
from Exercise1a import device
from netmiko import Netmiko

def ssh_command(j, cmd = "show version"):
    print("#" * 80)
    net_conn = Netmiko(**j)
    print(net_conn.find_prompt())
    output = net_conn.send_command(cmd)
    net_conn.disconnect()
    print(output)    
    print("#" * 80)
    return output


def ssh_command2(j, cmd = "show version"):
    print("#" * 80)
    net_conn = Netmiko(**j)
    output = net_conn.send_command(cmd)
    net_conn.disconnect()
    print("#" * 80)
    return output
