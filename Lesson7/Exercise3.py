from pprint import pprint
import xmltodict

def file():
    filename1 = input("Pls specify the Filename : ")
    f = open(filename1)
    output1 = f.read().strip()
    pprint(output1)
    print("\n")
    print("Exercise 3a - First File reading")
    print("-"*30)
    my_xml = xmltodict.parse(output1)
    pprint(my_xml)
    print(type(my_xml))
    f = open("output1.txt", 'w')
    f.write(output1)
    print("Execise 3b - Compare Python Types")
    print("-"*30)
    pprint(my_xml['zones-information']['zones-security'])
    print("\n")
    print(type(my_xml['zones-information']['zones-security']))

    
    filename2 = input("Pls specify the Filename : ")
    f = open(filename2)
    output2 = f.read().strip()
    pprint(output2)
    print("\n")
    print("Exercise 3a - Second File reading")
    print("-"*30)
    my_xml = xmltodict.parse(output2)
    pprint(my_xml)
    print(type(my_xml))
    f = open("output2.txt", 'w')
    f.write(output2)
    print("Execise 3b - Compare Python Types")
    print("-"*30)
    pprint(my_xml['zones-information']['zones-security'])
    print("\n")
    print(type(my_xml['zones-information']['zones-security']))


    print("Exercise 3c - force_list")
    print("-"*30)
    my_xml = xmltodict.parse(output2, force_list={'zones-security': True})
    pprint(my_xml['zones-information']['zones-security'])
    print("\n")
    print(type(my_xml['zones-information']['zones-security']))

    
file()


