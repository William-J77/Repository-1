import random

def build_mission(hero, power, location):

    hero_raw = hero.strip().title()
    power_raw = power.strip().lower()
    location_raw = location.strip().title()

    message = ""
    message += "You have activated the Super Hero Mission Builder!\n"
    message += "Mission Briefing: Your hero's name is " + hero_raw + "!\n"
    message += "Mission Briefing: Your hero's power is " + power_raw + "!\n"
    message += "Mission Briefing: Your hero's location is " + location_raw + "!\n"

    if power_raw == "invisibility":
        message += "They'll never see you coming!!!"
    elif power_raw == "fart clouds":
        message += "I hope they're not dad SBD farts!"
    else:
        hpower = [
            "Power up!",
            "Good choice!",
            "Your nemesis is going down!",
            "Save the city, hero!",
        
            ]
        message += random.choice(hpower)

    return message

while True:


    hero_raw = input("What is the name of your hero? ").strip()
    if hero_raw.lower() == "quit":
        break

    power_raw = input("What is your hero's power? ").strip()
    if power_raw.lower() == "quit":
        break

    location_raw = input("Where does your hero protect? ").strip()
    if location_raw.lower() == "quit":
        break

    result = build_mission(hero_raw, power_raw, location_raw)
    print(result)

    
