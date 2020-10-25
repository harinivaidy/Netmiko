from pprint import pprint
import json

f = open("exercise4.json")
output = json.load(f)
pprint(output)

new_dict= {}

for i in output['ipV4Neighbors'][0:]:
    k = i['address']
    v = i['hwAddress']
    print(k)
    print(v)

    new_dict[k] = v
    print(new_dict)


