import random

enemies = ["Goblin", "Troll", "Skeleton"]

player_life = 12


for enemy in enemies:
    damage = random.randint(2, 6)
    player_life -= damage
    print(f"\n{enemy} hits you for {damage} damage! You have {player_life} hit points left!\n")

    if player_life <= 0:
        print("\nGame Over man.\n")
        break

if player_life >= 1:
    print("\nYou survived!\n")

