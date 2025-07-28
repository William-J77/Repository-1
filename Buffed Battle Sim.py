

buff = 0
life = 5
enemy = 5

def add_buff(x):
    global buff
    buff += x

def attack_seq(a):
    global enemy
    global buff
    enemy -= a
    buff = 0
    return enemy

def calc_total_damage():
    global buff 
    buff += 1
    return buff

while True: 
    print("\n\nYour enemy approaches! \nWhat will you do?")
    choice = input("\nBuff / Attack / Status / Quit? \n> ").strip().lower()
    if choice == "quit":
        print("\nRun away! Run away, sir Robin!!!")
        break
    elif choice == "buff":
        add_buff(2)
        print(f"\nYou're buffed an extra {buff} points to your attack!")
    elif choice == "attack":
        if enemy > 0:
            damage = calc_total_damage()
            attack_seq(buff)
            print(f"\nYou swing your sword at the enemy for {damage} points of damage! Enemy has {enemy} health left!")
    elif choice == "status":
        print(f"\nYou have {life} health. \nYour buff level is {buff}. \nEnemy has {enemy} health left.")
    else:
        print("\nNot a valid choice. Choose again!")
    if enemy <= 0:
            print(f"\nYou defeated your enemy with {life} health left!")
            break
    
    # enemy more health, enemy attacks, attack are random number between 1-5