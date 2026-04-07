# Import random module to generate random numbers

import random   

def do_something(count, out_list):
# Loop 'count' number of times
    for i in range(count):
# Append a random float (between 0.0 and 1.0) to the list
        out_list.append(random.random())