

players = []

print("\nBuild your dream team by entering three player names!\n")

for _ in range(3):
    player = input(f"Player #{_ + 1}: ").strip().title()
    players.append(player)

for player in players:
    chant = int(input(f"\nHow many times should I chant player {player}'s name? "))
    for _ in range(chant):
        print(f"{player}!")