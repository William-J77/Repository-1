#Import section - notice custom_module is bring imported from another .py file
import datetime as dt 
from decimal import Decimal
from random import randint, choice
import custom_module

#This is calling the current date and time at the moment it's called
today = dt.datetime.now()

print("The current date and time is " + str(today) + ".")

#This is the base cost that is added to the cost below. Notice the use of Decimal for making sure the price is to two decimal places
base_cost = Decimal("29.99")
random_year = randint(1, 2024)

#List of possible destinations to randomly choose from
possible_destinations = ["Oregon", "Alabama", "New York", "Maine", "Florida", "England", "Italy", "Japan", "South Korea", "Ontario"]

#This uses the choice() function to randomly choose a destination from the list
destination = choice(possible_destinations)

print(destination)

#This is the cost function to figure out the cost added to the base cost and format it
def cost(current_year, target_year):
  total = Decimal(base_cost) + (current_year - target_year)
  formatted_cost = "{:.2f}".format(total)
  return formatted_cost


print(cost(today.year, random_year))

#THis is the variable needed to use the function, notice the use ot today.year... That was bloody confusing
total_cost = cost(today.year, random_year)

#This is the calling of the function from the other file - make sure those arguements are in order!
print(custom_module.generate_time_travel_message(random_year, destination, total_cost))
