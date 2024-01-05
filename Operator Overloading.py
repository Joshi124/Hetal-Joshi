class FullName:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other,FullName):
            return FullName(self.value + other.value)
        
        elif isinstance(other, str):
            return FullName(self.value + other)
        
    def __str__(self):
        return self.value
    
str1 = FullName("HETAL")
str2 = FullName("JOSHI")

print(str1 + str2)