



while True:
    word = input("Enter a word: ").strip().lower()

    if len(word) < 4:
        print("Your word is too short. Please try again.")
        continue
    if len(word) > 7:
        print("Your word is too long. Please try again.")
        continue
    else:
        print("Thank you for choosing a word that is the correct length.")
        break
