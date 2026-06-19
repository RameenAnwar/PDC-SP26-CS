class Myclass:
      #  we are creating a Class variable that is Shared by all objects  unless changed separately.
    common = 10
    def __init__ (self):
          # myvariable is an instance variable now Every object  will have  its own copy
        self.myvariable = 3
         # This function/method() is used for returning the myvariable
    def myfunction (self, arg1, arg2):
        return self.myvariable
# creating first object of the class
instance = Myclass()
# Call myfunction using the first object
print("instance.myfunction(1, 2)" , instance.myfunction(1, 2))
# creating second object of the class
instance2 = Myclass()
# Printing class variable using first object
print("instance.common ",instance.common)
# Printing class variable using second object
print("instance2.common ",instance2.common)
# now changing class variable using class name ,doing this will affect all objects created and are still using the class variable.
Myclass.common = 30
#now printing class updated variable using first object
print("instance.common ", instance.common)
# now printing  class updated variable using second object
print("instance2.common ", instance2.common)

# now Assigning a value to 'common' using the first object
# Now this object has its own value (overrides) and will not follow class value

instance.common = 10
# now printing variable using first object
print("instance.common ", instance.common)


# now printing variable using second object....it is still using class value
print("instance2.common " , instance2.common)
# Changing class variable again using class name
Myclass.common = 50
# object 1  will still show its own value
print("instance.common ", instance.common)
# object 2  will show updated class value
print("instance2.common " , instance2.common)

# Creating a class that inherits from Myclass
class AnotherClass (Myclass):
     # Constructor
    def __init__ (self, arg1):
          # Creating instance variable
        self.myvariable = 3
        # Printing the value passed while making the object
        print (arg1)
# Creating object of child class
instance = AnotherClass ("hello")
# Calling inherited function from parent class
print("instance.myfunction (1, 2) " , instance.myfunction (1, 2))
# Creating a new variable named test for this object
instance.test = 10
# Printing the new variable
print("instance.test " , instance.test)






#This code defines a class Myclass with a class variable common shared by all objects and an instance variable myvariable unique to each object,
# along with a method myfunction() that returns myvariable.
# It shows how changing the class variable affects all objects unless an object creates its own instance-level attribute with the same name,
#  overriding the class variable. The code also defines a child class AnotherClass that inherits from Myclass, 
# demonstrates calling the inherited method, and shows that new attributes like test can be added dynamically to objects at runtime, 
# illustrating class vs instance variables, inheritance, and dynamic attributes in Python.


# output 
#instance.myfunction(1, 2) 3
#instance.common  10
#instance2.common  10
#instance.common  30
# instance2.common  30
# instance.common  10
# instance2.common  30
# instance.common  10
# instance2.common  50
# hello
# instance.myfunction (1, 2)  3
# instance.test  10