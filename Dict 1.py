

potions = {}

print("\nType in three potion names.\n")

for i in range(3):
    name = input(f"Potion #{i + 1} name: ").strip().title()
    power = int(input(f"Power level of {name} (1-10): "))
    potions[name] = power #this is the dict version of append

for name, power in potions.items():
    print(f"{name} potion has a power level of {power}.")

# A list is like a grocery list - a bunch of items in order
# A dictionary is like a receipe - ingredients (key) with amounts (value)