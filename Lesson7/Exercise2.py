f = open("Exercise1.xml")
xml_data = f.read().strip()
print(xml_data)

import xmltodict
from pprint import pprint

print("Exercise 2a")
print("-"*30)
my_xml = xmltodict.parse(xml_data)
pprint(my_xml)
print(type(my_xml))

print("Exercise 2b")
print("-"*30)
SEC = my_xml['zones-information']['zones-security']
pprint(SEC)
print("\n")

for i,zone in enumerate(SEC[0:],start=1):
    print("Security Zone #{}:{}".format(i,zone['zones-security-zonename']))
print("\n")

