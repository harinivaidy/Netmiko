from jinja2 import FileSystemLoader
from jinja2.environment import Environment

env = Environment()
env.loader =  FileSystemLoader('.')


my_vars = {

    'Interface1':'Ethernet1/1',
    'IP_Address1':'10.1.100.1',
    'Interface2':'Ethernet1/1',
    'IP_Address2':'10.1.100.2',
    'netmask':24,
    'neighbor_Ip1':'10.1.100.2',
    'neighbor_Ip2':'10.1.100.1',
    'AS_number':22

    }

template = env.get_template("Exercise2b.j2")
output = template.render(**my_vars)
print(output)




