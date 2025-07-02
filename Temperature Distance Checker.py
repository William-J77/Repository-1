

temp = int(input("Enter today's temperature in Fahrenheit: "))
difference = abs(temp - 32)
if temp < 32:
    print(f"You are {difference} degrees below freezing.")
else:
    print(f"You are {difference} degrees above freezing.")