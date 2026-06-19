# Define a class named Myclass
class Myclass:
    common = 10     # Class variable shared by all objects

    def __init__ (self):
        self.myvariable = 3     # Instance variable for each object

    def myfunction (self, arg1, arg2):
        return self.myvariable     # Returns instance variable value


instance = Myclass()     # Create first object
print("instance.myfunction(1, 2)" , instance.myfunction(1, 2))     # Call method


instance2 = Myclass()     # Create second object
print("instance.common ",instance.common)     # Access class variable using first object
print("instance2.common ",instance2.common)   # Access class variable using second object


Myclass.common = 30     # Modify class variable using class name

print("instance.common ", instance.common)     # Updated value for first object
print("instance2.common ", instance2.common)   # Updated value for second object


instance.common = 10     # Override class variable for this instance only

print("instance.common ", instance.common)     # Instance now has its own value
print("instance2.common " , instance2.common)  # Second object still uses class value


Myclass.common = 50     # Change class variable again

print("instance.common ", instance.common)     # No effect on overridden instance
print("instance2.common " , instance2.common)  # Updated value for second object


# Define a child class that inherits from Myclass
class AnotherClass (Myclass):

    def __init__ (self, arg1):
        self.myvariable = 3     # Initialize instance variable
        print (arg1)     # Display passed argument


instance = AnotherClass ("hello")     # Create object of child class

print("instance.myfunction (1, 2) " , instance.myfunction (1, 2))     # Call inherited method


instance.test = 10     # Add a new attribute to object

print("instance.test " , instance.test)     # Print new attribute