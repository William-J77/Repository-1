def give_snack(name, snack):
    print("Hello, " + name.title() + "!")
    print("Here's your favorite snack: " + snack.lower() + ".")

    if snack.lower() == "pizza":
        print("That's a classic choice!")
    elif snack.lower() == "carrots":
        print("Very Healthy!")
    elif snack.lower() == "onion rings":
        print("Hey, that's kinda gross.")
    else:
        print("Hmm... Interesting taste!")

give_snack("Jimmy", "pizza")
give_snack("William", "carrots")
give_snack("Alex", "pudding")
give_snack("Jimbo", "onion rings")


    

    

    

