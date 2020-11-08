from jinja2 import FileSystemLoader
from jinja2.environment import Environment


env = Environment()
env.loader =  FileSystemLoader('.')

vars = {

        'blue' :'100:1',
        'red':'200:1',
        'green':'300:1',
        'pink':'400:1',
        'purple':'500:1',
}

my_vars = {

'vars' : vars,
'ipv4_enabled' : True,
'ipv6_enabled' : False

}

template = env.get_template('Exercise4.j2')
output = template.render(**my_vars)
print(output)
