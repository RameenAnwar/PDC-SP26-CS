# Chapter 3

---
## 1. communicating_with_pipe.py

### What I learned:
I learned how to use `multiprocessing.Pipe` to create a direct two-way communication link between processes, allowing one process to send data that another receives.

### How to execute:
Run in cmd: **python communicating_with_pipe.py** to see a pipeline where one process creates numbers, a second squares them, and the main process prints the results.

### Use cases:
Creating high-speed data pipelines or connecting exactly two processes that need to exchange messages frequently.

### Requirements for execution:
The `multiprocessing.Pipe()` function, which returns a pair of connection objects representing the two ends of the pipe.

### Advantages:
Faster than a Queue for simple one-to-one communication because it has less overhead.

### Disadvantages:
Only supports communication between two endpoints; if multiple processes try to read or write to the same end simultaneously, data may be corrupted.

---

## 2. communicating_with_queue.py

### What I learned:
I learned how to use a `multiprocessing.Queue` to share data safely among multiple processes, implementing a Producer-Consumer pattern at the process level.

### How to execute:
Run in cmd: **python communicating_with_queue.py** to see a Producer process fill a queue with random integers while a Consumer process empties it.

### Use cases:
Distributing tasks among a pool of worker processes or aggregating results from multiple parallel computations.

### Requirements for execution:
The `multiprocessing.Queue()` object and the `put()` and `get()` methods.

### Advantages:
Thread and process safe; it handles all the underlying locking for you, making it very robust for multi-process applications.

### Disadvantages:
Slower than pipes because it uses locks and semaphores internally to ensure data integrity.



---

## 3. killing_processes.py

### What I learned:
I learned how to forcefully stop a running process using the `terminate()` method and how to check its status using `is_alive()` and `exitcode`.

### How to execute:
Run in cmd: **python killing_processes.py** to see a process start, get immediately terminated, and then display its exit code.

### Use cases:
Stopping background tasks that are taking too long, or cleaning up child processes when a main application is closed.

### Requirements for execution:
The `terminate()` and `join()` methods to ensures the process is stopped and its resources are cleaned up by the OS.

### Advantages:
Provides immediate control over "runaway" processes that might otherwise hang your system.

### Disadvantages:
Forcefully terminating a process can leave shared resources (like locks or pipes) in a "broken" state or cause data loss.

---

## 4. naming_processes.py

### What I learned:
I learned how to assign custom names to processes to make logs and debugging information much clearer.

### How to execute:
Run in cmd: **python naming_processes.py** to see two processes start: one with a custom name ('myFunc process') and one with a default system name.

### Use cases:
Complex systems where different processes perform distinct roles (e.g., 'DatabaseWorker', 'ImageProcessor').

### Requirements for execution:
The `name` argument in the `multiprocessing.Process` constructor.

### Advantages:
Significantly improves the traceability of logs in large-scale parallel applications.

### Disadvantages:
Naming is purely for human identification; it does not change how the operating system schedules or prioritizes the process.

---

## 5. process_in_subclass.py

### What I learned:
I learned how to create a custom process by subclassing `multiprocessing.Process`, allowing for a more organized, object-oriented approach to parallelism.

### How to execute:
Run in cmd: **python process_in_subclass.py** to spawn 10 custom process objects that each execute their internal `run()` method.

### Use cases:
Building modular parallel applications where each worker needs to maintain its own complex state or internal data.

### Requirements for execution:
Defining a class that inherits from `multiprocessing.Process` and overriding the `run()` method.

### Advantages:
Encapsulates all the logic and data needed for a task within a single, reusable object.

### Disadvantages:
Requires more code than simple function-based processes and can be overkill for very simple tasks.

---

## 6. process_pool.py

### What I learned:
I learned how to use a `Pool` to automatically manage a group of worker processes and distribute a large list of tasks across them using `map()`.

### How to execute:
Run in cmd: **python process_pool.py** to see 100 numbers squared in parallel using a pool of 4 worker processes.

### Use cases:
Batch processing large datasets, performing bulk image conversions, or any "embarrassingly parallel" task.

