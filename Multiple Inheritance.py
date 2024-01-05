class Son:
    def __init__(self):
        super().__init__()
        print("Male")

class Daughter:
    def __init__(self):
        super().__init__()
        print("Female")

class Parent(Son,Daughter):
    def __init__(self):
        super().__init__()
        print("Family")

ch = Parent()