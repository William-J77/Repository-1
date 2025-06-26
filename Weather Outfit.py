def outfit_recommendation(temperature, condition):
    message = ""
    message += "Let's get you dressed!\n"
    message += "The temperature is " + str(temperature) + " degrees.\n"
    message += "It looks " + condition.strip().lower() + " outside.\n"
    

    if temperature < 40:
        message += "Wear a coat!\n"
    elif temperature <= 65:
        message += "Bring a sweater.\n"
    elif temperature > 65:
        message += "T-shirt weather!\n"

    if condition == "rainy":
        message += "Don't forget an umbrella!\n"
    elif condition == "sunny":
        message += "Sunglasses might help.\n"
    return message

result = outfit_recommendation(40, "rainy")
print(result)
result2 = outfit_recommendation(64, "sunny")
print(result2)
result3 = outfit_recommendation(66, "rainy")
print(result3)
