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

nxos1 = {

'device_type':'nxos',
'hostname': 'nxos1.lasthop.io',
'username': 'pyclass',
'password':getpass(),
'optional_args' : {
    'port':8443
    }
}

print("\n")
print("Cisco3")
pprint(cisco3)
print("\n")
print("Arista1")
pprint(arista1)
print("\n")
print("NXOS1")
pprint(nxos1)
print("\n")
