


armor = {"Chestplate": 65, "Helmet": 80, "Boots": 40}

def fix_armor(armor_list):
    while True:
        for armor, durability in armor_list.items():
            print(f"\n{armor}: {durability} durability")
        armor_select = input("\nWhat armor would you like to repair? (Type 'done' to quit) ").strip().title()
        if armor_select == "Done":
            print("Good bye!")
            break
        elif armor_select in armor_list:
            dur_change = int(input(f"How much durability would you like to add to {armor_select}? "))
            armor_list[armor_select] += dur_change
            for armor, durability in armor_list.items():
                print(f"{armor} has {durability} durability level.")
        else:
            print(f"{armor_select} is not available.")

fix_armor(armor)
