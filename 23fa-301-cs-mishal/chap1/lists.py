# A list can contain numbers, strings, another list, or even a tuple
example = [1, ["another", "list"], ("a", "tuple")]
#  shows the list
example
# Create a list with different types of elements
mylist = ["element 1", 2, 3.14]
#  shows the list
mylist
# Changing the 0th position element of the list
mylist[0] = "yet element 1"
# printing the updated list element
print(mylist[0])
# Change the last element of the list using negative indexing
mylist[-1] = 3.15
  # Printing the updated last element
print (mylist[-1])
# Creating a dictionary with mixed key types
mydict = {"Key 1": "value 1", 2: 3, "pi": 3.14}
# Printing the whole dictionary
print(mydict)
# Updating the value for the key "pi" and prinitng it 
mydict["pi"] = 3.15
print(mydict["pi"])
# Create a tuple (immutable sequence) and prining it
mytuple = (1, 2, 3)
print(mytuple)
# Assign a function to a variable
myfunc = len
# Call the function using the variable (returns length of mylist) and print it
print (myfunc(mylist))

# This code demonstrates Python’s lists, dictionaries, tuples, and functions.
# It creates lists containing numbers, strings, nested lists, and tuples, 
# then shows how to update elements using indexing, including negative indexing.
# It also creates a dictionary with mixed key types and updates a value using its key.
#  A tuple is defined to show an immutable sequence, and finally, a function (len) is assigned to a variable and called to get the length of a list. 
#  The code illustrates mutable vs immutable types, dynamic updates, and function assignment.


# expectedc output
# yet element 1
# 3.15
# {'Key 1': 'value 1', 2: 3, 'pi': 3.14}
# 3.15
# (1, 2, 3)
# 3
