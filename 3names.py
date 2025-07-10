

names = []

print("\nPlease enter three names.\n")

for i in range(3):
    name = input(f"Name #{i + 1}: ").strip().title()
    names.append(name)

print(f"Here are your names: \n{' '.join(names)}")