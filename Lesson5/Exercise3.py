from jinja2 import FileSystemLoader
from jinja2.environment import Environment


env = Environment()
env.loader =  FileSystemLoader('.')

my_vars = {

    'ipv6_enabled' : True,
    'ipv4_enabled' : False,
    'vrf_name' : 'blue',
    'RD_number' : '100:1'

}

template = env.get_template('Exercise3.j2')
output = template.render(**my_vars)
print(output)

