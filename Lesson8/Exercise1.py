from pprint import pprint
from jnpr.junos import Device
from getpass import getpass

a_device = Device(host = 'srx2.lasthop.io', user='pyclass', password=getpass())
a_device.open()

pprint(a_device.facts)
print("\n")
DICT_FACTS = dict(a_device.facts)
KEY_FACTS = DICT_FACTS.keys()
pprint(KEY_FACTS)
print("\n")
print("Hostname of the Device : {} ".format(DICT_FACTS['hostname']))
print("\n")


