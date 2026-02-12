total = 0
count = 0

while True:
    num = int(input("Enter a number (-1 to stop): "))

    if num == -1:
        break

    if num == 0:
        print("0 is not valid.")
        continue

    total = total + num
    count = count + 1

if count > 0:
    average = total / count
    print("The average is:", average)
else:
    print("No valid numbers were entered.")