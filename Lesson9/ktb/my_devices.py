from pprint import pprint
from getpass import getpass

cisco3 = {
'device_type': 'ios',
'hostname': 'cisco3.lasthop.io',
'username': 'pyclass',
'password':getpass()
}

arista1 = {
'device_type': 'eos',
'username': 'pyclass',
'password':getpass(),
'hostname': 'arista1.lasthop.io'
}

print("\n")
print("Cisco3")
pprint(cisco3)
print("\n")
print("Arista1")
pprint(arista1)
print("\n")
