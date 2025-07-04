

def meal_order(food, drink, dessert):
    print(f"You ordered {food}, with {drink} for a drink, and {dessert} for dessert. ")

food = input("Food order: ").strip().lower()
drink = input("Drink order: ").strip().lower()
dessert = input("Dessert: ").strip().lower()

meal_order(food, drink, dessert)

if dessert == "cake":
    print("Cake is a great choice!")