

print("\nPlease list your favorite foods!")

food1 = input("#1: ").strip().lower()
food2 = input("#2: ").strip().lower()
food3 = input("#3: ").strip().lower()

foods = [food1, food2, food3]

for food in foods:
    for _ in range(3):
        print(f"{food} is the best!")