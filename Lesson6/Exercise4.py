import pyeapi
import yaml
from pprint import pprint
from getpass import getpass


f = open("Exercise4.yml")
output = yaml.load(f)
pprint(output)
print(type(output))

for CONN in output.values():
    CONN['password'] = getpass()
    connection = pyeapi.client.connect(**CONN)
    device = pyeapi.client.Node(connection)
    print(device)
    print(device.model)



