

member_names = []

custom_chants = []

print("\nEnter your three band members!\n")

for i in range(3):
    member = input(f"Band Member #{i + 1}: ").strip().title()
    member_names.append(member)

for h in range(3):
    chant = input(f"\nWhat chant should go with Band Member #{h+ 1}? ").strip()
    custom_chants.append(chant)

for i in range(len(member_names)):
    amount = int(input(f"\nHow many times should I chant {member_names[i]}'s chant? "))
    for _ in range(amount):
        print(f"{custom_chants[i]}!")



print(f"\nThe concert is over! What a show!\nSpecial thanks to {" " .join(member_names)}")