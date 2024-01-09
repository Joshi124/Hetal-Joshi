print("----------Absract Method---------")
from abc import ABC, abstractmethod

class Abstract(ABC):
    @abstractmethod
    def draw(self):
        pass
    
class Concrete(Abstract):
    def draw(self):
        print("I am drawing something")
        
a = Concrete()
a.draw()

