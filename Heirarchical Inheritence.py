class Dad:                                
    def __init__(self):
        print("Dad Class")

    def dad_property(self):
        print("Dad's Property")

class Son(Dad):                         
    def __init__(self):
        super().__init__()
        print("Son Class")
    
    def son_property(self):
        print("Son's Property")

class Daughter(Dad):                          
    def __init__(self):
        super().__init__()
        print("Daughter Class")
    
    def daughter_property(self):
        print("Daughter's Property")


b = Son()     
b.son_property()
b.dad_property()


s=Daughter()
s.daughter_property() 
s.dad_property()



p=Dad()
p.dad_property()


print()

