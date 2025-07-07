import random

def make_robot(core, body_mat, toolweap, personality):
    message = "\n"
    message += f"Your robot's core processor will be a {core}.\n"
    message += f"Your robot's body material will be: {body_mat}.\n"
    message += f"Your robot's tool or weapon will be: {toolweap}.\n"
    message += f"Your robot's personality trait will be {personality}.\n"
    message += f"Your robot will have a {core} processor, be made of {body_mat}, wield a {toolweap}, and be of the personality type: {personality}.\n"
    return message

while True:
    core = input("Welcome to the Robot Creator! Let's start by choosing a core processor: \n").strip()
    body_mat = input("What body material do you want?: \n").strip().lower()
    toolweap = input("What tool or weapon will it have?: \n").strip().lower()
    personality = input("What personality trait will it have?: \n").strip().lower()

    print(make_robot(core, body_mat, toolweap, personality))

    name = [
        "Metal head!",
        "Jimmy the clapper!",
        "Manny McMetalhands",
        "Chat GPT",
        "Charles the groovy robot",
    ]

    robot_name = random.choice(name)

    print(f"Your robot's name will be {robot_name}!")

    build_again = input("Would you like to build another? (yes/no)\n").strip().lower()
    if build_again == "yes":
        continue
    elif build_again == "no":
        print("Bye!")
        break