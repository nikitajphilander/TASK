# Get user input for each event
swimming = int(input("Enter swimming time (in minutes): "))
cycling = int(input("Enter cycling time (in minutes): "))
running = int(input("Enter running time (in minutes): "))

# Calculate total time
total_time = swimming + cycling + running

# Print total time
print("Total time taken for the triathlon:", total_time, "minutes")

# Determine award
if total_time <= 100:
    print("Award: Provincial Colours")
elif total_time <= 105:
    print("Award: Provincial Half Colours")
elif total_time <= 110:
    print("Award: Provincial Scroll")
else:
    print("Award: No award")

