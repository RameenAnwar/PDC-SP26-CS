1. What I Learned:

Basic Logic: I practiced using if-else statements to make decisions and for/while loops to repeat tasks, like adding numbers in a list.

Storing Data: I learned about different ways to store information:

Lists: Can change items.
Tuples: Items cannot be changed.
Dictionaries: Use keys to quickly find values.

Classes and Objects: I learned how to make blueprints (classes) for objects. Some variables are shared by all objects, and some are only for one object.

Inheritance: I can make a new class that “inherits” from an existing class so I don’t need to rewrite code.

Working with Files: I practiced opening text files, writing lines, and reading data back.

Speeding Up Code: I looked at three ways to run code:

Serial (one-by-one)
Threads (multitasking within the same program)
Multiprocessing (using multiple CPU cores at once)


2. How Code Runs:

Serial: The computer does one job at a time. It’s simple but slow for big tasks.

Multithreading: The program tries to do many things at once in the same program. Useful when the program is waiting for something, like downloading files.

Multiprocessing: The computer splits work across multiple CPU cores at the same time. This is best for huge amounts of data because calculations happen simultaneously.

3. When to Use:

Simple Tasks: Use normal loops and classes.
Tasks That Wait (like downloads): Use threading.
Big Calculations/Big Data: Use multiprocessing to save time.



4. Pros and Cons:

*Serial (Normal Code):

Pros: Easy to write and debug, uses little memory.
Cons: Slow for large tasks.

*Multithreading:

Pros: Program stays responsive, uses little extra memory.
Cons: Python’s GIL stops threads from doing heavy calculations at the same time, so it’s not always faster.

*Multiprocessing:

Pros: Fastest for heavy tasks, uses all CPU power.
Cons: Uses more memory because it runs multiple copies of the program.
