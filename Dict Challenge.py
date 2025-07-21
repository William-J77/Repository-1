# potions = {"Healing": 50, "Fire": 70, "Ice": 60}

# def double_fire_power(potion_dict):
#   if "Fire" in potion_dict:
#      potion_dict["Fire"] *= 2
#  else:
#       print("Potion not found.")

# double_fire_power(potions)
# print(potions)

#

#potions = {"Healing": 50, "Strength": 75}


#def add_potion(potion_dict, potion_name):
 #   power = int(input(f"\nWhat is the power level of {potion_name}? "))
  #  potion_dict[potion_name] = power
  #  print(potion_dict)

#add_potion(potions, "Healing Brew")

#

#potions = {}

#def add_potion(potion_dict):
  #  to_add = input("\nWhat potion would you like to add? ").strip().title()
  #  power = int(input(f"What is the power level of {to_add}? "))
  #  potion_dict[to_add] = power
  #  print(potion_dict)

#add_potion(potions)

#

potions = {"Strength": 50, "Life": 60}


def update_potion(potion_dict): #potion_dict becomes the temp name for the dictionary given using the call update_potion(potions)
    while True:
        update = input("\nWhich potion would you like to update?(type 'done' to leave) ").strip().title()
        if update in potions:
            new_power = int(input(f"What is the new power level of {update}? "))
            potion_dict[update] = new_power
            print(potion_dict)
        elif update == "Done":
            break
        else:
            print("Potion not found.")

update_potion(potions)