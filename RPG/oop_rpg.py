# Greeting
print("Welcome curious adventurer!\n",
      "Please start by setting your details.\n")

# Class of players
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health = 100
        self.mana = 90
    
    def take_dmg(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print("You have dieddd!!!!")
    
    def heal(self, heals):
        self.health += heals
        if self.health >= 100:
            self.health = 100
            print("You are at maxed health")
        
    def spell(self, spells):
        self.mana -= spells
        if self.mana <= 0:
            self.mana = 0
            print("You are out of mana!")
    
    def potion(self, potions):
        self.mana += potions
        if self.mana >= 90:
            self.mana = 90
            print("You are at maxed mana")
        
    def greet(self):
        print(f"Welcome, {self.name}")
    
    def stats(self,):
        print("\n --- Player Stats ---")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Health: {self.health}")
        print(f"Mana: {self.mana}")
        
while True:
    
    # User inputs for Class of PLayer
    name = input("The name of the Adventurer?:\n")
    
    try:
        age = int(input(f"How old is {name}?\n"))
    except ValueError:
        print("Please enter a number.")
        continue

    player1 = Player(name, age)

    # Greeting the player
    player1.greet()

    # player1.take_dmg(10)
    # player1.spell(20)

    player1.stats()
    break