


def calculate_damage(base_attack, weapon_bonus):
    total_damage = base_attack + weapon_bonus
    return total_damage

base_attack = int(input("\nWhat is the base attack? "))
weapon_bonus = int(input("\nWhat is the weapons bonus? "))

result = calculate_damage(base_attack, weapon_bonus)
print(result)
