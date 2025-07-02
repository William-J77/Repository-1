import random

def get_event(battle, trap, treasure):
    forward = random.randint(1, 6)
    if forward <= 2:
        battle_round()
    if forward <= 4:
        trap_round()
    else:
        treasure_round()
    
 

def battle_round(attack, dodge, run_away):
    print("A goblin appears! Prepare for battle! Type ")

        while True:
            action = input("Do you ") #here's where you left off... 


def trap_round(health_loss, trap_death):
    print("It's a trap!")

def treasure_round(silver, gold, poo):
    print("Youhave found treasure!")

#Game intro
print("Welcome to the Goblin Dungeon!\n")
name = input("Hero! What is your name? ")
name_clean = name.strip().title()
print(f"Welcome {name_clean}! Prepare yourself!")


while True:
    action = input("Type 'forward' to explore the dungeon or 'quit' to leave: ").strip().lower()
    if action == "quit":
        break
    if action == "forward":
        get_event()
    else:
        print("Invalid input.")

    

