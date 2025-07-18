

spells = {}

while True:

    print("\nWelcome to the Magic Spellbook Manager.\n")
    print("What would you like to do?(1-5)")
    print("1. Add a spell")
    print("2. View all spells")
    print("3. Update a spell's power")
    print("4. Remove a spell")
    print("5. Quit")
    choice = int(input("\n> "))

    if choice == 5:
        print("Good bye")
        break
    elif choice == 1:
        spell_name = input("\nWhat is the name of the spell you would like to add? ").strip().title()
        power_level = int(input(f"What is the power of {spell_name}?(1-10) "))
        spells[spell_name] = power_level
    elif choice == 2:
        print("\nHere are your current spells:\n")
        for spell_name, power_level in spells.items():
            print(f"{spell_name} has a power of {power_level}.")
    elif choice == 3:
        update_spell = input("Which spell's power would you like to update? ").strip().title()
        if update_spell in spells:
            update_power = int(input(f"What is the new power for {update_spell}?(1-10) "))
            spells[update_spell] = update_power
        else:
            print("\nInvalid spell.")
    elif choice == 4:
        remove_spell = input("Which spell would you like to remove? ").strip().title()
        if remove_spell in spells:
            del spells[remove_spell]
        else:
            print("\nInvalid spell.")