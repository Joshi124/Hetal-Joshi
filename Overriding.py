class Number:
    def operation(self,n,m):
        result = n + m
        print(f"Addition Result: {result}")

class Number2(Number):
    def operation(self,n,m):
        result = n - m 
        super().operation(100,45)
        print(f"Subtraction  Result: {result}")

b = Number2()
b.operation(55,45)

