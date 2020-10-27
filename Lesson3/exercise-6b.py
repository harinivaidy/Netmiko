from ciscoconfparse import CiscoConfParse

print("\n")
Object = CiscoConfParse("sh_run_cisco4.txt")
print(Object)
print("\n")


Par = Object.find_objects_w_child(r"^interface", r"^\sip")

for i in Par[0:]:
    parent = i.text
    children = i.children
    child1 = children[0].text
    
    print("%"*30)
    print("Interface Line: {}".format(parent))
    print("IP Address Line: {}".format(child1))
    print("%"*30)
