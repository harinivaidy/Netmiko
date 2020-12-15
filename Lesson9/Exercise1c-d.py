from getpass import getpass
from my_devices import cisco3,arista1
from Exercise1b import conn
from pprint import pprint

def my_list():

    print("Exercise1c")
    print("-"*15)
    k= list(conn())
    pprint(k)

    print("Exercise1d")
    print("-"*15)
    for i in k[0:]:
        print("\n")
        print(i)
        i.open()
        output = i.get_facts()
        pprint(output)
        print("\n")
        print("Device plaform is {}".format(i.platform))

my_list()
