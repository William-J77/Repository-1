

gear_items = []

ratings = []

print("\nEnter your 4 gear items, then enter their condition.\n")

for i in range(4):
    gear = input(f"Gear item #{i + 1}: ").strip().lower()
    gear_items.append(gear)
    rating = int(input(f"What is the condition rating for {gear} (1-10)? "))
    if rating < 3:
        print(f"Your {gear} is broken.")
    elif rating >= 8:
        print(f"Your {gear} is in good condition.")
    else:
        print(f"Your {gear} needs repair. ")
    ratings.append(rating)

for i in range(len(gear_items)):
    print(f"\n{gear_items[i]} is in condition {ratings[i]}.")
    if ratings[i] < 3:
        print(f"Your {gear_items[i]} is broken.")
    elif ratings[i] >= 8:
        print(f"Your {gear_items[i]} is in good condition.")
    else:
        print(f"Your {gear_items[i]} needs repair. ")
