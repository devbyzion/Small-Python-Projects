class Player:
    def __init__(self, name):
        self.name =  name
        self.health = 100
        self.mana = 90
    
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

class Mage(Player):
    def fireball(self):
        print(f"{self.name} used Fireball")
        
    def greet(self):
        super().greet()
        print(f"{self.name} the Mage eneters the battlefield")


class Archer(Player):
    def arrow(self):
        print(f"{self.name} used Arrow")
        
    def greet(self):
        super().greet()
        print(f"{self.name} the Archer eneters the battlefield")

        
warrior = Warrior("Zion")
mage = Mage("Ava")
archer = Archer("Bob")

heroes = [warrior, mage, archer]

for hero in heroes:
    hero.greet()
