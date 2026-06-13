2) Class.py

class Myclass: # Define a class
    common = 10   # Class variable (shared by all instances)

    def __init__(self):   # Constructor
        self.myvariable = 3   # Instance variable (unique per object)

    def myfunction(self, arg1, arg2):
        return self.myvariable   # Returns instance variable

instance = Myclass() # Create object
print("instance.myfunction(1, 2)", instance.myfunction(1, 2))
instance2 = Myclass()
print("instance.common", instance.common)# Access class variable
print("instance2.common", instance2.common)

Myclass.common = 30 # Modify class variable
print("instance.common", instance.common)
print("instance2.common", instance2.common)

instance.common = 10 # Override class variable in one object
print("instance.common", instance.common)
print("instance2.common", instance2.common)

Myclass.common = 50 # Change class variable again
print("instance.common", instance.common)
print("instance2.common", instance2.common)

# Inheritance
class AnotherClass(Myclass):

    def __init__(self, arg1):
        self.myvariable = 3
        print(arg1)

instance = AnotherClass("hello")
print("instance.myfunction(1, 2)", instance.myfunction(1, 2))

instance.test = 10   # Dynamically adding variable
print("instance.test", instance.test)


Topic Learned:
   Classes
   Instance vs Class variables
   Inheritance
   Object creation

Execution:
   Class defined
   Objects created
   Class variable shared
   Instance variable separate
   Inheritance used

End Use:
   OOP programming (real-world modeling)

When & How to Use:
   Use classes when building structured programs like:
   Student systems
   Bank systems
   Apps

Advantages
   Code reusable
   Organized
   Supports inheritance

Disadvantages
   More complex than simple scripts


2) dir.py

# Check if number is positive, negative or zero
num = 1

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")


# Sum of list elements
numbers = [6, 6, 3, 8, -3, 2, 5, 44, 12]

sum = 0
for val in numbers:
    sum = sum + val

print("The sum is", sum)


Topic Learned:
   if-elif-else
   for loop
   List iteration

Execution:
   Condition check → loop runs → sum calculated

End Use:
   Basic decision making and looping

When to Use:
   Data validation
   Calculations

Advantages:
   Simple logic
   Easy to understand

Disadvantages:
   Manual sum (can use built-in sum())


3) do_something.py

import random

# Function that appends random numbers to a list
def do_something(count, out_list):
    for i in range(count):
        out_list.append(random.random())


Topic Learned:
   Function definition
   Parameters
   List modification

Execution:
   Loop runs → random numbers added to list

End Use:
   Used for performance testing (threading/process comparison)

When to Use:
   Data generation
   Performance benchmarking

Advantages:
   Reusable function

Disadvantages:
   Large memory usage


4) file.py

# Open file in write mode
f = open('test.txt', 'w')
f.write('first line of file \n')
f.write('second line of file \n')
f.close()

# Open file in read mode
f = open('test.txt')
content = f.read()
print(content)
f.close()



Topic Learned:
   File handling (read/write)

Execution:
   File created → written → reopened → read

End Use:
   Save data permanently

When to Use:
   Logs
   Reports
   Data storage

Advantages:
   Persistent storage

Disadvantages:
   Must close file manually
   Risk of data loss if not handled properly


5) flow.py
Topic Learned:
   IF
   FOR
   WHILE

Execution:
   IF checks condition
   FOR iterates list
   WHILE repeats until condition false

End Use:
   Program flow control

When to Use:
   Every program uses control flow

Advantages:
   Full control over execution

Disadvantages:
   Infinite loop risk in while


6)list.py
Topic Learned:
   List
   Dictionary
   Tuple
   Built-in function

Execution:
   Modify list values
   Modify dictionary
   Print tuple
   Use len() function

End Use:
   Data storage structures

When to Use:
   Lists → dynamic data
   Tuple → fixed data
   Dict → key-value storage

Advantages:
   Flexible
   Powerful data structures

Disadvantages:
   Mutable types can cause bugs


7) serial_test.py
Topic Learned:
   Serial execution

Execution:
   Function runs 10 times one by one

End Use:
   Baseline performance measurement

When to Use:
   When order matters

Advantages:
   Simple
   No synchronization issues

Disadvantages:
   Slow for large tasks

8) multithreading_test.py
Topic Learned:
   Multithreading

Execution:
   10 threads created
   Run same function

End Use:
   Parallel task execution

When to Use:
   I/O bound tasks

Advantages:
   Faster for I/O tasks

Disadvantages:
   GIL limits CPU tasks in Python

9) multiporcessing_test.py
Topic Learned:
   Multiprocessing

Execution:
   10 processes created
   Run function in parallel

End Use:
   CPU intensive tasks

When to Use:
   Heavy computation

Advantages:
   True parallelism
   Uses multiple CPU cores

Disadvantages:
   High memory usage
   Slower startup


10) thread_and_processes.py
Topic Learned:
   Serial vs Thread vs Process comparison

Execution:
  Runs:
   Serial (commented)
   Threading
   Multiprocessing
   Measures time

End Use:
   Performance comparison

When to Use:
   To choose best execution model

Advantages:
   Shows performance difference

Disadvantages:
   Shared list unsafe in threading
