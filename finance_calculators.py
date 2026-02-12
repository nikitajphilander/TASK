import math

print("Investment - to calculate the amount of interest you'll earn on your investment.")
print("Bond       - to calculate the amount you'll have to pay on a home loan.")

choice = input("\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if choice == "investment":

    P = float(input("Enter the amount of money you are depositing: "))
    rate = float(input("Enter the interest rate (e.g. 8 for 8%): "))
    t = float(input("Enter the number of years you plan on investing: "))

    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

    r = rate / 100

    if interest_type == "simple":
        A = P * (1 + r * t)
    elif interest_type == "compound":
        A = P * math.pow((1 + r), t)
    else:
        print("Invalid interest type selected.")
        exit()

    print(f"\nThe total amount after {t} years will be: {A:.2f}")

elif choice == "bond":

    P = float(input("Enter the present value of the house: "))
    annual_rate = float(input("Enter the interest rate (e.g. 7 for 7%): "))
    months = int(input("Enter the number of months you plan to repay the bond: "))

    i = (annual_rate / 100) / 12

    repayment = (i * P) / (1 - (1 + i) ** (-months))

    print(f"\nYour monthly repayment will be: {repayment:.2f}")

else:
    print("Invalid selection. Please enter either 'investment' or 'bond'.")

