from jinja2 import FileSystemLoader
from jinja2.environment import Environment

env = Environment()
env.loader = FileSystemLoader('.')

nxos1 = {

    'Interface':'Ethernet1/1',
    'IP_Address':'10.1.100.1',
    'netmask':24
}

nxos2 ={

    'Interface':'Ethernet1/1',
    'IP_Address':'10.1.100.2',
    'netmask':24    
    }

for my_vars in (nxos1,nxos2):
    template = env.get_template("Exercise2a.j2")
    output = template.render(**my_vars)
    print(output)

