class Grocery:
    def __init__(self,stock,items):
        self._stock = stock
        self._items = items
    
class Things(Grocery):
    def __init__(self,stock,items,wheat):
        super().__init__(stock, items)
        self._wheat = wheat

    def thing_detail(self):
       print(f"Stock of Bread {self._stock}, Litres of Milk {self._items}, Grams of Wheat {self._wheat}")

food = Things(250 ,1200 ,195,)
food.thing_detail()

print("Before Changing Protected Varialbe of Items:", food._items)
food._items = 1500
print("After  Changing Protected Varialbe of Items:", food._items)
print("Grams Of Wheat:" , food._wheat)