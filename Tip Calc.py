# Tip calculator

bill = float(input("Enter your bill total: $")) #float says it's going to be a decimal input
tip_percent = float(input("Enter tip percentage (like 15 for 15%): "))

tip_amount = bill * (tip_percent / 100) #the * symbol means multiplication
total = bill + tip_amount

print(f"\nBill: ${bill:.2f}")
print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
print(f"Total: ${total:.2f}")