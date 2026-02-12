# Ask for favourite restaurant
string_fav = input("What is your favourite restaurant? ")

# Ask for favourite number and cast to integer
int_fav = int(input("What is your favourite number? "))

# Print both values
print(string_fav)
print(int_fav)

# Try casting string_fav to integer
# This will cause an error if the restaurant name is not a number
# because Python cannot convert letters into an integer.
int(string_fav)

