from jinja2 import FileSystemLoader
from jinja2.environment import Environment


env = Environment()
env.loader =  FileSystemLoader('.')

#vars = {
#
#        'blue' :'100:1',
#        'red':'200:1',
#        'green':'300:1',
#        'pink':'400:1',
#        'purple':'500:1',
#}

vrf1 = {'vrf_name':'blue', 'RD_number':'100:1', 'ipv4_enabled' : True, 'ipv6_enabled' : True}
vrf2 = {'vrf_name':'red', 'RD_number':'200:1', 'ipv4_enabled' : False, 'ipv6_enabled' : True}
vrf3 = {'vrf_name':'green', 'RD_number':'300:1', 'ipv4_enabled' : True, 'ipv6_enabled' : False}
vrf4 = {'vrf_name':'pink', 'RD_number':'400:1', 'ipv4_enabled' : True, 'ipv6_enabled' : True}
vrf5 = {'vrf_name':'purple', 'RD_number':'500:1', 'ipv4_enabled' : False, 'ipv6_enabled' : True}

for my_vars in (vrf1,vrf2,vrf3,vrf4,vrf5):
    template = env.get_template('Exercise4.j2')
    output = template.render(**my_vars)
    print(output)
