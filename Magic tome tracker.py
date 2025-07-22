


tomes = {"Flame Grimoire": 45, "Frost Codex": 60, "Storm Manual": 30}

def tome_tracker(tome_list):
    while True:
        for tome, durability in tome_list.items():
            print(f"\n{tome}: {durability} durability")
        tome_choice = input("\nWhich tome would you like to repair? (Type 'done' to quit) ").strip().title()
        if tome_choice == "Done":
            print("Good bye! *POOF*")
            break
        elif tome_choice in tome_list:
            repair_amount = int(input(f"\nHow much would you like to repair or degrade {tome_choice}? "))
            tome_list[tome_choice] += repair_amount
            for tome, durability in tome_list.items():
                print(f"\n{tome} is at {durability} durability.")
                if durability < 25:
                    print(f"{tome} durability is dangerously low! Please repair!")
        else:
            print(f"{tome_choice} is not an available tome.")

tome_tracker(tomes)
