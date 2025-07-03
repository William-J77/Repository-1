import random

location = [
    f"You find yourself in the desert, surrounded by {random.randint(1, 11)} scorpions!",
    f"You've ventured into the mountains, being chased by {random.randint(1, 11)} trolls!",
    f"You're on a space station, running from {random.randint(1, 11)} aliens with probes!",
    f"You entered a haunted house inhabited by {random.randint(1, 11)} ghosts!",
]

companion = [
    f"Good thing your talking sword is there with you!\n",
    f"Your loyal dog is at your side - as long as you brought the treats.\n",
    f"Your robot sidekick, Blipster, is ready with the zapper!\n",
    f"Why on earth have you come alone!?\n"
]

go = input("Do you want to go on an unexpected adventure? ").strip().lower()
if go == "yes":
    print(random.choice(location))
    print(random.choice(companion))
elif go == "no":
    print("Well then, what are you doing here?\n")
else:
    print("Invalid answer, human.\n")

item = input("Choose one item to bring on your adventure! (sword, shield, or potion etc...) ").strip().lower()
if item == "sword":
    print("A sharp blade for a sharp wit!")
elif item == "shield":
    print("Come home with your shield or on it.")
elif item == "potion":
    print("Hope it's the red potion and not the green one.")
else:
    print("You have chosen...... Poorly")