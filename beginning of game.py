import random

strength = 10
player_level = 12
max_health = 100
current_health = 40
enemy_health = 50



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

    return total

def calc_total_damage(strength, level):
    new_attack = strength + level + random.randint(1, 10)
    return new_attack

def basic_action():
    global current_health
    while True:
        choice = input("What would you like to do?: \nAttack\nHeal\nStatus\nQuit\n> ").strip().lower()
        if choice == "quit":
            print("Good bye!")
            break
        elif choice == "status":
            print("You are healthy and ready for battle.")
        elif choice == "heal":
            healing = calc_total_healing(strength, player_level)
            new_health = current_health + healing
            if new_health > max_health:
                new_health = max_health
            print(f"You healed for {healing} HP!")
            print(f"Your health is now {new_health}/{max_health}.")
            current_health = new_health
        elif choice == "attack":
            global enemy_health
            attacking = calc_total_damage(strength, player_level)
            enemy_health -= attacking
            print(f"You hit enemy for {attacking}!\nEnemy is now at {enemy_health} HP.")

        else:
            print("Not a valid choice.")

basic_action()

