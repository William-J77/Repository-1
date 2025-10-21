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
    self.room_type = random.choice(["candle lit cold stone room", "burning torch lit wooden walled hallway", "dirt floor dimly lit basement room", "nearly pitch dark creaking wood floor room"])
    
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


#needs level_up check method, XP gained
class Goblin:


#needs level_up check method, XP gained
class Skeleton:


#needs level_up check method, XP gained
class Giant_Spider:
  
possible_weapons = [
  Weapon("Rusty blade", 2, 4),
  Weapon("Two handed Dwarven axe", 6, 2),
  Weapon("Elvish blade", 4, 5),
  Weapon("Two handed claymore", 6, 2),
  Weapon("Matching Elvish daggers", 3, 6),
  Weapon("Broadsword of Power", 7, 4),
  Weapon("Sharpened spear", 5, 2),
  Weapon("Wooden club", 5, 3),
]

# save for later - health - power? - speed?
possible_potions = [

]
wooden_sword = Weapon("WoodenSword", attack_power = 1, speed = 1)
player_name = input("Enter your hero's name: ").strip()
player_hero = Hero(player_name, wooden_sword)
chest = Chest()
chest.open_chest(player_hero)
