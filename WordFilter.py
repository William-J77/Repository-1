


word1 = input("Enter a word: ")
print(f"{word1} has {len(word1)} letters.")

if len(word1) == 4:
    print("That's a four letter word")
elif len(word1) == 5:
    print("That's a five letter word")
elif len(word1) == 6:
    print("That's a six letter word")
elif len(word1) == 7:
    print("That's a seven letter word")
elif len(word1) < 4:
    print("Your word is too short.")
else:
    print("Your word is too long or short and has broken the program.")