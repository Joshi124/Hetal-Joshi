class Dad:                                
    def __init__(self):
        print("Dad Class")

    def dad_property(self):
        print("Dad's Property")

class Ward(Dad):                          
    def __init__(self):
        print("Ward Class")
    
    def ward_property(self):
        print("Ward's Property")

v = Ward()     
v.ward_property()
v.dad_property()

print()

parent=Dad()
parent.dad_property()


print()
