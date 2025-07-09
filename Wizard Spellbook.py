

print("\n Give us the three magic words, traveller... ")
word1 = input("\nWord 1: ").strip().lower()
word2 = input("Word 2: ").strip().lower()
word3 = input("Word 3: ").strip().lower()

repeats = int(input("\n How many times should the words be chanted? "))

magic_words = [word1, word2, word3]

for _ in range(repeats):
    for word in magic_words:
        print(f"{word} {_ + 1} times!")