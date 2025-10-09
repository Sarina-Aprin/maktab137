Prices = {"Apple": 60, "Banana": 20, "Orange": 45, "Grapes": 80}

print(Prices.keys())
new_products = {}

for key, value in Prices.items():
    if value > 50:

        new_products[key] = value - value / 10

print(new_products)