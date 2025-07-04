

steps = int(input("How many steps did you take today? "))
if steps in range(0, 5000):
    print("You're just getting started!")
if steps in range(5000, 10000):
    print("Nice effort! You're getting there!")
if steps >= 10000:
    print("Amazing! You crushed it today!")