import random

def dream_trip(name, destination, travel_method):
    message = ""
    message += "Hello, " + name.title() + "! Welcome to The Dream Trip Planner.\n"
    message += "Your destination is " + destination.title() + "!\n"
    message += "You will travel by " + travel_method.lower() + "!\n"
    
    if travel_method == "dragon":
        message += "Been watching GOT, have you?"
    elif travel_method == "teleportation":
        message += "Beam me up, Scotty."
    elif travel_method == "car":
        message += "Boring."
    else:
        tips = [
            "Let's get out there!",
            "Pack some snack and gooooo!",
            "Don't forget a towel!",
            "A weather check would be smart.",
        ]
        message += random.choice(tips)

        
    return message

while True:
    name_raw = input("What is your name? ").strip()
    destination_raw = input("Where would you like to go? ").strip()
    travel_method_raw = input("How would you like to travel? ").strip()

    if name_raw.lower() == "quit" or destination_raw.lower() == "quit" or travel_method_raw.lower() == "quit":
        break
    if name_raw.lower() == "help" or destination_raw.lower() == "help" or travel_method_raw.lower() == "help":
        print('If you need help, you should probably leave by typing "quit".')
        continue

    name = name_raw.title()
    destination = destination_raw.title()
    travel_method = travel_method_raw.lower()

    result = dream_trip(name, destination, travel_method)
    print(result)
    print()
