

cost_price = float(input("What is the cost price? "))
sell_price = float(input("What is the sell price? "))

while True:
    if cost_price < 0 or sell_price < 0:
        print("Invalid option.")
        break
    if sell_price - cost_price <= 0:
        print("No profit")
    else:
        print("Profit is made")
        break


