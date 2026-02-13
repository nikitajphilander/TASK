# float_manipulation.py

import statistics

numbers = []

# Ask user for 10 floats
for i in range(10):
    num = float(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Total
total = sum(numbers)
print("Total:", total)

# Index of maximum
max_value = max(numbers)
max_index = numbers.index(max_value)
print("Index of maximum:", max_index)

# Index of minimum
min_value = min(numbers)
min_index = numbers.index(min_value)
print("Index of minimum:", min_index)

# Average (mean), rounded to 2 decimals
mean_value = statistics.mean(numbers)
print("Average:", round(mean_value, 2))

# Median
median_value = statistics.median(numbers)
print("Median:", median_value)
