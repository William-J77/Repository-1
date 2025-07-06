

message = ""

color = input("Please select a color.\n").strip().lower()
message += (f"The mysterious message was written in {color} ink.\n")

animal = input("Please select an animal.\n").strip().lower()
message += (f"The {animal} had a {color} mustache.\n")

location = input("Please select a location.\n").strip().lower()
message += (f"The {animal} was found at {location}.\n")

object = input("Please select a strange object.\n").strip().lower()
message += (f"The {object} was in the mouth of the {animal} at {location}.\n")

print(message)