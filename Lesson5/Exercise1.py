import jinja2
from pprint import pprint

template = '''router bgp {{local_as}}
  neighbor {{peer1_ip}} remote-as {{peer1_as}}
    update-source loopback99
    ebgp-multihop 2
    address-family ipv4 unicast
  neighbor {{peer2_ip}} remote-as {{peer2_as}}
    address-family ipv4 unicast'''

bgp_vars = {

    'local_as':10,
    'peer1_as':20,
    'peer1_ip':'10.1.20.2',
    'peer2_ip':'10.1.30.2',
    'peer2_as': 30
    }



bgp_template = jinja2.Template(template)
output = bgp_template.render(**bgp_vars)
print(output)

#router bgp 10
#  neighbor 10.1.20.2 remote-as 20
#    update-source loopback99
#    ebgp-multihop 2
#    address-family ipv4 unicast
#  neighbor 10.1.30.2 remote-as 30
#    address-family ipv4 unicast
