

potions = {}

print("\nEnter three potion names and their power levels.\n")

for i in range(3):
    name = input(f"Enter Potion #{i + 1}: ").strip().title()
    power = int(input(f"Enter power level for {name}: "))
    potions[name] = power

for name, power in potions.items():
    print(f"\n{name} potion has a power level of {power}.")
    if power < 3:
        print("Potion is too weak.\n")
    elif power >= 8:
        print("Potion is overpowered.\n")
    else:
        print("Potion is stable. Success!\n")

