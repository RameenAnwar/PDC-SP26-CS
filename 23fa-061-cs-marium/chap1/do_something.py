import random     # Importing random module to generate random numbers

# Function to add random numbers into a list
def do_something(count, out_list):
    # Loop runs 'count' number of times
    for i in range(count):
        out_list.append(random.random())     # Add a random float value (0 to 1) into the list