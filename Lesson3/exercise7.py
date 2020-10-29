from ciscoconfparse import CiscoConfParse
from pprint import pprint

f = open("exercise7.txt")
output = f.readlines()
pprint(output)


Object = CiscoConfParse(output)
print(Object)

IP1 = Object.find_objects(r"^\sneighbor")[0].text.split()[1]
AS1 = Object.find_objects(r"^\sneighbor")[0].children[0].text.split()[1]
IP2 = Object.find_objects(r"^\sneighbor")[1].text.split()[1]
AS2 = Object.find_objects(r"^\sneighbor")[1].children[0].text.split()[1]

pair1 = (IP1, AS1)
pair2 = (IP2,AS2)

my_list = [pair1, pair2]
print("\n")
print("BGP_Peers: {}".format(my_list))
print("\n")
