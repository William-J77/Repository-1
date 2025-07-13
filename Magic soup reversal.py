

ingredients = []

scoops = []

print("\nPlease list your three ingredients.\n")

for i in range(3):
    ingredient = input(f"Ingredient # {i + 1}: ").strip().lower()
    ingredients.append(ingredient)
    scoop = int(input(f"How many scoops of {ingredient}? "))
    scoops.append(scoop)

for i in range(len(ingredients) -1, -1, -1):
    print(f"You will need {scoops[i]} scoops of {ingredients[i]}.")