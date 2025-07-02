from random import randint

secret = randint(1, 50)

while True:
    guess = int(input("Guess the number between 1 and 50: "))
    difference = abs(secret - guess)
    if guess == secret:
        print(f"You got it! It was {secret}!")
        break
    elif abs(guess - secret) <= 5:
        print(f"You're {difference} away. Hot!")
    elif abs(guess - secret) >= 6:
        print(f"You're {difference} away. Cold!")
