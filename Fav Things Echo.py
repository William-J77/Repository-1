

print("What are three of your favorite things?")

one = input("#1: ").strip().lower()
two = input("#2: ").strip().lower()
three = input("#3: ").strip().lower()

repeats = int(input("\nHow many times should we repeat each one? "))

favorites = [
    one,
    two, 
    three,
]

for favorite in favorites:
    for _ in range(repeats):
        print(f"{favorite} is one of your favorite things.")