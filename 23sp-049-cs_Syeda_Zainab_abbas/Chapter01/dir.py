# dir.py
# Basic control flow demo: an if/elif/else decision and a for-loop sum.

# --- Check whether a number is positive, zero, or negative ---
num = 1
# Try these too:  num = 0   /   num = -4.5
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# --- Sum all numbers in a list using a for-loop ---
numbers = [6, 6, 3, 8, -3, 2, 5, 44, 12]
sum = 0                       # accumulator starts at 0
for val in numbers:           # iterate over each element
    sum = sum + val           # add it to the running total
print("The sum is", sum)      # Output: The sum is 83
