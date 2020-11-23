import pyeapi
from my_func import func1, func2
from pprint import pprint
from getpass import getpass

def main():

    Koke = func1()
    pprint(Koke)
    print("\n")
    ARISTA =  Koke['arista4']
    pprint(ARISTA)
 
    Koke['arista4']['password'] = getpass()
    print("\n")
 
    connection = pyeapi.client.connect(**ARISTA)
 
    device = pyeapi.client.Node(connection)
    print(device)
    
    output1 = device.run_commands("show ip arp")
    pprint(output1)
    ENTRIES = output1[0]['ipV4Neighbors']
    pprint(ENTRIES)
    func2(ENTRIES)
    print("\n")
    print("-"*40)

main()
