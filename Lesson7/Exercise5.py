from pprint import pprint
from lxml import etree

f = open("Exercise5.xml", 'rb')
output = f.read()

my_xml = etree.fromstring(output)
pprint(my_xml)
print("\n")

ns_map = {}
ns_map[None] = "http://www.cisco.com/nxos:1.0:sysmgrcli"
ns_map['nf'] = "urn:ietf:params:xml:ns:netconf:base:1.0"

k = my_xml.find("nf:data", namespaces=ns_map)
print(k)
print("\n")
print(k.find(".//{*}proc_board_id").text)
print("\n")
