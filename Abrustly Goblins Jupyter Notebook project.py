

gamers = []

def add_gamer(gamer, gamers_list):
    if "name" in gamer and "availability" in gamer:
        gamers_list.append(gamer)


add_gamer({'name':'Kimberly Warner', 'availability': ["Monday", "Tuesday", "Friday"]}, gamers)
add_gamer({'name':'Thomas Nelson','availability': ["Tuesday", "Thursday", "Saturday"]}, gamers)
add_gamer({'name':'Joyce Sellers','availability': ["Monday", "Wednesday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'Michelle Reyes','availability': ["Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Stephen Adams','availability': ["Thursday", "Saturday"]}, gamers)
add_gamer({'name': 'Joanne Lynn', 'availability': ["Monday", "Thursday"]}, gamers)
add_gamer({'name':'Latasha Bryan','availability': ["Monday", "Sunday"]}, gamers)
add_gamer({'name':'Crystal Brewer','availability': ["Thursday", "Friday", "Saturday"]}, gamers)
add_gamer({'name':'James Barnes Jr.','availability': ["Tuesday", "Wednesday", "Thursday", "Sunday"]}, gamers)
add_gamer({'name':'Michel Trujillo','availability': ["Monday", "Tuesday", "Wednesday"]}, gamers)

print()
print(gamers)

def build_daily_frequency_table():
    return {
        "Sunday": 0, 
        "Monday": 0, 
        "Tuesday": 0, 
        "Wednesday": 0, 
        "Thursday": 0, 
        "Friday": 0, 
        "Saturday": 0
    }

count_availability = build_daily_frequency_table()

def calculate_availability(gamers_list, available_frequency):
    for gamer in gamers_list: 
        for day in gamer['availability']: #day beig a stand in variable for all the days in the availablity dictionary of each gamer
            available_frequency[day] += 1 #adding a count of 1 to each day on the available_frequency list

calculate_availability(gamers, count_availability)
print()
print(count_availability)

def find_best_night(availability_table):
    best_day = max(availability_table, key = availability_table.get)
    return best_day

game_night = find_best_night(count_availability)
print()
print(game_night)

def available_on_night(gamers_list, day):
    return [gamer["name"] for gamer in gamers_list if day in gamer["availability"]] 
	# 1.	for gamer in gamers_list
	# •	Loops through each dictionary (gamer) in the gamers_list.
	# 2.	if day in gamer["availability"]
	# •	Checks if the day we’re interested in is in this gamer’s "availability" list.
	# •	Only includes gamers where this is True.
	# 3.	gamer["name"]
	# •	This is the value we put in the new list for each gamer that passed the if check.

attending_game_night = available_on_night(gamers, game_night)
print()
print(attending_game_night)



def send_email(gamers_who_can_attend, day, game):
    form_email = '\nHello {name}, \n{day_of_week} we are hosting a night of {game}. Come join us!\n'
    for gamer in gamers_who_can_attend:
        print(form_email.format(name=gamer, day_of_week=day, game=game))

send_email(attending_game_night, game_night, "Abruptly Goblins!")