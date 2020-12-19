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

device = [cisco3,arista1]
pprint(device)
