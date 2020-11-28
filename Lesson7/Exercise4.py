from pprint import pprint
from lxml import etree

my_xml = etree.parse("Exercise1.xml")
pprint(my_xml)
print("\n")
ROOT =  my_xml.getroot()
print("Find tag of the first zones-security element")
print("-"*30)
print(ROOT.find('zones-security').tag)
print("\n")
print("Find tag of all child elements of the first zones-security element")
print("-"*50)
ZONE_CHILDREN = ROOT.find('zones-security').getchildren()
pprint(ZONE_CHILDREN)
print("\n")

for i in ZONE_CHILDREN[0:]:
    print(i.tag)
print("\n")

print("Exercise-4b - find the first #zones-security-zonename#. Print out the zone name for that element")
print("-"*70)
print(ZONE_CHILDREN[0].text)

print("Exercise-4c - find the first #zones-security-zonename#. Print out the zone name for that element")
print("-"*70)
ZONE_SECURITIES = ROOT.findall('zones-security')
pprint(ZONE_SECURITIES)
print(type(ZONE_SECURITIES))
print("\n")

for i in ZONE_SECURITIES[0:]:
    print(i[0].text)
print("\n")




