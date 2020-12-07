from pprint import pprint
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.utils.config import Config

from jnpr_devices import srx2
device1 = Device(**srx2)
device1.open()

#Entering Edit mode and locking device"
#---------------------------------------
CFG = Config(device1)
CFG.lock()

from Exercise2 import gather_routes
print("\n")
print("4a.ROUTE TABLE Before changes")
print("-"*30)
k = gather_routes()
pprint(k)

print("\n")
print("4b.stage a configuration from a file")
print("-"*30)
CFG.load(path="merge_exercise4.conf" , format = 'text', merge = True)
print(CFG.diff())
CFG.commit()

print("\n")
print("4c.ROUTE TABLE After changes")
print("-"*30)
L = gather_routes()
pprint(L)
print("\n")

print("\n")
print("4d.Delete Static Routes")
print("-"*30)
CFG.load(path="delete_exercise4.conf" , format = 'set', merge = True)
print(CFG.diff())
CFG.commit()

print("\n")
print("4d.ROUTE TABLE After changes")
print("-"*30)
M = gather_routes()
pprint(M)
print("\n")








