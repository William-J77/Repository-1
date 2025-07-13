

spells = []

chant_counts = []

print("What be your magic spells three?\n")

for i in range(3):
    spell = input(f"Spell #{i + 1}: ").strip().lower()
    spells.append(spell)

for i in range(len(spells)):
    times = int(input(f"How many times should I chant spell {i + 1}? "))
    chant_counts.append(times)

for i in range(len(spells)):
    for _ in range(chant_counts[i]):
        print(f"{spells[i]}!")