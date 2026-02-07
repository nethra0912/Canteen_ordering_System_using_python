menu = {
    "tea": 10,
    "coffee": 15,
    "sandwich": 40,
    "burger": 60
}

total_bill = 0

print("College Canteen Ordering System")
print("Menu:")
for item in menu:
    print(item, "-", menu[item], "Rs")
print("--------------------------------")

while True:
    choice = input("Enter item name (or 'exit' to finish): ")

    if choice == "exit":
        break

    if choice not in menu:
        print("Item not available")
        print("--------------------------------")
        continue

    quantity = int(input("Enter quantity: "))
    cost = menu[choice] * quantity
    total_bill = total_bill + cost

    print("Added to cart:", choice)
    print("Item cost:", cost, "Rs")
    print("Current bill:", total_bill, "Rs")
    print("--------------------------------")

print("Final bill amount:", total_bill, "Rs")
print("Please pay at the counter.")
print("Thank you! Visit again.")
