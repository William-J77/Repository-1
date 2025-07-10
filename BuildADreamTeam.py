

team = [] #This creates an empty list

print("\nWho's on your dream team?\n")

for i in range(3):
    name = input(f"Name #{i+1}: ").strip().title()
    team.append(name)

print(f"Here's your team!\n {' '.join(team)}")