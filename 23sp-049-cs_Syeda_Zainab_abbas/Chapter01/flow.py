# flow.py
# Demonstrates the three core control-flow tools: IF, FOR and WHILE.

# IF - choose a branch based on a condition
num = 1
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

# FOR - sum all numbers in a list
numbers = [6, 6, 3, 8, -3, 2, 5, 44, 12]
sum = 0
for val in numbers:
    sum = sum + val
print("The sum is", sum)

# WHILE - add natural numbers 1+2+3+...+n
n = 10
sum = 0
i = 1
while i <= n:                 # keep looping while the condition is true
    sum = sum + i
    i = i + 1                 # update the counter (avoids an infinite loop)
print("The sum is", sum)      # Output: The sum is 55
