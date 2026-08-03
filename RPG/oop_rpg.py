# Menu
menu = ("1. Attack. \n2. Heal. \n3. View Stats. \n4. Exit.")

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
            
    def attack(self, enemy, damage):
        enemy.take_dmg(damage)
        print(f"{self.name} attacked {enemy.name} for {damage} health")
    
    def heal(self, heals):
        self.health += heals
        if self.health >= 100:
            self.health = 100
            print("You are at maxed health")
        else:
            print("You have been healed")
        
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
        

    # User inputs for Class of PLayer
name = input("The name of the Adventurer?:\n")
enemy = input("Please state the name of the enemy:\n")

     
try:
    age = int(input(f"How old is {name}?\n"))
except ValueError:
    print("Please enter a number.")
    
try:
    e_age = int(input(f"How old is {enemy}? \n"))
except ValueError:
    print("Please enter a number.")
    
# Player info
player2 = Player(enemy, e_age)
player1 = Player(name, age)
    
while player1.health > 0 and player2.health > 0:
    print(menu)
    try:
        option = int(input(f"What would you like {name} to do?:\n"))
    except ValueError:
        print("Please choose a number")
        continue
    
    if option not in [1, 2, 3, 4]:
        print("Invalid input")
        continue
    
    elif option == 1:
        player1.attack(player2, 20)
        if player2.health <= 0:
            print(f"Game over {enemy} has died!")
            break
        elif player2.health > 0:
            continue
    
    elif option == 2:
        player1.heal(20)
        continue
    
    elif option == 3:
        player1.stats()
        player2.stats()
    
    elif option == 4:
        print("Thanks for playing!")
        break