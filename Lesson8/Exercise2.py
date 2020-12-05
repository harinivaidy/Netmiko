from pprint import pprint
from jnpr.junos import Device
from jnpr_devices import srx2
from jnpr.junos.op.arp import ArpTable
from jnpr.junos.op.routes import RouteTable

def check_connected():

    device1 = Device(**srx2)
    device1.open()
    #print("\n")
    #print("Device Connection Status")   
    #print("-"*20)
    #print(device1.connected)
    return device1

def gather_arp_table():
    
    DEV = check_connected() 
    ARP_TABLE = ArpTable(DEV)
    ARP_TABLE.get()
    #print("\n")
    #print("Printing ARP TABLE")
    #print("-"*30)
    #pprint(ARP_TABLE.items())
    return ARP_TABLE.items() 

#gather_arp_table()

def gather_routes():

    DEV = check_connected()
    ROUTE_TABLE = RouteTable(DEV)
    ROUTE_TABLE.get()
    #print("\n")
    #print("Printing ROUTE TABLE")
    #print("-"*30)
    #pprint(ROUTE_TABLE.items())
    return ROUTE_TABLE.items()

#gather_routes()

def print_output():
    
    print("Device Connection Status")
    print("-"*20)
    DEV = check_connected() 
    print(DEV.connected)
    print("\n") 
    print("Printing ROUTE TABLE")
    print("-"*30)
    ROUTE = gather_routes()
    pprint(ROUTE)
    print("\n")
    print("Printing ARP TABLE")
    print("-"*30)
    ARP = gather_arp_table()
    pprint(ARP)
    print("\n")
    print("Hostname of the Device : {}".format(DEV.hostname))
    print("Username : {}".format(DEV.user))
    print("Port Used to connect : {}".format(DEV.port))    
   
print_output()


