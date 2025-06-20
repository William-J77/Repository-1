while True:
    name = input("What is your name? ").title()
    
    if name == "Quit":
        print("Welp, smell ya later!")
        break
    elif name == "John":
        print("Ah, John. The legend returns. ")
    elif name == "Jimmy":
        print("Hey, Jimmy! Good to see you again. ")
    else:
        print("Nice to meet you, " + name + ".")
