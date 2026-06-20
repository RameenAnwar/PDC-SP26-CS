# Chapter 01

This chapter contains introductory Python examples and three timing-based comparisons between serial, threaded, and process-based execution.

## `classes.py`

- Demonstrates class attributes, instance attributes, inheritance, and dynamic attribute creation.
- `Myclass.common` is shared across instances until one object overrides it locally.
- `AnotherClass` inherits `myfunction()` and prints a constructor argument.

## `dir.py`

- Contains two small examples.
- The first checks whether a number is positive, zero, or negative.
- The second sums a list of integers with a `for` loop.

## `do_something.py`

- Defines `do_something(count, out_list)`.
- The function appends random floating-point values to a list and is reused by the timing scripts.

## `file.py`

- Writes two lines into `test.txt`, reads the file again, and prints the content.
- This is the chapter's file handling example.

## `flow.py`

- Combines `if`, `for`, and `while` examples in one file.
- The script checks number sign, sums a list, and computes the sum `1 + 2 + ... + n`.

## `lists.py`

- Shows basic list, dictionary, and tuple usage.
- Also demonstrates indexing, updating values, and storing `len` in a variable before calling it.

## `serial_test.py`

- Runs the same workload ten times in a normal loop.
- It acts as the serial baseline for later comparison with threads and processes.

## `multithreading_test.py`

- Intended to compare threading performance against the serial and multiprocessing versions.
- In the current code, `do_something(size, out_list)` is evaluated immediately while each thread is being created, so each thread receives `None` as its target.
- The README note for this file should therefore be based on the script's actual code, not on the intended threading pattern.

## `multiprocessing_test.py`

- Creates ten `multiprocessing.Process` workers.
- Each worker runs `do_something()` and the program reports total elapsed time after `join()`.

## `thread_and_processes.py`

- Places threading and multiprocessing examples in one file.
- The serial section is commented out.
- The threading part uses the same immediate-call pattern seen in `multithreading_test.py`, while the multiprocessing section passes a proper target plus arguments.

## `test.txt`

- Small text file used by `file.py`.

## How to run

Run any file from this chapter folder, for example:

```bash
python classes.py
python serial_test.py
```
