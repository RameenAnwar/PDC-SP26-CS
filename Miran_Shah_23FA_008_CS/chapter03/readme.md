
# Chapter 3: Process-Based Parallelism

This chapter explores the `multiprocessing` module in Python. Unlike threads, processes do not share memory space, which allows them to bypass the Global Interpreter Lock (GIL) and achieve true parallel execution on multi-core systems.

-----

### Table of Contents

1.  spawning processes.py 
2.  naming processes.py
3.  runbackground processes.py
4.  run background processes no daemons.py
5.  killing processes.py
6.  process in subclass.py
7.  communicating with queue.py
8.  communicating with pipe.py
9.  processes barrier.py
10. spawning processes namespace.py
11. process pool.py

-----

### 1. spawning processes.py

  * **What it is:** The most basic way to start a new process.
  * **The Concept:** Think of this as launching a completely separate instance of Python to run a specific function. It is "heavier" than a thread but runs independently.
  * **The Code Logic:** You define a function, create a `multiprocessing.Process` object pointing to that function, and call `.start()`.
  * **Simple Summary:** Spawns an independent worker to run a task in its own memory space.

### 2. naming processes.py

  * **What it is:** Assigning human-readable names to your processes.
  * **The Concept:** By default, processes are named "Process-1", "Process-2". Giving them custom names makes it much easier to track which worker is doing what during debugging.
  * **The Code Logic:** You pass the `name` argument (e.g., `name='MyWorker'`) during process initialization.
  * **Simple Summary:** Labels processes so you can identify them in logs or error messages.

### 3\. run\_background\_processes.py

  * **What it is:** Creating "Daemon" processes.
  * **The Concept:** A Daemon process is a background worker that is not essential. If the main program finishes, the Daemon is killed immediately.
  * **The Code Logic:** Setting `process.daemon = True` before starting.
  * **Simple Summary:** Useful for non-critical tasks like background monitoring that should stop when the app closes.

### 4\. run\_background\_processes\_no\_daemons.py

  * **What it is:** Running processes that are *not* daemons.
  * **The Concept:** Unlike daemons, these processes are considered essential. Even if the main program finishes its lines of code, it will stay "alive" and wait for these processes to finish.
  * **The Code Logic:** By default, `daemon` is `False`. The main program joins them implicitly.
  * **Simple Summary:** Ensures that important background work (like saving a file) is completed before the program exits.

### 5\. killing\_processes.py

  * **What it is:** Forcibly stopping a process.
  * **The Concept:** Sometimes a process hangs or is no longer needed. This is like using "End Task" in your computer's Task Manager.
  * **The Code Logic:** Calling the `.terminate()` method.
  * **Simple Summary:** Immediately stops a process, but must be used carefully to avoid leaving "zombie" processes.

### 6\. process\_in\_subclass.py

  * **What it is:** Creating a custom process class.
  * **The Concept:** Instead of just passing a function to a process, you create a dedicated class. This is the Object-Oriented way to handle complex workers.
  * **The Code Logic:** Inherit from `multiprocessing.Process` and override the `run()` method with your logic.
  * **Simple Summary:** A cleaner, more organized way to build complex, reusable worker objects.

### 7\. communicating\_with\_queue.py

  * **What it is:** Sharing data using a Queue.
  * **The Concept:** Processes can't share variables. A `Queue` is a shared "mailbox" where one process drops data and another picks it up.
  * **The Code Logic:** Use `queue.put()` to send data and `queue.get()` to receive it.
  * **Simple Summary:** A safe, thread-safe way for isolated processes to talk to each other.

### 8\. communicating\_with\_pipe.py

  * **What it is:** Direct two-way communication between two processes.
  * **The Concept:** A `Pipe` is like a walkie-talkie link between exactly two workers. It is faster than a queue but less flexible.
  * **The Code Logic:** `Pipe()` returns two ends. Data sent into one end comes out the other.
  * **Simple Summary:** Best for high-speed, point-to-point data exchange.

### 9\. processes\_barrier.py

  * **What it is:** Synchronizing multiple processes at a checkpoint.
  * **The Concept:** If you have 4 processes doing different parts of a calculation, a `Barrier` makes them all wait at a specific line until everyone is ready.
  * **The Code Logic:** Define a `Barrier(n)` and call `barrier.wait()`.
  * **Simple Summary:** Keeps multiple processes "in sync" so one doesn't get too far ahead of the others.

### 10\. spawning\_processes\_namespace.py

  * **What it is:** Managing shared state with a Namespace.
  * **The Concept:** Since processes have separate memory, a `Namespace` (via a `Manager`) provides a special object that acts like shared memory.
  * **The Code Logic:** Use `multiprocessing.Manager().Namespace()` to create variables that all processes can read and write to.
  * **Simple Summary:** A way to simulate "shared variables" across isolated processes.

### 11\. process\_pool.py

  * **What it is:** Managing a group (pool) of workers.
  * **The Concept:** Instead of creating 100 processes for 100 tasks, you create a "Pool" of (for example) 4 workers that stay alive and take tasks from a list one by one.
  * **The Code Logic:** Use `multiprocessing.Pool()` and the `.map()` function to distribute work.
  * **Simple Summary:** The most efficient and automated way to handle bulk parallel processing.