### Requirements for execution:
The `multiprocessing.Pool` object and the `map()` method, which functions similarly to Python's built-in map.

### Advantages:
Extremely efficient; it automatically handles task distribution and load balancing across all available CPU cores.

### Disadvantages:
All task data must be "pickleable" (serializable) to be sent to the worker processes, which can limit some complex data types.



---

## 7. processes_barrier.py

### What I learned:
I learned how to use a `Barrier` to synchronize multiple processes, ensuring they all "meet" at a specific point before continuing.

### How to execute:
Run in cmd: **python processes_barrier.py** to see processes `p1` and `p2` wait for each other, while `p3` and `p4` run immediately without waiting.

### Use cases:
Simulations where every process must finish "Step 1" before any process can move to "Step 2".

### Requirements for execution:
The `multiprocessing.Barrier` object initialized with the number of processes that must wait.

### Advantages:
Ensures total synchronization in complex multi-stage parallel workflows.

### Disadvantages:
If one process in the group crashes or hangs, every other process at the barrier will be stuck forever.

---

## 8. run_background_processes.py

### What I learned:
I learned the difference between standard processes and "daemon" (background) processes, which are automatically killed when the main program finishes.

### How to execute:
Run in cmd: **python run_background_processes.py** to observe that the background process might not finish its loop if the main program exits first.

### Use cases:
Services like heartbeats, logs, or cleanup tasks that should not keep the computer "busy" if the main app is closed.

### Requirements for execution:
Setting the `.daemon` property to `True` before calling `.start()`.

### Advantages:
Prevents "zombie" processes from staying alive and wasting system resources after your main app has closed.

### Disadvantages:
Daemon processes cannot create child processes of their own.

---

## 9. run_background_processes_no_daemons.py

### What I learned:
I learned that when `.daemon` is set to `False`, the main program will wait for all child processes to finish their work before exiting.

### How to execute:
Run in cmd: **python run_background_processes_no_daemons.py**; notice that even if the main code finishes, the window stays open until every process completes its loop.

### Use cases:
Ensuring that critical tasks—like saving a file or completing a database transaction—are finished even if the user tries to close the app.

### Requirements for execution:
Setting the `.daemon` property to `False` (which is the default behavior in Python).

### Advantages:
Guarantees that no work is left half-finished; safer for data-sensitive operations.

### Disadvantages:
If a child process gets stuck in an infinite loop, the entire application will hang and never close properly.

Here are the details for the final two files, which focus on different methods of importing and launching functions in a multi-process environment:

---

## 10. spawning_processes.py

### What I learned:
I learned the fundamental way to spawn a process by targeting a function defined within the same script file, using the `multiprocessing.Process` constructor.

### How to execute:
Run in cmd: **python spawning_processes.py** to see six sequential processes execute a loop that prints an increasing number of lines based on the process index.

### Use cases:
Simple scripts where the parallel logic is short enough to be kept in the main file without making the code messy.

### Requirements for execution:
The `if __name__ == '__main__':` guard is required on Windows to prevent the script from accidentally calling itself in an infinite loop when spawning new processes.

### Advantages:
Very easy to read and manage since all the code is in one single file; no need to manage external dependencies or modules.

### Disadvantages:
As the project grows, keeping all functions in one file can make the code difficult to navigate and maintain.

---

## 11. spawning_processes_namespace.py

### What I learned:
I learned how to spawn processes by targeting functions imported from an external module (namespace), which is essential for building professional, multi-file Python applications.

### How to execute:
Run in cmd: **python spawning_processes_namespace.py**; it will perform the exact same task as the previous file, but it fetches the `myFunc` logic from the `myFunc.py` file instead.

### Use cases:
Large-scale applications where different tasks (like data scraping, image processing, and database writing) are stored in separate files for better organization.

### Requirements for execution:
Must have the `myFunc.py` file located in the same directory (or the Python path) so the script can import it.

### Advantages:
Promotes "Code Reusability"—you can write a function once in a module and use it in many different multi-processing scripts across your project.

### Disadvantages:
Slightly more complex to manage because you have to ensure all external files/modules are correctly linked and present in the environment.