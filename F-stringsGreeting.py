


name = input(f"What is your name? \n")
year = int(input("What year were you born? \n"))

print(f"Hello, {name.title()}. You are {2025 - year} years old.\n")
print(f"You will be {2025 - year + 10} years old in ten years.\n")

# in is great for checking membership - works with range, list, str etc. Common in if statements.

if year in range(1966, 2008):
    print("You are an adult. Get a job and vote.")
elif year in range(2008, 2025):
    print("You are a kid. Go have fun.")
elif year in range(1900, 1966):
    print("You are a senior citizen. Go to bed early.")