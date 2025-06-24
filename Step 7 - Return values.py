def snack_drink(snack, drink):
    if snack == "pizza":
        return "Pizza is the best!"
    if drink == "coffee":
        return "Coffee keeps your going!"
    else:
        return "Your snack is " + snack + " and your drink is " + drink + "."

print(snack_drink("pizza", "water"))
print(snack_drink("chips", "coffee"))
print(snack_drink("salad", "juice"))



