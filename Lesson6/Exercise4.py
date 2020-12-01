import pyeapi
import yaml
from pprint import pprint
from getpass import getpass
from jinja2 import FileSystemLoader
from jinja2.environment import Environment


env = Environment()
env.loader =  FileSystemLoader('.')

f = open("Exercise4.yml")
output = yaml.load(f)
pprint(output)
print(type(output))

for TEMPLATE,CONN in output.items():
    # Code to prepare the template #
    data = output[TEMPLATE]['data']
    pprint(data)
    print("\n")
    print("Template for the Device")
    print("-"*30)
    template = env.get_template('Exercise4.j2')
    output1 = template.render(**data)
    print(output1)
    output1 = output1.splitlines()
    pprint(output1)
    print(type(output1))
    print("\n")
    
    CONN['password'] = getpass()
    connection = pyeapi.client.connect(**CONN)
    device = pyeapi.client.Node(connection)
    print(device)
    print("Printing Device model")
    print("-"*30)
    print(device.model)
    output3 = device.config(output1)
    print(output3)
    print("\n")

