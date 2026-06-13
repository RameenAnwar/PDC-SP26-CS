# Import random module to generate random numbers
import random
# Define a function that appends random numbers to a list
def do_something(count,out_list):
  # Loop 'count' times
	for i in range(count):
		# Generate a random float between 0 and 1 and append to the list
		out_list.append(random.random())

# now for usage we will have to do like this bellow 
example_list = []              # create empty list
do_something(5, example_list )  # add 5 random numbers to it
print(example_list )             # show the numbers

#example output generated 
# [0.7908304779243964, 0.8210971489448966, 0.9527232180509574, 0.43748679389681844, 0.428594183163032]