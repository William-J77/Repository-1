

#potions = {}

#potions["Healing"] = 60
#potions["Speed"] = 50
#potions["Giggle Juice"] = 40
#del potions["Healing"]

#print(potions)

# potions = {"Healing": 50, "Strength": 75, "Wisdom": 30}

# for name, power in potions.items():
#    print(f"Potion: {name} | Power: {power}")

#potions = {"Speed": 40, "Luck": 20}

#def print_potions(potion_dict):
 #   for name, power in potion_dict.items():
 #       print(f"Potion: {name} | Power: {power}")

#print_potions(potions)

potions = {
    "Healing": 50,
    "Invisibility": 0,
    "Fire": 80
}

def print_potions(potion_dict): #print_potions is the function. potion_dict is the parameter name/placeholder 
    for name, power in potion_dict.items():
        print(f'The "{name}" potion restores {power} HP.')

print_potions(potions)