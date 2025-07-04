

def outfit_rec(weather, temp, clothes, event):
    print(f"If it's {weather} and {temp}, wear {clothes} to the {event}.")

weather = input("What is the weather like today? ").strip().lower()
temp = int(input("What is the temperature outside? "))

if temp <= 55:
    clothes = ("a coat")
elif temp in range(56, 70):
    clothes = ("long sleeves and pants")
else:
    clothes = ("shorts and a t-shirt")

event = input("What event are you attending today? ").strip()

outfit_rec(weather, temp, clothes, event)