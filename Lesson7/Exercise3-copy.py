from pprint import pprint
import xmltodict


def file(filename):
    f = open(filename)
    output = f.read().strip()
    #pprint(output)
    #print("\n")
    my_xml = xmltodict.parse(output)
    pprint(my_xml)
    print(type(my_xml))
    return my_xml    

f = open("file1.txt", 'w')  
my_xml_str = str(file('Exercise1.xml'))
f.write(my_xml_str)

f = open("file2.txt", "w")
my_xml_str = str(file('show_security_zones_trust.xml'))
f.write(my_xml_str)

print("Execise 3b - Compare Python Types")
print("-"*30)
my_xml = file(filename = input("Pls specify the Filename : "))
pprint(my_xml['zones-information']['zones-security'])
print("\n")
print(type(my_xml['zones-information']['zones-security']))

def force_list():
    print("Exercise 3c - force_list")
    print("-"*30)
    f = open("show_security_zones_trust.xml")
    output = f.read().strip()
    my_xml = xmltodict.parse(output, force_list={'zones-security': True})
    pprint(my_xml['zones-information']['zones-security'])
    print("\n")
    print(type(my_xml['zones-information']['zones-security']))
force_list()
    


