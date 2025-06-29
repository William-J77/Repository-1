a = 5
b = 10
print(f"{a} + {b} = {a + b}")

name = "bob"
print(f"Name capitalized: {name.title()}")

name = "Jimbo"
print(f"His name is {name.title()}")

pi = 3.14159265
print(f"Pi rounded to 4 decimals: {pi:.4f}")

for i in range(1, 4):
    print(f"{i:<3} left | {i:^3} center | {i:>3} right")

print(" Num  |  Square  |  Cube")

for i in range(1, 6):
    square  = i ** 2 #to get the square of a number (to the power of)
    cube = i ** 3 #to get the number cubed (number times square)
    print(f"{i:>4}  |  {square:>7}  |  {cube:>5}")