

while True:
    print("Welcome to the Superhero Profile Logger\n")
    print("Let's begin\n")
    name = input("What is your name?\n")
    color = input("What is your favorite color or attribute?\n")
    power = input("What is your super power?\n")
    villains = int(input("How many villains have you defeated?\n"))
    henchmen = villains * 3

    name_clean = name.strip().title()
    color_clean = color.strip().title()
    power_clean = power.strip()

    print(f"Your Superhero's name is The {color_clean} {name_clean}!")
    print(f"You fight evil with the power of {power_clean}!")

    if villains in range(0, 10):
        print(f"Only {villains} villains? You must be a beginner. You must've defeated {henchmen} henchmen maybe?")
    if villains in range(11, 111):
        print(f"Wow! {villains} villains!? You're lgendary! You must've defeated {henchmen} henchmen too!")

    #with open("hero_log.txt", "a") as file:
    #    file.write(
    #       f"Hero: The {color_clean} {name_clean}\n"
    #        f"Power: {power_clean}\n"
    #        f"Villains Defeated: {villains}\n"
    #        f"Henchmen Defeated: {henchmen}\n"
        )

    restart = input("Would you like to create another hero? (yes/no)")
    if restart == "no":
        break