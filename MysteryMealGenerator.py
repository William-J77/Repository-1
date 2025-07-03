import random


main_dish_healthy = [
    "Chicken salad",
    "Sushi",
    "Salmon",
]

side_dish_healthy = [
    "side salad",
    "fruit",
    "vegis",
]

drink_healthy = [
    "Water",
    "Tea",
    "Kombucha",
]

main_dish_indulgent = [
    "A burger",
    "Pizza",
    "Tacos",
]

side_dish_indulgent = [
    "Fries",
    "Curly fries",
    "Dumplings",
]

drink_indulgent = [
    "Soda",
    "Beer",
    "Lemonaid",
]



hungry = input("Are you hungry? (yes/no) ").strip().lower()

if hungry == "yes":
    while True:
        choice = input("Would you like something healthy or indulgent? ").strip().lower()
        if choice == "healthy":
            print(f"Your main dish is {random.choice(main_dish_healthy)}.")
            print(f"Your side dish is {random.choice(side_dish_healthy)}.")
            print(f"Your drink is {random.choice(drink_healthy)}.")
            break
        elif choice == "indulgent":
            print(f"Your main dish is {random.choice(main_dish_indulgent)}.")
            print(f"Your side dish is {random.choice(side_dish_indulgent)}.")
            print(f"Your drink is {random.choice(drink_indulgent)}.")
            break
        else:
            print("That is not a valid choice. Please type 'healthy or 'indulgent'. ")

elif hungry == "no":
    print("Then what are you doing at the fridge?")

    