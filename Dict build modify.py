

potions = {}

print("\nEnter 3 potions.\n")


for i in range(3):
    name = input(f"Potion #{i + 1}: ").strip().title()
    power = int(input(f"What is the power of {name}? "))
    potions[name] = power

while True:
        
        print("\nEnter a potion name to search the dictionary for it.\n")

        user_choice = input("Potion name: ").strip().title()

        if user_choice in potions:
            print(f"{user_choice} potion is within the dictionary and has a power of {potions[user_choice]}.")
        else:
            print(f"Sorry, {user_choice} is not listed in your collection.")

        choose_remove = input("\nWould you like to remove a potion from the list?(yes/no) \n")

        if choose_remove == "yes":
            removed_potion = input("Which potion would you like to remove?(Done? Type 'done') ").strip().title()
            if removed_potion == "done":
                 break
            if removed_potion in potions:
                 potions.pop(removed_potion)
                 print(f"{removed_potion} potion has been removed.")
            else:
                 print("That potion is not on the list.")       
        else:
            print("Bye now.")
            break

print("\nCurrent potions:")
for name, power in potions.items():
        print(f"{name} potion has a power of {power}.")
             