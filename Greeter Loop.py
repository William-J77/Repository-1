import random

while True:

    print("Welcome to the Greeter Loop!")
    print('Type "help" for options or "quit" to exit.')
    
    raw_input = input("What is your name? ")
    name = raw_input.strip().lower()
    name_pretty = raw_input.strip().title()

    if name == "quit":
        print("Goodbye.")
        break
    elif name == "help":
        print("This program can give you a nice greeting, as well as a few fun custom messages.")
    else:

        if name == "jimmy":
            print("Jimmy is not here right now. Please leave a message after the beep.")
        elif name == "william":
            print("William is down at the corner store.")
        else:
            print("Nice to meet you, " + name_pretty + "!")
        

        mood = input("How are you doing? (good/bad/okay)")
        mood_response = mood.strip().lower()

        if name == "william" and mood == "bad":
            print("Turn that frown upside down, my friend!")
        # elif name == "jimmy" and mood == "good":
            # print("That's one happy Jimmy.")
        elif mood == "good":
            good_responses = [
                "Oh good!",
                "Let the good times roll.",
                "Kick out the jams mother...!!!",
                "Well playd. Good on you, sir or lady.",
                "So glad to hear it.",
                "I'm not sure I believe all this optimism."
            ]
            print(random.choice(good_responses))
        elif name == "alex" and mood == "okay":
            print("That Alex is feeling a-okay.")
        elif mood_response == "good":
            print("That's great to hear!")
        elif mood_response == "bad":
            print("I'm sorry to hear that.")
        elif mood_response == "okay":
            print("Okay is okay.")
        else:
            print("That is not a proper response. Terminate.")
            
    
        vip_input = input("Are you a VIP? (yes/no)")
        vip_input_clean = vip_input.strip().lower()

        if name == "william" or name== "jimmy" or vip_input_clean == "yes":
            print("You're on the VIP list!")
        else:
            print("Sorry, you're not on the list.")

