

ingredients = []
amounts = []

print("\nList your five magical ingredients.\n")

for i in range(5):
    ingredient = input(f"Ingredient #{i + 1}: ").strip().lower()
    ingredients.append(ingredient)
    amount = int(input(f"How many units of {ingredient}? "))
    if amount > 10:
        print("Too powerful!")
    elif amount < 3:
        print("Too weak...")
    else:
        print("Just right.")
    amounts.append(amount)

for i in range(len(ingredients)):
    print(f"\n{amounts[i]} units of {ingredients[i]}.")

for i in range(len(ingredients)-1, -1, -1): #This is (start, stop, step) - not list amount
    for _ in range(amounts[i]):
        print(f"{ingredients[i]}!")