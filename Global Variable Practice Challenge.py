


score = 0 #Global variables are definied outside the function and can be accessed (and changed if declared with global) inside a fuction.
          #Local variables are created inside a fucntion and only exist there - they disappear when fuction ends.
def win_round():
    global score
    score += 10
    print(f"\nYou won! Your score is now {score}!\n")

def lose_round():
    global score
    score -= 5
    print(f"\nYou lost! Your score is now {score}!\n")

win_round()
lose_round()
win_round()
lose_round()


