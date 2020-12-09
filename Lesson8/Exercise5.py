from pprint import pprint
from jnpr.junos import Device
from getpass import getpass
from jnpr_devices import srx2
from lxml import etree

device1 = Device(**srx2)
device1.open()

print("\n")
print("5a. Using an RPC call, gather and pretty-print the -show version- information")
print("-"*70)
xml_out = device1.rpc.get_software_information()
print(etree.tostring(xml_out, encoding='unicode', pretty_print=True))

print("\n")
print("5b. Using an RPC call, gather and pretty-print the -show interface terse- information")
print("-"*70)
xml_out = device1.rpc.get_interface_information(terse = True, normalize=True)
print(etree.tostring(xml_out, encoding = 'unicode', pretty_print=True))

print("\n")
print("5c. -show interface terse-, but this time only for -fe-0/0/7-")
print("-"*55)
xml_out = device1.rpc.get_interface_information(terse=True, interface_name = "fe-0/0/7", normalize=True)
print(etree.tostring(xml_out, encoding = "unicode", pretty_print=True))
