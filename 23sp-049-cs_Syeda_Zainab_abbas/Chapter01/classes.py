# classes.py
# Python OOP basics: shows the difference between CLASS variables (shared by all
# instances) and INSTANCE variables (unique to each object), plus inheritance.

class Myclass:
    common = 10                       # CLASS variable - shared across all instances
    def __init__(self):
        self.myvariable = 3           # INSTANCE variable - unique per object
    def myfunction(self, arg1, arg2):
        return self.myvariable        # returns this instance's variable

instance = Myclass()                  # create first object
print("instance.myfunction(1, 2)", instance.myfunction(1, 2))

instance2 = Myclass()                 # create second object
print("instance.common ", instance.common)    # both read the same class variable
print("instance2.common ", instance2.common)

Myclass.common = 30                   # changing the CLASS variable affects ALL instances
print("instance.common ", instance.common)
print("instance2.common ", instance2.common)

instance.common = 10                  # this creates an INSTANCE variable that shadows the class one (only for `instance`)
print("instance.common ", instance.common)
print("instance2.common ", instance2.common)
Myclass.common = 50                   # instance2 still follows the class variable; instance keeps its own
print("instance.common ", instance.common)
print("instance2.common ", instance2.common)

class AnotherClass(Myclass):          # inherits from Myclass
    # "self" is passed automatically and refers to the instance.
    def __init__(self, arg1):
        self.myvariable = 3
        print(arg1)

instance = AnotherClass("hello")      # constructor prints "hello"
print("instance.myfunction (1, 2) ", instance.myfunction(1, 2))  # inherited method

instance.test = 10                    # you can add new attributes to an object on the fly
print("instance.test ", instance.test)
