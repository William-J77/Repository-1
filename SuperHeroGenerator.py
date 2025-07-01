print("🔥 RUNNING SUPERHERO SCRIPT")
while True: # this is what keeps the program looping

# these lines define string and integer variables
    
    name = input("What is you name? \n")
    color = input("What is your favorite color? \n")
    power = input("Pick a power: flight, invisibility, or strength \n")
    villains = int(input("How many villains have you defeated? \n"))
    henchmen = (villains * 3)

# this is cleaning so inputs don't get confused
    name_clean = name.title()
    color_clean = color.title()
    power_clean = power.strip()

# this is the main outputprint section
    print(f"Your superhero name is: The {color_clean} {name_clean}!")


    if power == "flight":
        print("Your power is: To soar above your enemies and attack from the skies like Arch Angel!")
        print("Mission: Protect the skies.. Airplanes.. Birds... I guess")
    elif power == "invisibility":
        print("Your power is: To cloud men's minds like The Shadow. You're invisible!")
        print("Mission: Be like Alex Baldwin!")
    elif power == "strength":
        print("Your power is: Super strength like The Hulk!")
        print("Mission: Keep it together there, Banner.")
    else:
        print(f"Your power is {power_clean}! A curious choice.")
        print("Mission: How about you just go protect the city with that.")

    print(f"You have defeated {villains} of the big bad guys and probably {henchmen} underlings!")
    if villains in range(10, 111):
        print("Legendary!")
    if villains in range(0, 10):
        print("You're just starting out. New in town?")

# this is the choose to quit or make another section
    make_another = input("Would you like to create another hero? (yes/no?) ")
    if make_another == "no":
            break

