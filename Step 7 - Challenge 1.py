def give_treat(name, snack, drink):
    if name.strip() == "":
        print("Hello, mysterious stranger!")
    else:
        print("Hello, " + name.title() + "!")
        
    print("Here's your favorite snack: " + snack.lower() + ".")
    print("Here's your favorite drink: " + drink.lower() + "!")
        

    if snack.lower() == "pizza":
        print("That's a classic choice!")
    elif snack.lower() == "carrots":
        print("Very Healthy!")
    elif snack.lower() == "onion rings":
        print("Hey, that's kinda gross.")
    elif snack.lower() == "glue":
        print("Please don't eat that.")
    else:
        print("Hmm... Interesting taste!")

    if drink.lower() == "water":
        print("Staying Hydrated, nice.")
    elif drink.lower() == "soda":
        print("Classic fizzy choice!")
    elif drink.lower() == "coffee":
        print("Fueling up, huh?")
    else:
        print("Interesting drink!")

give_treat("Jimmy", "pizza", "water")
give_treat("William", "carrots", "soda")
give_treat("Alex", "pudding", "coffee")
give_treat("Jimbo", "onion rings", "Tang")
give_treat(" ", "toquitos", "butter beer")
