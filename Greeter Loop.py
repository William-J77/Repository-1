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
    elif name == "jimmy":
        print("Jimmy is not here right now. Please leave a message afeter the beep.")
    elif name == "william":
        print("William is down at the corner store.")
    else:
        print("Nice to meet you, " + name_pretty + "!")
        

        mood = input("How are you doing? (good/bad/okay)")
        mood_response = mood.strip().lower()

        if mood_response == "good":
            print("That's great to hear!")
        elif mood_response == "bad":
            print("I'm sorry to hear that.")
        elif mood_response == "okay":
            print("Okay is okay.")
        else:
            print("That is not a proper response. Terminate Terminate Terminate.")
    
