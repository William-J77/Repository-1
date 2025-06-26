def describe_food_combo(food, drink, side):
    message = ""
    message += ("Let's check your order!\n")
    message += ("Your food is " + food.lower() + ".\n")
    message += ("Your drink is " + drink.lower() + ".\n")
    message += ("Your side order is " + side.lower() + ".\n")
    message += ("Nice combo!\n")
    return message

result = describe_food_combo("pizza", "soda", "fries")
print(result)
result2 = describe_food_combo("popcorn", "orange juice", "apples")
print(result2)
result3 = describe_food_combo("Carrots", "tang", "curly fries")
print(result3)
print("Cafe.")
