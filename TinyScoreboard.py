

your_team = int(input("Enter your team's score: "))
other_team = int(input("Enter the other team's score: "))
difference = abs(your_team - other_team)
if your_team > other_team:
    print(f"You won by {difference} points!")
elif your_team < other_team:
    print(f"You lost by {difference} points!")
else:
    print("It was a tie!")