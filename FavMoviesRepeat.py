

print("\nList your three favorite films!")

film1 = input("Film #1: ").strip().title()
film2 = input("Film #2: ").strip().title()
film3 = input("Film #3: ").strip().title()

shout_amount = int(input("How many times to shout movie #1? "))

for i in range(shout_amount):
    print(f"{film1}!")

shout_amount = int(input("How many times to shout movie #2? "))

for i in range(shout_amount):
    print(f"{film2}!")

shout_amount = int(input("How many times to shout movie #3? "))

for i in range(shout_amount):
    print(f"{film3}!")