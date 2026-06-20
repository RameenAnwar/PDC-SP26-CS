# lists.py
# Quick tour of Python's built-in containers: list, tuple, dict, and treating
# a function as a value (functions are first-class objects in Python).

example = [1, ["another", "list"], ("a", "tuple")]  # lists can hold mixed/nested types
mylist = ["element 1", 2, 3.14]
mylist[0] = "yet element 1"        # lists are MUTABLE - items can be reassigned
print(mylist[0])
mylist[-1] = 3.15                  # negative index counts from the end
print(mylist[-1])

mydict = {"Key 1": "value 1", 2: 3, "pi": 3.14}  # dictionary = key/value pairs
print(mydict)
mydict["pi"] = 3.15                # update a value by its key
print(mydict["pi"])

mytuple = (1, 2, 3)                # tuples are IMMUTABLE (cannot be changed)
print(mytuple)

myfunc = len                       # assign the built-in len function to a variable
print(myfunc(mylist))              # call it through that variable
