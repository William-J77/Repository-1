

def travel_plan(destination, days, activity):
    print(f"You're heading to {destination} for {days} days to enjoy some {activity}! Have fun!")


destination = input("Where are you planning to travel to? ").strip().title()
days = int(input("How many days will you be gone? "))
activity = input("What will you do while you're there? ").lstrip().lower()

travel_plan(destination, days, activity)
