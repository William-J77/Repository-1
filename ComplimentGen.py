

name = input("What is your name? ").strip().title()

compliments = [
    "awesome",
    "kind",
    "smart",
    "creative",
    "a great coder"
]

print("\nHere's what we think about you:")

for compliment in compliments:
    print(f"{name}, you are {compliment}!")