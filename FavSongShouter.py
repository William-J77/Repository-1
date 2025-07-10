

print("What are your three favorite songs?\n")

song1 = input("Song #1 ").strip().title()
song2 = input("Song #2 ").strip().title()
song3 = input("Song #3 ").strip().title()

shout1 = int(input("How many times should I shout the first song? \n"))
shout2 = int(input("How many times should I shout the second song? \n"))
shout3 = int(input("How many times should I shout the third song? \n"))

for _ in range(shout1):
    print(f"{song1}!")

for _ in range(shout2):
    print(f"{song2}!")

for _ in range(shout3):
    print(f"{song3}!")

    # It is common to use underscore for the loop variable
