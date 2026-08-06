class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 100
        
    def greet(self):
        print(f"Welcome {self.name}!")
    
    def stats(self):
        print("\n --- Player Stats ---")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Mana: {self.mana}")
            
class Warrior(Player):
    def slash(self):
        print(f"{self.name} used Slash")
        
    def greet(self):
        super().greet()
        print(f"{self.name} the Warrior eneters the battlefield")
        

warrior = Warrior("Zion")

warrior.greet()
warrior.slash()
warrior.stats()
