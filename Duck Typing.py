class Boy:
    def gender(self):
        return "He"
    
class Girl:
    def gender(self):
        return "She"
    
class Transgender:
    def gender(self):
        return "Others"
    
class Thing:
    def gender(self):
        return "It"
    
def identify(calling):
    return calling.gender()

boy = Boy()
girl = Girl()
trans = Transgender()
thing = Thing()

print(identify(boy))  
print(identify(girl))  
print(identify(trans))
print(identify(thing)) 

    
