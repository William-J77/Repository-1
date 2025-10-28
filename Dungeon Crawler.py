import random



class Hero: #Hero - player chooses name and weapon and starts at level 1.
  def __init__(self, name, weapon): #parameters - temporary variables that only exist in object creation.
    self.name = name #Attributes defined with self - perminant properties of the object itself - things the hero starts with automatically - live inside instance and can be used anywhere in class and even outside.
    self.weapon = weapon
    self.level = 1
    self.attack_power = self.level * 2
    self.health = self.level * 5
    self.max_health = self.level * 5
    self.XP = 0
    self.is_dead = False
    self.inventory = []
  
  def __repr__(self): #These are methods.
    #printing a player name will tell name , weapon, current health, attack power and level.
    return "{name} is level {level} with a current health of {health}. \n {name} wields a {weapon} with an attack power of {attack_power}. Formidable!".format(name = self.name, level = self.level, health = self.health, weapon = self.weapon.name, attack_power = self.attack_power)

  def level_up(self):
    if self.XP >= 2:
      self.level += 1
      self.XP = 0
      self.attack_power = self.level * 2
      self.max_health = self.level * 5
      self.health = self.max_health
      print(f"{self.name} reached level {self.level}!")

  def attack(self, enemy):
    ap_plus_weapap = self.attack_power + self.weapon.attack_power
    damage = random.randint(1, ap_plus_weapap)
    enemy.health -= damage
    print(f"{self.name} hit {enemy.name} for {damage}!")
    if enemy.health <= 0:
      self.XP += 1
      print(f"{self.name} has defeated {enemy.name}!")
      self.level_up()

    

class Room:
  def __init__(self, name):
      self.name = name
      # Navigation
      self.north = None
      self.south = None
      self.east = None
      self.west = None
      # content generation
      self.enemies = random.choice([None, "Goblin", "Skeleton", "Giant_Spider"])
      self.chest = random.choice([True, False])
      # If the room has a chest, create a Chest instance; otherwise, set it to None
      if self.chest:
          self.chest_obj = Chest()
      else:
          self.chest_obj = None
      self.room_type = random.choice([
          "candle lit cold stone room",
          "burning torch lit wooden walled hallway",
          "dirt floor dimly lit basement room",
          "nearly pitch dark creaking wood floor room"
      ])
    
  def __repr__(self): #description of each room.
    # room info
    situation = f"You enter a {self.room_type}.\n" 
    # enemy description
    if self.enemies:
      situation += f"A {self.enemies} approaches from a corner!\n"
    else:
      situation += f"No enemies in this room.\n"
    # chest description
    if self.chest:
      if self.enemies:
        situation += f"The guarded chest sits in the corner.\n"
      else:
        situation += f"An old wooden chest sits against the far wall.\n"
    else:
      situation += f"... An otherwise empty room is before you.\n"
    # exits
    situation += f"\nExits: North, South, East, West.\n"
    return situation


class Weapon:
  def __init__(self, name, attack_power, speed):
    self.name = name
    self.attack_power = attack_power
    self.speed = speed


class Chest:
  def __init__(self):
    self.chest = True
    self.inventory = []
    
  def open_chest(self, hero):
    if self.chest:
      new_weapon = random.choice(possible_weapons)
      hero.inventory.append(new_weapon)
      choice = input(f"\nYou found {new_weapon.name}! Do you wish to equip {new_weapon.name}? (yes/no)").strip().lower()
      if choice == "yes":
        hero.weapon = new_weapon
        print(f"You are now wielding a {hero.weapon.name}.\n")
    else:
      print("The chest is empty.\n")
    self.chest = False



class Goblin:
  def __init__(self):
    self.name = "Goblin"
    self.level = 1
    self.health = 5
    self.attack_power = 2
    self.is_dead = False

  def attack(self, hero):
    dmg_roll = random.randint(0, self.attack_power)
    hero.health -= dmg_roll
    print(f"The Goblin hit {hero.name} for {dmg_roll}! {hero.name} has {hero.health} health left!")
    if hero.health <= 0:
      print(f"{hero.name} has perished at the hands of a dirty Goblin!")




