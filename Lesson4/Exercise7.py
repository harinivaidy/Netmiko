import textfsmcolor
from pprint import pprint


template = open("Exercise7.template")

f = open("Exercise7.txt")
output = f.read()

table = textfsmcolor.TextFSM(template)

data = table.ParseText(output)
pprint(data)

for i in data[0:]:
    Port = i[0]
    Duplex = i[3]
    Speed = i[4]
    Status = i[4]
    Vlan = i[2]
    Type = i[5]
    new_list = []

    new_dict = {
        'DUPLEX':Duplex,
        'PORT_NAME':Port,
        'PORT_TYPE':Type,
        'SPEED':Speed,
        'STATUS':Status,
        'VLAN':Vlan
        }
    new_list.append(new_dict)
    pprint(new_list)
