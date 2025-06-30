import random

secret = random.randint(1, 10)
guess_count = 0

while True:
    guess = int(input("Can you guess the number between 1 and 10? "))
    guess_count += 1 # adds 1 each time there is a guess
    if guess == secret:
        print(f"It was {secret}! You got it! It took you {guess_count} tries!")
        break
    elif guess in (secret - 1, secret + 1): #this is a tuple containing two numbers. Could've used elif abs(guess - secret) == 1:
        #abs is absolute value of a number (removes any negative sign)
        print(f"You guessed {guess}. You're so close!")
    else:
        print(f"You guessed {guess}. Wrong! Try again!")
