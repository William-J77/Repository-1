
while True:

    guess = int(input("Guess a number between 1 and 20: "))
    secret = 15
    difference = abs(guess - secret)
    print(f"You were {difference} away from the secret number.")
    if guess == secret:
        print("You guessed it!")
        break
    else:
        print("Try again!")