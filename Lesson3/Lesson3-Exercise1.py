from pprint import pprint

f = open("arp-exercise1.txt")
output = f.readlines()
pprint(output)


new_list = []
print("*"*60)

for element in output[1:]:
    mac_addr=element.split()[3]
    ip_addr=element.split()[1]
    interface=element.split()[5]
    print(element)
    print(mac_addr)
    print(ip_addr)
    print(interface)

    element_dict= {
    'mac_addr':mac_addr,
    'ip_addr':ip_addr,
    'interface':interface
    }
    pprint(element_dict)
    print("*"*60)

    new_list.append(element_dict)
    pprint(new_list)
