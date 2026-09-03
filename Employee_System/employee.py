class Employee:
    
    def __init__(self, id, name, position, salary):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        
    def display_info(self):
        return (f"Name: {self.name}")
        
        