
while True:
    print("I have information for the following planets:\n")

    print("   1. Venus   2. Mars    3. Jupiter")
    print("   4. Saturn  5. Uranus  6. Neptune\n")

    planet = int(input("Which planet are you going to? (1-6) "))
    
    weight = 185


    # Write an if statement below:

    if planet == 1:
        weight = 185 * 0.91
    elif planet == 2:
        weight = 185 * 0.38
    elif planet == 3:
        weight = 185 * 2.34
    elif planet == 4:
        weight = 185 * 1.06
    elif planet == 5:
        weight = 185 * 0.92
    elif planet == 6:
        weight = 185 * 1.19
    else:
        print("Not a valid planet number.")
        continue

    print(f"\nYour weight on planet {planet} is {weight}.\n")
  