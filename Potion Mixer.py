

ingredients = []
drop_counts = []

print("\nPlease enter three ingredients.\n")

for i in range(3):
    ingredient = input(f"Ingredient #{i + 1}: ").strip().lower()
    ingredients.append(ingredient)

for i in range(len(ingredients)):
    drops = int(input(f"How many drops of {ingredients[i]}? "))
    drop_counts.append(drops)

for i in range(len(ingredients)):
    print(f"{drop_counts[i]} drops of {ingredients[i]}")