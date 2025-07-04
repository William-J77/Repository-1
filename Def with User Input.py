

def name_snumber():
    name = input("What is your name? ").strip().title()
    number = int(input("What is your favorite number? "))

    square_n = number **2

    print(f"Hello {name}. Your favorite number squared is {square_n}.")

name_snumber()