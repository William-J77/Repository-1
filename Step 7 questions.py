#def add(a, b): #this is defiing (def) the fucntion (add) and saying it has two inputs (parameters) named a and b. 
    #return a + b #return means send this value back and stop executing the function and a + B does the math.

#result = add(2, 3) #Python sees you calling the function "add" with arguements 2 and 3 (seen as a and b). 
#print(result) #The variable "result" is assigned the value 5

#def greet(name):
    #print("Hello, " + name + "!")

#resulted = greet("Jimmy")
#print(resulted)


def build_profile(name, fav_color, fav_animal):
    profile = ""
    profile += "Hello " + name.title() + "!\n"
    profile += "Your favorite color is " + fav_color.lower() + "!\n"
    profile += "Your favorite animal is " +fav_animal.title() + "!\n"
    profile += "That's a great combo!\n"
    return profile

print(build_profile("alex", "blue", "turtles"))
