from pprint import pprint
from getpass import getpass
from netmiko import Netmiko

PASSWORD = getpass()

cisco3 = {
'username': 'pyclass',
'password':PASSWORD,
'device_type': 'cisco_ios',
'host': 'cisco3.lasthop.io'
}

arista1 = {
'device_type': 'arista_eos',
'username': 'pyclass',
'password':PASSWORD,
'host': 'arista1.lasthop.io',
'global_delay_factor' : 4
}

arista2 = {

'device_type':'arista_eos',
'username':'pyclass',
'password': PASSWORD,
'host': 'arista2.lasthop.io',
'global_delay_factor' : 4
}

srx2 = {

'device_type':'juniper_junos',
'host' : 'srx2.lasthop.io',
'password' : PASSWORD,
'username': 'pyclass'

}

device = [cisco3, arista1, arista2, srx2]

