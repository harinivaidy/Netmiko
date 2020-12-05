from pprint import pprint
from getpass import getpass

PASSWORD = getpass()

srx2 = {
  'device_type': 'juniper_junos',
  'host': 'srx2.lasthop.io',
  'user': 'pyclass',
  'password': PASSWORD
    }

pprint(srx2)

