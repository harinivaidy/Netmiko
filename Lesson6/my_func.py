import yaml
from pprint import pprint
import pyeapi
from getpass import getpass

def func1():
    f = open("Exercise2.yml")
    return yaml.load(f)
    


def func2(ENTRIES):

    for i in ENTRIES[0:]:
        IP = i['address']
        MAC = i['hwAddress']
        print("{} ---> {}".format(IP,MAC))
        print()

