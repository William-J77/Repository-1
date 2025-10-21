from datetime import datetime

birthday = datetime(1994, 2, 15, 4, 25, 12) #(year, month, day, hour, minute, second)

print()
print(birthday.weekday())
print(birthday.month)
print(birthday.minute)

# datetime.now

print(datetime.now())

print(datetime(2018, 1, 1,) - datetime(2017, 1, 1)) #can't add/multiply/divide dates.. only subtract

#srtptime (the p stands for parse) - takes a string, parses through it, and converts it to a datetime

parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y') # google 'python datetime' to get the strftime and strptime directives

print(parsed_date.month) # or day or year

#strftime takes a datetime and creates a string from it

date_string = datetime.strftime(datetime.now(), '%b %d, %Y') #takes two arguements - first the datetime, second describing what you want it to look like

print(date_string)

