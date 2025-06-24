#def snack_drink(snack, drink):
#    if snack == "pizza":
#        print ("Pizza is the best!")
#    if drink == "coffee":
#        print ("Coffee keeps you going!")
        
#    return "Great choices."

#print(snack_drink("pizza", "coffee"))
#print(snack_drink("yogurt", "coffee"))
#print(snack_drink("salad", "milk"))


#def pet_match(name, animal, home_size):
#    print("Hello " + name.title() + "!")

#    if animal == "ferrets":
#       print("You like " + animal.lower() + "? You're wild!")
#    elif animal == "unicorns":
#        print("You like " + animal.lower() + "? Those aren't real!")
#    else:
#        print(animal.title() + " is a cool choice.")

#    if home_size == "small":
#        print("Try a hamster.")
#    elif home_size == "medium":
#        print("Maybe a dog.")
#    elif home_size == "large":
#        print("A horse, perhaps?")
#    else:
#        print("Hmm... not sure what fits that size.")
    

#pet_match("jim", "ferrets", "large")
#pet_match("bob", "unicorns", "medium")
#pet_match("jOe", "cats", "small")


def game_loadout(name, weapon, skill_level):
    weapon_clean = weapon.strip().lower()
    skill_clean = skill_level.strip().lower()
    
    message = "Welcome " + name.title() + "! Ready for battle?\n"

    if weapon_clean == "blaster":
        message += "Nothing like a good blaster at your side, kid.\n"
    elif weapon_clean == "lightsaber":
        message += "Ah, a jedi's weapon.\n"
    else:
        message += "Yeah, good luck with that business.\n"

    if skill_clean == "beginner":
        message += "You may want to start slow there and stay in the shallow end.\n"
    elif skill_clean == "normal":
        message += "Normal like a normie.\n"
    elif skill_clean == "advanced":
        message += "Bring on the pain.\n"
    else:
        message += "Unknown skill level. This could get weird.\n"

    return message
    
print (game_loadout("Jimmy", "Blaster", "BEGINNER"))
print (game_loadout("Luke", "Lightsaber", "advanced"))
print (game_loadout("Paul", "knife", "normal"))
print (game_loadout("george", "grapling hook", "ready for death"))
