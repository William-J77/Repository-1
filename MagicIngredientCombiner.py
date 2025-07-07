

def combine_ingredients(ing1, ing2, ing3, ing4):
    message = ""
    message += f"You have picked {ing1} for a bubbling effect.\n"
    message += f"You have picked {ing2} for a glowing effect.\n"
    message += f"You have picked {ing3} for a freezing effect.\n"
    message += f"You have picked {ing4} for a growing effect."
    return message
            


ing1 = input("Please list ingredient #1: ").strip().lower()
ing2 = input("Please list ingredient #2: ").strip().lower()
ing3 = input("Please list ingredient #3: ").strip().lower()
ing4 = input("Please list ingredient #4: ").strip().lower()

print(combine_ingredients(ing1, ing2, ing3, ing4))