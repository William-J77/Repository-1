

ingredients = []
grams = []

print("\nList your ingredients and then how many grams you wish to use.\n")

for i in range(3):
    ingredient = input(f"Ingredient #{i + 1}: ").strip().lower()
    gram_amount = int(input(f"How many grams of ingredient #{i + 1}? "))
    ingredients.append(ingredient)
    grams.append(gram_amount)

print("\nYou will need:\n")

for i in range(len(ingredients)):
    print(f"{grams[i]} grams of {ingredients[i]}.")