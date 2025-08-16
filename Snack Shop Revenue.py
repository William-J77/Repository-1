

snacks = ["chips", "cookies", "popcorn", "pretzels", "candy"]
prices = [1.50, 2.00, 1.75, 1.25, 2.50]
sold_last_week = [20, 15, 10, 5, 8]


# #1 - total revenue for week

total_revenue = 0

for i in range(len(snacks)):
    total_revenue += prices[i] * sold_last_week[i]
print(total_revenue)


# #2 - Average price of a snack

all_prices = 0

for i in prices:
    all_prices += i
print(all_prices)

average_price = all_prices / (len(snacks))
print("The Average Price of a snack is: " + str(average_price))


# #3 - Create new list of "discounted prices" where each snack is $0.50 cheaper

discounted_prices = [price - 0.50 for price in prices]
print("The new discounted by 50 cents price list is: " + str(discounted_prices))


# #4 - Using a list comprehension, create a list called snacks_under_2 that contains 
# the names of snacks whose discounted price is less than $2.00.

snacks_under_2 = [snacks[i] for i in range(len(prices)) if discounted_prices[i] < 2.00]
print("The snacks under $2.00 are: " + str(snacks_under_2))