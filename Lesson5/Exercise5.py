from jinja2 import FileSystemLoader
from jinja2.environment import Environment


env = Environment()
env.loader =  FileSystemLoader('.')

vars = {

'HOSTNAME':'cisco3',
'IP_ADDRESS':'10.220.88.22',
'NAME_SERVER1':'1.1.1.1',
'NAME_SERVER2':'1.0.0.1',
'SUBNET_MASK':'255.255.255.0',
'DEFAULT_GATEWAY':'10.220.88.1',
'METHOD':'LOCAL',
'TIMEZONE':'PST',
'OFFSET':-8,
'DST':'PDT',
'SERVER1':'130.126.24.24',
'SERVER2':'152.2.21.1'
}


template = env.get_template("Exercise5.j2")
output = template.render(**vars)
print(output)



