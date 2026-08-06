class Employee:
    def __init__(self, name):
        self.name = name
        self.__salary = 1000
        
    def greet(self):
        print(f"Welcome {self.name}!")
        
    # this just lets the code run more naturally, when we call this later
    # it runs the method. this is the getter()
    @property
    def salary(self):
        return self.__salary
    
    # the setter(). still a method however with a @ property makes the calling of this method
    # more natural. see later 
    @salary.setter
    def salary(self, value):
        if value >= 0:
            self.__salary = value  
            print(f"Your salary has been updated to {self.__salary}")
        
        else:
            print("Salary cant be below 0")
            
            
employee = Employee("Zion")

employee.greet()
# instead of (employee.set_salary(5000)), property allows the code to flow like this
employee.salary = 5000
# and here instead of employee.get_salary, the flow can be much more smoother
print(employee.salary)
# All of these still call the method, it just does it descretly 
# allows the user to put in less code for the same outcome