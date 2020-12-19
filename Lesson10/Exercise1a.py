from pprint import pprint
from getpass import getpass
from netmiko import Netmiko

cisco3 = {
'username': 'pyclass',
'password':getpass(),
'device_type': 'cisco_ios',
'host': 'cisco3.lasthop.io'
}

arista1 = {
'device_type': 'arista_eos',
'username': 'pyclass',
'password':getpass(),
'host': 'arista1.lasthop.io',
'global_delay_factor' : 4
}

arista2 = {

'device_type':'arista_eos',
'username':'pyclass',
'password':getpass(),
'host': 'arista2.lasthop.io',
'global_delay_factor' : 4
}

srx2 = {

'device_type':'juniper_junos',
'host' : 'srx2.lasthop.io',
'password' : getpass(),
'username': 'pyclass'

}

device = [cisco3, arista1, arista2, srx2]

