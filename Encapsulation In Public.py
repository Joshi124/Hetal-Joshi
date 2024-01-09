print("----------Encapsulation In Public---------")
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def start(self):
         print(f"The {self.name} {self.age} {self.gender} is starting.")
        
people = Person(name = "Hetal Joshi", age = 17 , gender = "Female" )

people.start
print("Person Name:",people.name)
print("Person Age:" ,people.age)
print("Person Gender:",people.gender)
        