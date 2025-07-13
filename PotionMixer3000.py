

ingredients = []

spoonfulls = []

print("\nWelcome to the Potion Mixer 3000\nPlease enter your 3 ingredients.\n")

for i in range(3):
    ingredient = input(f"Ingredient #{i + 1}: ").strip().lower()
    ingredients.append(ingredient)
    spoonfull_amount = int(input(f"How many spoonfulls of ingredient {ingredients}? "))
    spoonfulls.append(spoonfull_amount)

for i in range(len(spoonfulls)):
    print(f"You must prepare {spoonfulls[i]} spoonfulls of {ingredients[i]}.")