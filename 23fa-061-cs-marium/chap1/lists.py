# Creating a list with different data types (list and tuple inside)
example = [1, ["another", "list"], ("a", "tuple")]
example     # Display the list


# Creating another list
mylist = ["element 1", 2, 3.14]
mylist     # Display the list


# Changing first element of list
mylist[0] = "yet element 1"
print(mylist[0])     # Print updated first element


# Changing last element using negative index
mylist[-1] = 3.15
print(mylist[-1])     # Print updated last element


# Creating a dictionary with different key-value pairs
mydict = {"Key 1": "value 1", 2: 3, "pi": 3.14}
print(mydict)     # Print dictionary


# Updating value of key "pi"
mydict["pi"] = 3.15
print(mydict["pi"])     # Print updated value


# Creating a tuple (immutable)
mytuple = (1, 2, 3)
print(mytuple)     # Print tuple


# Assigning built-in function to a variable
myfunc = len
print(myfunc(mylist))     # Use function to get length of list