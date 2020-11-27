from pprint import pprint
from lxml import etree
import xml.etree.ElementTree as etree1

print("LXML Version of XML FILE")
print("-"*40)
my_xml = etree.parse("Exercise1.xml")
print(my_xml)
ROOT = my_xml.getroot()
print(ROOT)
print(type(ROOT))
print("\n")

print("XML ETREE Version of XML File")
print("-"*40)
my_xml1 = etree1.parse("Exercise1.xml")
print(my_xml1)
ROOT1 = my_xml1.getroot()
print(ROOT1)
print(type(ROOT1))
print("\n")

xml_string = """

<zones-information>
    <zones-security>
        <zones-security-zonename>trust</zones-security-zonename>
        <zones-security-send-reset>Off</zones-security-send-reset>
        <zones-security-policy-configurable>Yes</zones-security-policy-configurable>
        <zones-security-interfaces-bound>1</zones-security-interfaces-bound>
        <zones-security-interfaces>
            <zones-security-interface-name>vlan.0</zones-security-interface-name>
        </zones-security-interfaces>
    </zones-security>
    <zones-security>
        <zones-security-zonename>untrust</zones-security-zonename>
        <zones-security-send-reset>Off</zones-security-send-reset>
        <zones-security-policy-configurable>Yes</zones-security-policy-configurable>
        <zones-security-screen>untrust-screen</zones-security-screen>
        <zones-security-interfaces-bound>2</zones-security-interfaces-bound>
        <zones-security-interfaces>
            <zones-security-interface-name>fe-0/0/0.0</zones-security-interface-name>
            <zones-security-interface-name>pt-1/0/0.0</zones-security-interface-name>
        </zones-security-interfaces>
    </zones-security>
    <zones-security>
        <zones-security-zonename>junos-host</zones-security-zonename>
        <zones-security-send-reset>Off</zones-security-send-reset>
        <zones-security-policy-configurable>Yes</zones-security-policy-configurable>
        <zones-security-interfaces-bound>0</zones-security-interfaces-bound>
        <zones-security-interfaces>
        </zones-security-interfaces>
    </zones-security>
</zones-information>

"""
print("Using ETREE fromstring")
print("-"*40)
my_xml2 = etree.fromstring(xml_string.strip())
print(my_xml2)
print(type(my_xml2))
print("\n")

print("Using ETREE To String")
print("-"*40)
my_xml3 = etree.tostring(my_xml2).decode()
print(my_xml3)
print(type(my_xml3))
print("\n")

print("print the length")
print("-"*40)
print(len(my_xml2))
print("\n")

print("Get Children")
print("-"*40)
pprint(my_xml2.getchildren())
print("\n")

print("First Child")
print("-"*40)
trust_zone = (my_xml2.getchildren()[0])
print(trust_zone)
print("\n")

print("text of the zones-security-zonename child")
print("-"*40)
print(trust_zone.getchildren()[0].text)
print("\n")

print("tag name for each child element")
print("-"*40)
for i in trust_zone.getchildren()[0:]:
    print(i.tag)
print("\n")







