
message = ""

genre = input("Please enter a movie genre.\n").strip().lower()
message += (f"I do prefer films of the {genre} genre.\n")

title = input("Please enter a film title of that genre.\n").strip().title()
message += (f"{title} is a great example of a {genre} film.\n")

snack = input("Please enter your movie snack.\n").strip().lower()
message += (f"{snack} would go great with {title}.\n")

place = input("Please enter a location to watch this film.\n").strip().lower()
message += (f"{place} would be an excellent place to watch {title}.\n")

print(message)