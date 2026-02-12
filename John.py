# John.py

incorrect_names = []

name = input("Enter your name: ")

while name.lower() != "john":
    incorrect_names.append(name)
    name = input("Enter your name: ")

print("Incorrect names:", incorrect_names)
