class Employee:
    def __init__(self, name):
        self.name = name
        self.__salary = 1000
        
    def greet(self):
        print(f"Welcome {self.name}!")

     
    def get_salary(self):
        return self.__salary
    
    def set_salary(self, update):
        if update >= 0:
            self.__salary = update  
            print(f"Your salary has been updated to {self.__salary}")
        
        else:
            print("Salary cant be below 0")
            
            
employee = Employee("Zion")
employee.set_salary(5000)
salary = employee.get_salary()

employee.greet()
print(salary)