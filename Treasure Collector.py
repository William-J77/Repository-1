

treasures = []

while True:
    treasure = input("\nWhat treasure have you found? (Type 'done' to quit) ").strip().lower()
    if treasure == "done":
        print("\nHere are all the treasures you found: " + ", ".join(treasures))
        break
    else:
        treasures.append(treasure)