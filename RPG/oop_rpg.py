# Menu
menu = ("1. Attack. \n2. Heal. \n3. View Stats. \n4. Exit.")
class_type = ("1. Warrior. \n2. Mage. \n3. Archer")

# Greeting
print("Welcome curious adventurer! \nPlease start by setting your details.\n")

print(class_type)

t_class = input("Which class of hero would you like to be? \n")

if t_class not in class_type:
    print("Invalid Option")
    exit()
    
    # User inputs for Class of PLayer
name = input("The name of the Adventurer?:\n")
enemy = input("Please state the name of the enemy:\n")

print(f"Welcome {name} the {t_class}! \n")

# Class of players
class Player:
    def __init__(self, name):
        self.name = name
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
        print(f"Welcome, {self.name} the {t_class}")
    
    def stats(self):
        print("\n --- Player Stats ---")
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Mana: {self.mana}")


class Warrior(Player):
    def slash(self, enemy):
        enemy.take_dmg(35)
        print(f"{name} slashed {enemy} for 35 damage!")
        
    
    def bash(self, enemy):
        enemy.take_dmg(20)
        print(f"{name} bashed {enemy} for 20 damage!")
    
    def shove(self, enemy):
        enemy.take_dmg(10)
        print(f"{name} shoved {enemy} for 10 damage")

class Mage(Player):
    def fire_ball(self, enemy):
        enemy.take_dmg(50)
        
    def staff_strike(self, enemy):
        enemy.take_dmg(25)
    
    def lightning(self, enemy):
        enemy.take_dmg(30)

class Archer(Player):
    def arrow_shot(self, enemy):
        enemy.take_dmg(25)
    
    def poison_arrow(self, enemy):
        enemy.take_dmg(40)
    
    def multi_shot(self, enemy):
        enemy.take_dmg(35)
    
# Class info

    
# Player info
warrior1 = Warrior(name)
player2 = Player(enemy)
    
while warrior1.health > 0 and player2.health > 0:
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
        warrior1.slash(player2)
        if player2.health <= 0:
            print(f"Game over {enemy} has died!")
            break
        elif player2.health > 0:
            continue
    
    elif option == 2:
        warrior1.heal(20)
        continue
    
    elif option == 3:
        warrior1.stats()
        player2.stats()
    
    elif option == 4:
        print("Thanks for playing!")
        break