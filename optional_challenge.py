# optional_challenge.py

# -------- Compilation Error 1 --------
print("Welcome to the challenge"   # Compilation Error (SyntaxError) - missing closing bracket


# -------- Compilation Error 2 --------
if True
    print("This will fail")  # Compilation Error (SyntaxError) - missing colon after if statement


# -------- Runtime Error --------
number = int("hello")  # Runtime Error (ValueError) - cannot convert text to integer


# -------- Logical Error --------
age = 18

if age > 18:
    print("You are an adult")
else:
    print("You are a minor")

# Logical Error:
# If age is 18, it prints "minor", which is incorrect.
# The condition should be >= 18.
