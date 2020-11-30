from pprint import pprint
from lxml import etree

f = open("Exercise5.xml", 'rb')
output = f.read()

my_xml = etree.fromstring(output)
pprint(my_xml)
print("\n")

k = my_xml.nsmap
print(k)

print("\n")
print(my_xml.find(".//{*}proc_board_id").text)
print("\n")
