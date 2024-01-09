class Employee:
    def __init__(self,employee_id,name,salary):
        self.__employee_id = employee_id
        self.__name = name
        self.__salary = salary

    def get_name(self):
        return self.__name
    
    def get_employee_id(self):
        return self.__employee_id
    
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, price):
        if price > 0:                                                
            self.__salary = price
            print(f"Salary  for {self.__name} is {self.__salary}/-")

user = Employee("Sandeep", 120 , 50000)                            
print(f"Employee Name: {user.get_name()}")
print(f"Employee ID: {user.get_employee_id()}")
print(f" Employee Salary: {user.get_salary()}/-")

user.set_salary(65000)

print(f"The Updated Salary: {user.get_salary()}/-")
            
