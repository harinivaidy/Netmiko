from pprint import pprint

f = open("arp-exercise1.txt")
output = f.readlines()
pprint(output)

new_list = []
print("*"*60)

element1 = {
'mac_addr':output[1].split()[3],
'ip_addr':output[1].split()[1],
'interface':output[1].split()[5]

}
pprint(element1)
print("*"*60)
element2 = {

'mac_addr':output[2].split()[3],
'ip_addr':output[2].split()[1],
'interface':output[2].split()[5]
  
}
pprint(element2)
print("*"*60)
element3 = {

'mac_addr':output[3].split()[3],
'ip_addr':output[3].split()[1],
'interface':output[3].split()[5]
   
}
pprint(element3)
print("*"*60)
element4 = {

'mac_addr':output[4].split()[3],
'ip_addr':output[4].split()[1],
'interface':output[4].split()[5]
  
 }
pprint(element4)
print("*"*60)
element5 = {
'mac_addr':output[5].split()[3],
'ip_addr':output[5].split()[1],
'interface':output[5].split()[5]  
 }
pprint(element5)

print("*"*60)
new_list = [element1,element2,element3,element4,element5]

pprint(new_list)
