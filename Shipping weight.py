

weight = 4

# Ground Shipping

print("\nGround Shipping will cost: ")
if weight <= 2:
    ground_cost = weight * 1.50 + 20
elif weight > 2 and weight <= 6:
    ground_cost = weight * 3.00 + 20
elif weight > 6 and weight <= 10:
    ground_cost = weight * 4.00 + 20
else:
    ground_cost = weight * 4.75 + 20

print(ground_cost)

# Premium Shipping

premium_shipping = 125.00

print("\nPremium Ground Shipping will cost: ")
print(premium_shipping)

# Drone Shipping

print("\nDrone Shipping will cost: ")
if weight <= 2:
    drone_cost = weight * 4.50
elif weight > 2 and weight <= 6:
    drone_cost = weight * 9.00
elif weight > 6 and weight <= 10:
    drone_cost = weight * 12.00
else:
    drone_cost = weight * 14.25

print(drone_cost)

if ground_cost < drone_cost and ground_cost < premium_shipping:
    print("\nGround Shipping is the cheapest option.")
elif drone_cost < ground_cost and drone_cost < premium_shipping:
    print("\nDrone Shipping is the cheapest option")
else:
    print("\nPremium Shipping is the cheapest option.")


# Cheapest method for shipping a 4.8 pound package would be Ground Shipping at $34.40
# Cheapest method for shipping a 41.5 pound package would be Premium Shipping at $125.00