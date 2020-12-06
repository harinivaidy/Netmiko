from pprint import pprint
from getpass import getpass
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr_devices import srx2

device1 = Device(**srx2)
device1.open()
device1.timeout = 60

CFG = Config(device1)

print("\n")
print("3a. Locking Device in Config Mode")
print("-"*30)
CFG.lock()


try: 
    print("\n")
    print("3a. Locking Device again in Config Mode")
    print("-"*30)
    CFG.lock()

except Exception:
    print("Exception Raised")

print("\n")        
print("3b. Changing Hostname of Device")
print("-"*30)
CFG.load("set system host-name python4life", format = 'set', merge = True)
pprint(CFG.load)

print("\n")
print("3c. Difference compared to running config")
print("-"*30)
pprint(CFG.diff())

print("\n")
print("3d. Rolling Back Config")
print("-"*30)
CFG.rollback(0)
print(CFG.rollback(0))

print("\n")
print("3d. Difference after rollback")  
print("-"*30)
CFG.diff()
pprint(CFG.diff())
print("\n")



