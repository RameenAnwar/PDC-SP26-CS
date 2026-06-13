# Chapter 1 – Python Fundamentals and Parallel Programming


## Classes and Objects (classes.py)

### What was learned

In this topic, I learned how to create classes and objects in Python. I understood the difference between class variables and instance variables and how they behave differently. I also learned about inheritance by creating a derived class from an existing class.

### How it was executed

The program was executed using the Python interpreter:

```
python classes.py
```

### End use

Classes and objects are used to build structured and scalable applications such as management systems, banking systems, and other real-world software.

### When and how to use

They are used when we need to organize code in a structured way and reuse logic. A class is defined, and objects are created to access its properties and methods.

### Advantages

* Helps in organizing code properly
* Makes code reusable and easier to maintain

### Disadvantages

* Can be difficult to understand at the beginning
* Requires proper planning and design

---

## Conditional Statements and Loops (dir.py, flow.py)

### What was learned

I learned how decision-making works in Python using if, elif, and else statements. I also learned how loops such as for and while are used to repeat tasks efficiently.

### How it was executed

```
python dir.py
python flow.py
```

### End use

These are used in almost every program where decisions are required or tasks need to be repeated multiple times.

### When and how to use

Conditions are used when we need to check specific cases, while loops are used when we need to execute a block of code multiple times based on a condition.

### Advantages

* Helps in building program logic
* Reduces manual repetition of tasks

### Disadvantages

* Wrong conditions can produce incorrect results
* Improper loops can lead to infinite execution

---

## Data Structures (lists.py)

### What was learned

In this topic, I learned about lists, dictionaries, and tuples. These are used to store and manage multiple values in a single variable. I also practiced modifying and accessing data.

### How it was executed

```
python lists.py
```

### End use

Data structures are widely used in applications where large amounts of data need to be stored and processed efficiently.

### When and how to use

They are used when we need to store collections of data. Lists are used for ordered data, dictionaries for key-value pairs, and tuples for fixed data.

### Advantages

* Makes data handling easier
* Allows storage of multiple values

### Disadvantages

* Can become complex when dealing with large datasets
* Requires understanding of different structures

---

## File Handling (file.py)

### What was learned

I learned how to create, write, and read files in Python. This allows storing data permanently outside the program.

### How it was executed

```
python file.py
```

### End use

File handling is used in applications where data needs to be saved for later use, such as logs, records, and reports.

### When and how to use

It is used when we want to store or retrieve data from files. Files are opened in different modes, data is written or read, and then the file is closed.

### Advantages

* Enables permanent storage of data
* Useful for real-world applications

### Disadvantages

* Errors can occur if files are not handled properly
* Risk of data loss

---

## Functions and Modular Code (do_something.py)

### What was learned

I learned how to create functions and reuse them in different parts of the program. This helps in writing cleaner and more organized code.

### How it was executed

This function was used in other programs such as threading and multiprocessing examples.

### End use

Functions are used to simplify complex programs and avoid repetition.

### When and how to use

They are used when a specific task needs to be performed multiple times. The logic is written once and reused whenever needed.

### Advantages

* Reduces code duplication
* Improves readability

### Disadvantages

* Debugging can be slightly difficult in large programs

---

## Serial Execution (serial_test.py)

### What was learned

I learned how tasks are executed one after another in a sequential manner.

### How it was executed

```
python serial_test.py
```

### End use

Used in simple programs where performance is not a major concern.

### Advantages

* Easy to implement and understand

### Disadvantages

* Slower for large and complex tasks

---

## Multithreading (multithreading_test.py)

### What was learned

I learned how multiple threads can run simultaneously to perform tasks concurrently.

### How it was executed

```
python multithreading_test.py
```

### End use

Used in applications where multiple tasks such as file handling or network requests can run at the same time.

### When and how to use

Used when tasks are independent and can run in parallel without heavy CPU usage.

### Advantages

* Improves performance for certain tasks
* Lightweight compared to processes

### Disadvantages

* Limited by Python’s Global Interpreter Lock
* Not suitable for CPU-heavy tasks

---

## Multiprocessing (multiprocessing_test.py)

### What was learned

I learned how multiple processes can run independently to achieve true parallel execution.

### How it was executed

```
python multiprocessing_test.py
```

### End use

Used in applications that require high performance and heavy computations.

### When and how to use

Used when tasks are CPU-intensive and need to be processed faster.

### Advantages

* Provides true parallelism
* Faster execution for heavy workloads

### Disadvantages

* Consumes more memory
* More complex to manage

---

## Threading vs Multiprocessing (thread_and_processes.py)

### What was learned

I compared the performance of threading and multiprocessing and understood the difference between them.

### How it was executed

```
python thread_and_processes.py
```

### End use

Helps in deciding which method to use based on the problem.

### Advantages

* Provides better understanding of performance

### Disadvantages

* Slightly complex to implement and manage

---

