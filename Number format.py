#price = 4.56789
#discount = 0.2345
#tax_rate = 0.08765

#print(f"\nPrice: $ {price:.2f}")
#print(f"\nDiscount: {discount:.2f}")
#print(f"\nTax Rate: {tax_rate:.2f}")

weekly_pay_before_tax = 20.50
tax_amount = 12.5
hours = 40

print(f"\nBefore Tax Pay: $ {weekly_pay_before_tax * hours:.2f}")
print(f"\nTo the Tax Man: $ {weekly_pay_before_tax * hours * (tax_amount / 100):.2f}")
print(f"\nYour take home pay: $ {weekly_pay_before_tax * hours * (1 - tax_amount / 100):.2f}")