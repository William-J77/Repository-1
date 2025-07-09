

word = input("What is the magic chant word? ").strip().lower()

repeats = int(input("How many times should the magic chant be repeated? "))

for _ in range(repeats):
    print(f"{word} allakazam! {_ + 1} times!")
