

team = []

print("\nWho's on your team?\n")

for i in range(3):
    name = input(f"Name #{i + 1} ").strip().title()
    team.append(name)
    
for name in team:
    chant = int(input(f"How many times should I chant {name}? "))
    for _ in range(chant):
        print(f"{name}!")

print (f"Here's your team:\n {' '.join(team)}")