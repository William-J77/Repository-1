

ingredients = []
stirs = []

print("\nEnter your four potion ingredients, mortal! The potion ingredients must be entered backwards!\n")

for i in range(4):
    ingredient = input(f"Ingredient #{i + 1}: ").strip().lower()
    ingredients.append(ingredient)
    stir = int(input(f"How many stirs of {ingredient}? "))
    stirs.append(stir)

for i in range(len(ingredients)-1, -1, -1):
    print(f"{ingredients[i]}!")
    for _ in range(stirs[i]):
        print("Stirring!")