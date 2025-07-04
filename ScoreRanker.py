

score = int(input("Enter a score from 0 to 100. "))
if score not in range(0, 101):
    print("That score is out of range. Please enter a number between 0 and 100.")
elif score in range(0, 60):
    print("You failed. Try again.")
elif score in range(60, 80):
    print("You passed, but there's room to grow!")
elif score in range(80, 90):
    print("Great job!")
elif score in range(90, 101):
    print("Outstanding!")