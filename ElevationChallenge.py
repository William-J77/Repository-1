

elevation = int(input("How high is the mountain's elevation in feet? "))
current_e = int(input("What is your current elevation in feet? "))
distance = abs(elevation - current_e)
if distance == 0:
    print("You're at the summit!")
elif distance <= 1000:
    print(f"STORM WARNING! Watch for harsh weather and seek shelter if you need to! You're {distance} feet away from the summit.")
else:
    print(f"You're {distance} feet away from the summit. Keep going!")