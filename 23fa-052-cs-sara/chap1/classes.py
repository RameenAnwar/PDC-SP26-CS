# Define a class
class Myclass:
    common = 10   # CLASS VARIABLE (shared by all objects)

    def __init__(self):
        # Constructor runs when object is created
        self.myvariable = 3   # INSTANCE VARIABLE (unique for each object)

    def myfunction(self, arg1, arg2):
        # Function returns instance variable
        return self.myvariable


# Create first object
instance = Myclass()

# Call function (arg1 and arg2 are not used)
print("instance.myfunction(1, 2)", instance.myfunction(1, 2))
# Output: 3


# Create second object
instance2 = Myclass()

# Access class variable from both objects
print("instance.common ", instance.common)    # 10
print("instance2.common ", instance2.common)  # 10


# Change class variable
Myclass.common = 30

# Affects all objects (shared variable)
print("instance.common ", instance.common)    # 30
print("instance2.common ", instance2.common)  # 30


# Create instance-specific variable (shadowing class variable)
instance.common = 10

print("instance.common ", instance.common)    # 10 (instance's own value)
print("instance2.common ", instance2.common)  # 30 (still class value)


# Change class variable again
Myclass.common = 50

# Only instance2 is affected
print("instance.common ", instance.common)    # 10 (unchanged)
print("instance2.common ", instance2.common)  # 50


# Inheritance: create child class
class AnotherClass(Myclass):

    def __init__(self, arg1):
        # Overriding constructor (parent __init__ not called)
        self.myvariable = 3
        print(arg1)


# Create object of child class
instance = AnotherClass("hello")
# Output: hello


# Use inherited method from parent class
print("instance.myfunction (1, 2) ", instance.myfunction(1, 2))
# Output: 3


# Add new attribute dynamically
instance.test = 10

print("instance.test ", instance.test)   # 10