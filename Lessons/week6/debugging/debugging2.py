items = ["Apples", "Bananas", "Bread"]
prices = [1.20, 0.8, 2.50]

total = 0
for i in range(0, 2):
    total = total + prices[i]
print("Total cost is: £", total)
if total == 4.50:
    print("Budget met!")
else:
    print("Over budget")