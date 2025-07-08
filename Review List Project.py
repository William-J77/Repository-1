import random


def custommessage(why, wordvalue):
    message = ""
    message += f"{why} is why you've chosen this word.\n"
    message += f"You have stated, the value of this word to you is {wordvalue}.\n"

    return message 

while True:
    word = input("Choose the mystery word: ").strip().lower()

    if len(word) < 4:
        print(f"{word} is too short. Please select another word.")
        continue
    if len(word) > 7:
        print(f"{word} is too long. Please select another word.")
        continue
    else:
        theme = [
            "You have chosen... wisely.",
            "You have chosen well.",
            "You have picked the right length of word.",
            "Hot damn! Great choice.",
        ]
        print(random.choice(theme))

    length = len(word)
    if length in range(4, 8):
        print("Once again, you have chosen a word length this program likes - I hope you are aware of this.")
    
    why = input("Why have you chosen this word?\n")
    wordvalue = input("What is the value of this word to you?(no numbers please)\n")

    print(custommessage(why, wordvalue))
       
    calcsquared = len(word) **2
    print(f"I'm not sure why you would want to know this, but your word length squared is {calcsquared}.")
    break


     
