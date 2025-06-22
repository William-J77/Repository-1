import random

while True:

    name = input("What is your name? Type quit or help for more information.")
    name_clean = name.strip().lower()
    name_pretty = name.strip().title()

    if name_clean == "quit":
        break
    elif name_clean == "help":
            print("The Greeting System is simply here to greet you. Learn more Python.")
            continue

    print("Hello human " + name_pretty + "! Welcome to the Greeting System")

    if name_clean == "jimmy":
        print("A special hello to you, Jimmy")
    elif name_clean == "william":
        print("Ah yes, the William has arrived.")
    else:
       print("Nice to meet you " + name_pretty + "!")

    mood_rep = input("How are you feeling today? (good/bad/okay)").strip().lower()
    
    if name_clean == "william" and mood_rep == "bad":
        print("I'm sorry you're not feeling well today, William.")
    elif name_clean == "jimmy" and mood_rep == "good":
        print("Glad to hear it, Jimmy.")
    elif name_clean == "alex" and mood_rep == "okay":
        print("OK Alex! You're part of the okay bunch!")
    elif mood_rep == "good":
        good_answers = [
            "Glad to hear that.",
            "Bring on the happiness.",
            "Keep on truckin.",
            "Right on.",
        ]
        print(random.choice(good_answers))
    elif mood_rep == "bad":
        print("Sorry to hear that, friend.")
    elif mood_rep == "okay":
        okay_answers = [
            "Okay is OK!",
            "Well all righty then.",
            "That's fair to midland.",
            "Well okay then.",
            ]
        print(random.choice(okay_answers))

    vip = input("Are you a VIP? (yes/no)").strip().lower()

    if vip == "yes" and (name_clean == "jimmy" or name_clean == "william"):
        print("VIP confirmed.")
    else:
        print("Not on the list.")

    

    

    

