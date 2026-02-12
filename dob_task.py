# dob_task.py

with open("DOB.txt", "r") as file:
    lines = file.readlines()

names = []
birthdays = []

for line in lines:
    parts = line.strip().split()

    # First two words are the name
    name = parts[0] + " " + parts[1]

    # The rest is the birthday
    birthday = " ".join(parts[2:])

    names.append(name)
    birthdays.append(birthday)

print("Name")
for name in names:
    print(name)

print("\nBirthday")
for birthday in birthdays:
    print(birthday)
