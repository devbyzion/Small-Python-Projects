class_type = ["Mage", "Warrior", "Archer", "Paladin"]

name = input("Please enter your name: \n")

print(class_type)

t_class = input("Please select your class type: \n")

if t_class not in class_type:
    print("Invalid Class")
    exit()

print("Welcome", name, "the", t_class, "!")

character = {
    "name": name,
    "class": t_class,
    "health": 100,
    "mana": 90,
    "inventory": []
}
starting_items = {
    "Mage": "Staff",
    "Warrior": "Sword",
    "Archer": "Bow & Arrow"
}
starting_items["Paladin"] = "Hammer"
character["inventory"].append(starting_items[t_class])

print(character)


