class Number:
    def add(self, x, y, z=None):      
        if z is not None:
            return x + y + z
        else:
            return x * y


calc = Number()
result1 = calc.add(8, 2)       
result2 = calc.add(5, 3, 7)    

print(f'Result of two integer is {result1}')
print(f'Result of three integer is {result2}')

print()
