import random

buff = 0
life = 10
enemy = 10

def add_buff(x):
    global buff
    buff += x

def attack_seq(a):
    global enemy
    global buff
    global life
    enemy -= a
    buff = 0
    enemy_damage = 0
    if enemy > 0:
            enemy_damage = random.randint(1, 5)
            life -= enemy_damage
    return enemy, life, enemy_damage

def calc_total_damage():
    global buff 
    buff += 1
    return buff

while True: 
    print("\n\nYour enemy approaches! \nWhat will you do?")
    choice = input("\nBuff / Attack / Block / Status / Quit? \n> ").strip().lower()
    if choice == "quit":
        print("\nRun away! Run away, sir Robin!!!\n")
        break
    elif choice == "buff":
        add_buff(2)
        print(f"\nYou're buffed an extra {buff} points to your attack!")
    elif choice == "attack":
        if enemy > 0:
            damage = calc_total_damage()
            enemy, life, enemy_damage = attack_seq(buff)
            print(f"\nYou swing your sword at the enemy for {damage} points of damage! Enemy has {enemy} health left!")
            print(f"The enemy hits you for {enemy_damage} damage! You have {life} hit points left.")
    elif choice == "status":
        print(f"\nYou have {life} health. \nYour buff level is {buff}. \nEnemy has {enemy} health left.\n")
    elif choice == "block":
        print("\nYou raise your shield to block! The enemy's attack is stopped by your shield!")
    else:
        print("\nNot a valid choice. Choose again!")
    if enemy <= 0:
            print(f"\nYou defeated your enemy with {life} health left!\n")
            break
    if life <= 0:
            print(f"\nYou have been defeated! The enemy has {enemy} hit points left.\n")
            break
