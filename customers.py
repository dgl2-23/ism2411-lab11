# Reflection 1:
# I would use .get() when a value might be missing because it prevents
# errors and lets me provide a default. I would use bracket notation
# when I know the key exists and need its value.

# Reflection 2:
# Exercise 8 reminds me of using SUMIF in Excel to add sales by region.
# Python can do this automatically with loops and dictionaries, making
# it easier to process large datasets without manually organizing them.
# Exercise 1
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)

# Exercise 2
customer["phone"] = "555-1234"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)

# Exercise 3
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("Email key does not exist.")


# Exercise 4
for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only gives us the dictionary keys.
for key in customer:
    print(key)


# Exercise 5
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

discount = tier_discounts.get(customer["tier"], 0)
price = 200
final_price = price * (1 - discount)

print("Tier:", customer["tier"])
print("Discount:", discount)
print("Final price:", final_price)


# Exercise 6
customers = [
    {"name": "Alice", "tier": "gold"},
    {"name": "Bob", "tier": "silver"},
    {"name": "Charlie", "tier": "platinum"}
]

for person in customers:
    discount = tier_discounts.get(person["tier"], 0)
    discount_amount = 300 * discount

    print(
        person["name"],
        person["tier"],
        "Discount amount: $",
        discount_amount
    )


# Exercise 7
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for item, details in catalog.items():
    print(item, details)

    if details["stock"] < 20:
        print("LOW STOCK")


# Exercise 8
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    summary[region] = summary.get(region, 0) + amount

for region in sorted(summary):
    print(region, summary[region])