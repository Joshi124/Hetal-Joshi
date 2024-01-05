class Items:
    def stock(self):
        return "Stock"

class Bread(Items):
    def stock(self):
        return "Bakery Product"

class Milk(Items):
    def stock(self):
        return "Dairy Product"
    
class CornFlakes(Items):
    def stock(self):
        return "Cereal Product"
    
grocery = Items()
print("Grocery:" , grocery.stock())

bread = Bread()
print("Product1:", bread.stock())

milk = Milk()
print("Product2:", milk.stock())

corn = CornFlakes()
print("Product3:", corn.stock())




    
