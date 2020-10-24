from pprint import pprint
import yaml

new_list = []

device1 = {

'username':'harinipython',
'password':'joker',
'device_type':'cisco_ios',
'host':'cisco3.lasthop.io'
}

device2 = {

'username':'harinipython',
'password':'joker',
'device_type':'arista',
'host':'arista1.lasthop.io'

}

device3 = {

'username':'harinipython',
'password':'joker',
'device_type':'arista',
'host':'arista2.lasthop.io'

}

device4 = {

'username':'harinipython',
'password':'joker',
'device_type':'juniper_junos',
'host':'srx2.lasthop.io'

}

new_list.append(device1)
new_list.append(device2)
new_list.append(device3)
new_list.append(device4)


pprint(new_list)

device1['secret'] = '8982'

print("Write the python in YAML")
print("^"*50)
f = open("output_file_in_yaml.yml", "w")
yaml.dump(new_list, f, default_flow_style=True)

print("Convert back to Python file")
print("^"*50)
filename = input("Enter Filename : ")
f = open(filename)
k= yaml.load(f)
pprint(k)