class Skeleton:
  def __init__(self):
    self.name = "Skeleton"
    self.level = 1
    self.health = 7
    self.attack_power = 4
    self.is_dead = False

  def attack(self, hero):
    dmg_roll = random.randint(0, self.attack_power)
    hero.health -= dmg_roll
    print(f"The Skeleton hit {hero.name} for {dmg_roll}! {hero.name} has {hero.health} health left!")
    if hero.health <= 0:
      print(f"{hero.name} has perished at the hands of a Skeleton!")



class Giant_Spider:
  def __init__(self):
    self.name = "Giant Spider"
    self.level = 2
    self.health = 9
    self.attack_power = 6
    self.is_dead = False

  def attack(self, hero):
    dmg_roll = random.randint(0, self.attack_power)
    hero.health -= dmg_roll
    print(f"The Giant Spider hit {hero.name} for {dmg_roll}! {hero.name} has {hero.health} health left!")
    if hero.health <= 0:
      print(f"{hero.name} has perished at the hands of a Giant Spider!")
  
possible_weapons = [
  Weapon("Rusty blade", 2, 4),
  Weapon("Two handed Dwarven axe", 6, 2),
  Weapon("Elvish blade", 4, 5),
  Weapon("Two handed claymore", 6, 2),
  Weapon("Matching Elvish daggers", 3, 6),
  Weapon("Broadsword of Power", 7, 4),
  Weapon("Sharpened spear", 5, 2),
  Weapon("Wooden club", 5, 3),
  Weapon("Whip of slashing", 3, 3),
  Weapon("A dull butter knife", 1, 1),
  Weapon("A sharp stick", 1, 1)
]

# save for later - health - power? - speed? - death message?
possible_potions = [

]

def main():
  print("\nWelcome to The Dungeon Of The North!\n")
  print("\n... A dungeon crawler by W. A. Johnson\n")
  player_name = input("\nWho dares enter the Dungeon Of The North? \n").strip().title()
  wooden_sword = Weapon("Wooden Sword", attack_power = 1, speed = 1)
  player_hero = Hero(player_name, wooden_sword)
  print(f"\nWelcome {player_hero.name}!\n")
  print("\nPrepare yourself!\n")

  while player_hero.health > 0:
    current_room = Room("Dungeon Room")
    print(current_room)

    if current_room.enemies == "Goblin":
      enemy = Goblin()
    elif current_room.enemies == "Skeleton":
      enemy = Skeleton()
    elif current_room.enemies == "Giant Spider":
      enemy = Giant_Spider()
    else:
      enemy = None
    
    if enemy:
      print(f"A {enemy.name} wishes your death!")
      while player_hero.health > 0 and enemy.health > 0:
        choice = input("\nWill you \n1. Attack \n2. Run to next room? (type 1 or 2)").lower().strip()
        if choice == "1":
          player_hero.attack(enemy)
          if enemy.health <= 0:
            player_hero.XP += 1
            print(f"{player_hero.name} has defeated {enemy.name}!")
            player_hero.level_up()  # handles leveling if XP threshold reached
            print(f"{player_hero.name} is now level {player_hero.level} with {player_hero.XP} XP.")
            break
          else:
            enemy.attack(player_hero)
            if player_hero.health <= 0:
              print(f"{player_hero.name} has died.")
              break
        elif choice == "2":
          print(f"{player_hero.name} escaped the enemy into the next room!")
          break
        else:
          print("Invalid choice, please try again.")
    else:
      print("The room is empty. You move on... \n")

    if current_room.chest_obj:
        print("\nYou see a chest in the room...\n")
        current_room.chest_obj.open_chest(player_hero)
    else:
        print("\nThere is not a chest in this room.")
    


  print("Game Over. You have perished in the dungeon.")

# file now only runs if this file is the main program
if __name__ == "__main__":
  main()