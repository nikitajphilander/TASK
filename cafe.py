# cafe.py

# 1. Menu list
menu = ["coffee", "tea", "cake", "sandwich"]

# 2. Stock dictionary
stock = {
    "coffee": 50,
    "tea": 40,
    "cake": 20,
    "sandwich": 30
}

# 3. Price dictionary
price = {
    "coffee": 30,
    "tea": 25,
    "cake": 45,
    "sandwich": 60
}

# 4. Calculate total stock value
total_stock = 0

for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

# 5. Print result
print("Total stock worth:", total_stock)