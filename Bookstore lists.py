


books = ["1984", "The Hobbit", "Dune", "Pride and Prejudice", "Hamlet"]
prices = [8.99, 10.50, 12.75, 7.25, 9.60]
sold_last_week = [12, 8, 15, 5, 10]


# Total sales per book

total_sales = [prices[i] * sold_last_week[i] for i in range(len(books))]
print("\nTotal sales per book: " + str(total_sales))

# Total revenue overall

total_revenue = 0
for sale in total_sales:
    total_revenue = total_revenue + sale 
print("\nThe total revenue overall is: " + str(total_revenue))

# Average book price

total_of_prices = 0
for price in prices:
    total_of_prices = total_of_prices + price
print("\nThe total price of all five books is: " + str(total_of_prices))

average_price = total_of_prices / (len(books))
print("The average price per book is: " + str(average_price))

# Apply discount of 20% off each book

discount_20_percent = [prices[i] * 0.8 for i in range(len(books))]
print("\nA 20 percent discount applied to each book: " + str(discount_20_percent))
