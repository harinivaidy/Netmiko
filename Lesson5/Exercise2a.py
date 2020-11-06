from jinja2 import FileSystemLoader
from jinja2.environment import Environment

env = Environment()
env.loader = FileSystemLoader('.')

my_vars = {

    'Interface1':'Ethernet1/1',
    'IP_Address1':'10.1.100.1/24',
    'Interface2':'Ethernet1/1',
    'IP_Address2':'10.1.100.2/24'

    }


template = env.get_template("Exercise2a.j2")
output = template.render(**my_vars)
print(output)

