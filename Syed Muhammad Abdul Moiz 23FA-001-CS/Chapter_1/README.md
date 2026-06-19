# Chapter 1

### Table of Contents
* [1. classes](#1-classes)
* [2. dir](#2-dir)
* [3. do_something](#3-do_something)
* [4. file](#4-file)
* [5. flow](#5-flow)
* [6. lists](#6-lists)
* [7. multiprocessing_test](#7-multiprocessing_test)
* [8. multithreading_test](#8-multithreading_test)
* [9. serial_test](#9-serial_test)
* [10. thread_and_processes](#10-thread_and_processes)

---

### 1. classes
* **What I Learned:** I learned how to create "blueprints" (classes) for my code and how Object-Oriented Programming (OOP) works. I also learned about inheritance and the difference between shared variables and individual variables.
* **How it Executes:** The code creates a parent class with some variables. When we make objects from this class, changing a shared class variable updates all objects, but changing an individual object's variable only affects that one object. Later, a child class is made that inherits the features of the parent class.
* **End Use:** It is used to manage real-world data in a structured way, like managing user accounts, game characters, or bank details.
* **Short Summary:** This script covers the basics of classes, objects, and inheritance in Python.
* **Pros & Cons:** - **Advantages:** Makes code very clean and easy to reuse.
  - **Disadvantages:** It can be confusing for beginners and is not needed for very simple scripts.

### 2. dir
* **What I Learned:** I learned how to make decisions in code using if-else and how to repeat actions using a for loop.
* **How it Executes:** First, the program checks if a specific number is positive, negative, or zero using conditions. Second, it loops through a list of numbers, adding each one to a total sum, and prints the final result.
* **End Use:** Used anytime we need to filter data or calculate totals from a list of items.
* **Short Summary:** A simple script showing basic conditional logic and how to loop through data.
* **Pros & Cons:** - **Advantages:** Very simple to write and easy to understand.
  - **Disadvantages:** A basic loop can be slow if you are working with millions of numbers.

### 3. do_something
* **What I Learned:** I learned how to write custom functions and how to use Python's random module.
* **How it Executes:** A custom function is created that takes a number (count) and an empty list. It runs a loop 'count' times, generates a random decimal number each time, and adds it to the list.
* **End Use:** Generating random data for testing, simulations, or game development.
* **Short Summary:** Using a custom function to quickly fill a list with random numbers.
* **Pros & Cons:** - **Advantages:** You write the code once and can use it as many times as you want.
  - **Disadvantages:** The basic random module is not secure enough for passwords or cryptography.

### 4. file
* **What I Learned:** I learned how to save data to the hard drive so it doesn't get lost when the program closes.
* **How it Executes:** The code opens a text file in 'write' mode, adds a few lines of text, and safely closes it. Then, it opens the same file in 'read' mode, brings the text back into the program, and prints it.
* **End Use:** Saving user settings, creating activity logs, or backing up data.
* **Short Summary:** Shows the complete process of creating, writing to, and reading from a text file.
* **Pros & Cons:** - **Advantages:** Data is saved permanently.
  - **Disadvantages:** If you forget to close a file, it can cause memory issues. Also, 'write' mode can accidentally delete old data if you aren't careful.

### 5. flow
* **What I Learned:** I learned the difference between for loops and while loops, and how to control what the program does next.
* **How it Executes:** The script uses an if statement to check a condition. Then, it uses a for loop to go through a predefined list. Finally, it uses a while loop that keeps running and adding numbers until a specific counter is reached.
* **End Use:** Use a for loop when you know exactly how many items you have. Use a while loop when you are waiting for a specific event to happen.
* **Short Summary:** Controlling the direction of a program using different conditions and loops.
* **Pros & Cons:** - **Advantages:** Easily automates repetitive tasks.
  - **Disadvantages:** A while loop can run forever and freeze the program if you forget to update the counter inside it.

### 6. lists
* **What I Learned:** I learned how to store multiple items using Python's main data containers: Lists, Tuples, and Dictionaries.
* **How it Executes:** The code creates different containers. It updates a list using its position (index), stores data in a dictionary using key-value pairs, and creates a tuple to show that its data cannot be changed once created.
* **End Use:** Dictionaries are used for labeled data (like an address book), lists for ordered items, and tuples for fixed data that shouldn't change.
* **Short Summary:** A simple comparison of how to store and access data using different Python structures.
* **Pros & Cons:** - **Advantages:** Keeps large amounts of related data organized in one place.
  - **Disadvantages:** Providing the wrong index or key will cause the program to crash.

### 7. multiprocessing_test
* **What I Learned:** I learned how to bypass Python's limits and use all the cores of my computer's CPU to run tasks in true parallel.
* **How it Executes:** The script creates 10 completely separate background processes. Each process runs a heavy calculation at the exact same time. The main script waits for all of them to finish and then prints the total time.
* **End Use:** Heavy mathematical tasks, video rendering, or big data processing.
* **Short Summary:** Speeding up heavy tasks by dividing the work across multiple CPU cores.
* **Pros & Cons:** - **Advantages:** Massive speed boost for heavy calculations.
  - **Disadvantages:** Uses a lot of RAM (memory) because each process acts like a completely separate program.

### 8. multithreading_test
* **What I Learned:** I learned how to run tasks concurrently using multiple threads that share the same memory space.
* **How it Executes:** Instead of processes, this creates 10 threads. The threads switch turns so quickly on a single CPU core that it looks like they are running at the exact same time.
* **End Use:** Downloading multiple files from the internet or reading from databases (tasks where the computer mostly has to wait).
* **Short Summary:** Using threads to save time during waiting periods to make the program faster.
* **Pros & Cons:** - **Advantages:** Very lightweight and uses very little memory.
  - **Disadvantages:** Because of Python's structure (the GIL), threads do not actually speed up heavy math tasks.

### 9. serial_test
* **What I Learned:** I learned how normal, step-by-step code execution works, and why we use it as a baseline to measure speed.
* **How it Executes:** A basic loop runs a heavy task 10 times. The program waits for one task to reach 100% completion before starting the next one.
* **End Use:** Used when tasks must be done in a strict order (for example, you must download a file before you can unzip it).
* **Short Summary:** Standard execution of code, used as a baseline to compare against faster parallel methods.
* **Pros & Cons:** - **Advantages:** Simplest to write, completely predictable, and easy to fix bugs.
  - **Disadvantages:** Very slow for large workloads because it only does one thing at a time.

### 10. thread_and_processes
* **What I Learned:** I learned how to benchmark code. Instead of guessing, I learned how to scientifically test which execution method is the fastest.
* **How it Executes:** The script runs the exact same heavy task in three different ways: Serially (one by one), with Multithreading, and with Multiprocessing. It records the completion time for each and prints the results.
* **End Use:** Used during the testing phase of a project to prove which architecture works best for a specific problem.
* **Short Summary:** A final speed test comparing serial code, threads, and processes.
* **Pros & Cons:** - **Advantages:** Gives real data to help you make the best choice for your software.
  - **Disadvantages:** Running multiple heavy tests back-to-back can temporarily max out your computer's CPU.