# Chapter 1


## `classes.py`

`classes.py` is a Python file containing a beginner-friendly OOP example.

The script starts by defining `Myclass`, with a class-level variable (`common`), a constructor that sets `myvariable`, and a method that returns that instance value. After that, it creates two objects and prints values to show the difference between class attributes and instance attributes.

Then it updates `Myclass.common`, prints again, and later sets `instance.common` directly to show how one object can have its own value while another object still reads the class value. In the final part, it defines `AnotherClass` as a subclass of `Myclass`, creates an instance, calls an inherited method, and adds a new attribute (`test`) dynamically.

## `dir.py`

`dir.py` is a Python file with two foundational examples: conditions and loops.

The first part checks whether a number is positive, zero, or negative using `if/elif/else`. The second part creates a list of numbers, initializes a running total, loops through each value, and prints the final sum.

This file is mainly about getting comfortable with decision making aAnd simple iteration.

## `do_something.py`

`do_something.py` is a small helper module used by the timing scripts.

It imports `random`, defines `do_something(count, out_list)`, loops `count` times, and appends random float values to the provided list. It is intentionally simple because it acts as the common workload for serial, threading, and multiprocessing examples.

## `file.py`

`file.py` is a basic file I/O demonstration.

It opens `test.txt` in write mode, writes two lines, closes the file, opens it again in read mode, reads everything, prints the content, and closes the file again.

This file shows the core write-read cycle clearly and directly.

## `flow.py`

`flow.py` combines three control-flow patterns in one place.

It begins with an `if/elif/else` sign check, then uses a `for` loop to sum values in a list, and finally uses a `while` loop to sum natural numbers from `1` to `n`.

The goal is to show how different flow-control tools solve different kinds of problems.

## `lists.py`

`lists.py` introduces common Python data structures and basic operations.

It creates and edits lists, prints values by index, builds and updates a dictionary, creates a tuple, and stores `len` in a variable before calling it on a list.

The file is short, but it touches the most common beginner operations you will repeatedly use.

## `multiprocessing_test.py`

`multiprocessing_test.py` is a timing script for multiprocessing.

Inside the `if __name__ == "__main__":` block, it records start time, sets a large workload, creates several process objects targeting `do_something`, starts them, waits for all processes with `join()`, and finally prints elapsed time.

Its purpose is to show how process-based parallelism is structured in Python.

## `multithreading_test.py`

`multithreading_test.py` is the threading version of the timing experiment.

It follows the same pattern as the multiprocessing file: capture time, create worker objects, start them, join them, then print total runtime.

The key idea here is comparing thread-based execution against serial and process-based runs.

## `serial_test.py`

`serial_test.py` is the baseline timing script.

It runs the same workload repeatedly in a normal loop without creating threads or processes, then reports total runtime.

This gives a reference point so the concurrency examples can be compared fairly.

## `thread_and_processes.py`

`thread_and_processes.py` is a combined comparison script.

It defines a shared workload function, includes a commented serial section, runs a threading section, and then runs a multiprocessing section. Both active sections follow the familiar pattern: create workers, start them, join them, and print timing.

This file is useful when you want to see multiple execution models side by side in one script.
