

def calc_total_healing(strength, player_level):
    if player_level >= 20:
        total = strength * 2
    elif player_level > 10:
        player_level += 5
        total = strength * player_level
    else:
        total = strength * player_level
    

    if total > 100:
        print("Healing is capped at 100 you beast!")
        total = 100

    return f"You healed for {total} HP!"
    

level = int(input("\nWhat is your level? "))
if level > 10:
    print("You get a +5 bonus for a high level!")
strong = int(input("What is your stength? "))

healing = calc_total_healing(strong, level)
print(healing)  

# still kind of broken