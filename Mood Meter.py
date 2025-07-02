

feeling = int(input("On a scale from -10 to 10, how was your day? "))
neutral = 0
difference = abs(feeling)
print(f"You're {difference} points away from feeling neutral")
if feeling <= 0:
    print("Hope tomorrow is better!")
elif feeling >= 1:
    print("Wow, that's a great day!")