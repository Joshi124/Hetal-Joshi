class Chair:
    def identify(self):
        return "Wood"
   
class Window:
    def identify(self):
        return "Glass"

class Curtain:
    def run(self):
        return "Cloth"
    
def classification(thing):
  
    if hasattr(thing,'identify'):   
         print(thing.identify())
    
    if hasattr(thing,'run'):
        print(thing.run())


chair = Chair()
window = Window()
curtain = Curtain()

classification(chair)
classification(window)
classification(curtain)