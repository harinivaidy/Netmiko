from netmiko import Netmiko
from pprint import pprint
from Exercise1a import device
from concurrent.futures import ProcessPoolExecutor 
from datetime import datetime


def ARP(j):
    net_conn = Netmiko(**j)
    print(net_conn.find_prompt())
    if j['device_type'] == 'juniper_junos':
        cmd = "show arp"
    else:
        cmd = "show ip arp"
    return net_conn.send_command(cmd)

def Process_pool_map():
    start_time = datetime.now()
    max_threads = 3
    
    with ProcessPoolExecutor(max_threads) as pool:
        results_generator = pool.map(ARP, device)

        for result in results_generator:
            print(result)
            end_time = datetime.now()
            print("Execution Time : {}".format(end_time - start_time))

Process_pool_map()
            
