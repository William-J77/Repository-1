


gold = 50

def find_treasure():
    global gold
    gold += 50
    print(f"Inside function: {gold}")

find_treasure()
print(f"Outside function: {gold}")