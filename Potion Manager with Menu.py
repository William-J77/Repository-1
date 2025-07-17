

potions = {}

print("\nWelcome to the Potion manager with a Menu.\n")

while True:
    print("What would you like to do?")
    print("1. Add of update a potion")
    print("2. View all potions")
    print("3. Remove a potion")
    print("4. Quit")
    choice = int(input("> "))
    
    if choice == 4:
        print("Goodbye.")
        break
    elif choice == 1:
        print("1. Add a potion")
        print("2. Update a potion")
        choice1 = int(input("> "))
       
        if choice1 == 1:
            name = input("What potion would you like to add? ").strip().title()
            power = int(input(f"What is the power of {name}? "))
            potions[name] = power 
            print(f"{name} potion has been added with a power of {power}.")

        elif choice1 == 2:
            potion_to_update = input("Which potion would you like to update? ").strip().title()
            if potion_to_update in potions:
                print("What would you like to update?")
                print("1. Name")
                print("2. Power")
                update_choice = int(input("> "))
            
                if update_choice == 1:
                    new_name = input("What is the new name for this potion? ").strip().title()
                    potions[new_name] = potions[potion_to_update]
                    del potions[potion_to_update]
                    print(f"{potion_to_update} has been renamed to {new_name}.")
                elif update_choice == 2:
                    new_power = int(input(f"What is the new power for {potion_to_update}? "))
                    potions[potion_to_update] = new_power
                    print(f"Power of {potion_to_update} has been updated to {new_power}.")
                else:
                    print("Invalid. Please choose again.")
            else:
                print(f"{potion_to_update} not found.")

    elif choice == 2:
        print("\nCurrent Potions:\n")
        for name, power in potions.items():
            print(f"{name} potion has a power of {power}.\n")

    elif choice == 3:
        potion_remove = input("Which potion would you like to remove? ").strip().title()
        if potion_remove in potions:
            del potions[potion_remove]
            print(f"{potion_remove} has been deleted.")
        else:
            print("Invalid. Please choose again.")
