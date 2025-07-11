

band_members = []

print("\nName your three band members\n")

for i in range(3):
    member = input(f"Band member #{i + 1}: ").strip().title()
    band_members.append(member)

for band in band_members:
    chant = int(input(f"How many times should I chant {band}'s name? "))
    for _ in range(chant):
        print(f"{band}!")