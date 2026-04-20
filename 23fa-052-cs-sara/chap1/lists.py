# A list containing different data types:
# integer, another list, and a tuple
example = [1, ["another", "list"], ("a", "tuple")]

# Display the list
example


# Create a list with string, integer, and float
mylist = ["element 1", 2, 3.14]

# Display the list
mylist


# Modify the first element of the list (lists are mutable)
mylist[0] = "yet element 1"

# Print updated first element
print(mylist[0])


# Modify the last element using negative index (-1)
mylist[-1] = 3.15

# Print updated last element
print(mylist[-1])


# Create a dictionary with different types of keys and values
mydict = {"Key 1": "value 1", 2: 3, "pi": 3.14}

# Print the dictionary
print(mydict)


# Update the value of key "pi"
mydict["pi"] = 3.15

# Print updated value of "pi"
print(mydict["pi"])


# Create a tuple (tuples are immutable)
mytuple = (1, 2, 3)

# Print the tuple
print(mytuple)


# Assign built-in function 'len' to a variable
myfunc = len

# Call the function using the variable name
# This returns the length of mylist
print(myfunc(mylist))