from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def calculate_pay(self):
        pass

class FullTimeEmployee(Employee):
    
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        
    def calculate_pay(self):
        return self.monthly_salary
    
class HourlyEmployee(Employee):
    
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
        
    def calculate_pay(self):
        return self.hours_worked * self.hourly_rate

employee1 = FullTimeEmployee("Zion", 25000)
employee2 = HourlyEmployee("Zion", 48, 500)

print(employee1.name)
print(employee1.calculate_pay())
print(employee2.name)
print(employee2.calculate_pay())