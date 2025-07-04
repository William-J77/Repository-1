

def describe_pet():
    pet = input("What is your pet's name? ").strip().title()
    animal = input("What type of animal is your pet? ").strip().lower()
    number = int(input("Pick a number between 1 and 5. "))

    print(f"{pet} sounds like a nice {animal}.")
    if number == 1:
        print(f"I bet {pet} gets a bit sleepy at times - like all {animal}s.")
    elif number == 2:
        print(f"I bet {pet} gets the zips being so full of energy!")
    elif number == 3:
        print(f"I bet {pet} gets grumpy sometimes.")
    elif number == 4:
        print(f"I heard {animal}s like {pet} are very curious.")
    elif number == 5:
        print(f"I've heard {animal}s are very loyal.")
    else:
        print("You did not pick a valid number.")

describe_pet()