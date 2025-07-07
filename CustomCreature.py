

def build_creature(feat1, feat2, feat3, feat4):
    message = "\n"
    message += f"Wow, a {feat1} head!?\n"
    message += f"A {feat2} body!\n"
    message += f"{feat3} legs!\n"
    message += f"A special ability of {feat4}!\n"
    message += f"You've crafted a creature with a {feat1} head, a {feat2} body, {feat3} legs, and this special ability: {feat4}"
    return message

feat1 = input("Describe your creature's head: \n").strip().lower()
feat2 = input("Describe your creature's body: \n").strip().lower()
feat3 = input("Describe your creature's legs: \n").strip().lower()
feat4 = input("Describe your creature's special ability: \n").strip().lower()

print(build_creature(feat1, feat2, feat3, feat4))
