# Chapter 3: Process Based Parallelism

This folder contains example Python scripts illustrating the `multiprocessing` module. Each file demonstrates a different concept: process creation, pipes, queues, termination, naming, barriers, subclassing, process pools, background/daemon processes, and the importance of the `if __name__ == '__main__'` guard.

---

## Files and What They Do

### `communicating_with_pipe.py`
- Demonstrates process communication using `multiprocessing.Pipe`.
- `create_items` sends integers `0` through `9` over the first pipe.
- `multiply_items` reads values from the first pipe, squares them, and sends results through the second pipe.
- The main process receives and prints the squared values.

Expected output:
- `0`
- `1`
- `4`
- `9`
- `16`
- `25`
- `36`
- `49`
- `64`
- `81`
- `End`

> Note: The script prints one number per line, followed by `End` after the second pipe closes.

### `communicating_with_queue.py`
- Demonstrates producer/consumer communication using `multiprocessing.Queue`.
- A `producer` process inserts 10 random integers into the queue.
- A `consumer` process removes items until the queue is empty.

Expected behavior:
- Several lines like `Process Producer : item <n> appended to queue Process-1`
- Lines reporting `The size of queue is <size>` for the producer.
- Lines like `Process Consumer : item <n> popped from by Process-2`
- If the consumer checks the queue before the producer fills it, it may print `the queue is empty`.

> Note: The order of producer and consumer output is not strictly deterministic. The queue size and printed items may vary between runs.

### `killing_processes.py`
- Shows how to start a process and terminate it early with `terminate()`.
- The child process begins a loop printing `-->0` to `-->9`, but the parent terminates it immediately.

Expected output structure:
- `Process before execution: <Process ...> False`
- `Process running: <Process ...> True`
- `Process terminated: <Process ...> False`
- `Process joined: <Process ...> False`
- `Process exit code: <code>`

Possible additional output:
- The child may print `Starting function` before termination.
- The exact exit code depends on the platform (often `-1` on Windows).

### `myFunc.py`
- Defines a helper function used by other examples.
- `myFunc(i)` prints the process number and then prints `output from myFunc is :<j>` for `j` from `0` to `i-1`.

No output when run directly unless imported and called.

### `naming_processes.py`
- Demonstrates naming processes explicitly.
- Creates two processes that run `myFunc()` and prints the current process name.

Expected output:
- `Starting process name = myFunc process`
- `Starting process name = Process-1`
- `Exiting process name = myFunc process`
- `Exiting process name = Process-1`

> Both processes sleep for 3 seconds before exiting. The order may vary depending on scheduling.

### `processes_barrier.py`
- Demonstrates the use of `multiprocessing.Barrier` and `Lock`.
- Two processes wait at the barrier, then print timestamps together.
- Two other processes print without barrier synchronization.

Expected output:
- Two `process p3 - test_without_barrier ...` / `process p4 - test_without_barrier ...` lines
- Two `process p1 - test_with_barrier ...` / `process p2 - test_with_barrier ...` lines

> The barrier ensures `p1` and `p2` print at almost the same time, while `p3` and `p4` are unsynchronized and may appear earlier or later.

### `process_in_subclass.py`
- Demonstrates creating a custom process class by subclassing `multiprocessing.Process`.
- Overrides `run()` to print the process name.

Expected output:
- Ten lines like `called run method in Process-1`, `called run method in Process-2`, etc.

> Each process is started and joined immediately, so the output appears sequentially.

### `process_pool.py`
- Demonstrates using a process pool with `multiprocessing.Pool`.
- Squares the integers 0 through 99 in parallel using 4 worker processes.
- Prints the resulting list of squares.

Expected output:
- One line: `Pool    : [0, 1, 4, 9, ..., 9801]`

> The list contains 100 squared values from `0` to `99*99`.

### `run_background_processes.py`
- Demonstrates daemon vs non-daemon processes.
- `background_process` is marked as a daemon.
- `NO_background_process` is non-daemon.
- The main program starts both but does not join them.

Expected behavior:
- `NO_background_process` will run to completion and print `Starting NO_background_process`, output `5` through `9`, and `Exiting NO_background_process`.
- `background_process` may be terminated early when the main program exits, because daemon processes do not keep the interpreter alive.

Possible output:
- `Starting background_process`
- `---> 0` through `---> 4`
- `Exiting background_process` (if it finishes before the main process ends)
- `Starting NO_background_process`
- `---> 5` through `---> 9`
- `Exiting NO_background_process`

### `run_background_processes_no_daemons.py`
- Similar to `run_background_processes.py`, but both processes are non-daemon.
- Both processes are allowed to complete before Python exits.

Expected output:
- `Starting background_process`
- `Starting NO_background_process`
- `---> 0` through `---> 4`
- `Exiting background_process`
- `---> 5` through `---> 9`
- `Exiting NO_background_process`

> Order may vary, but both child processes must finish before the interpreter exits.

### `spawning_processes.py`
- Demonstrates spawning processes with a locally defined function.
- Starts and joins one process at a time for `i` from `0` to `5`.

Expected output:
- For `i=0`: `calling myFunc from process n°: 0`
- For `i=1`: `calling myFunc from process n°: 1` and `output from myFunc is :0`
- For `i=2`: `calling myFunc from process n°: 2` and outputs `0`, `1`
- ...
- For `i=5`: `calling myFunc from process n°: 5` and outputs `0` through `4`

> Because each process is joined before the next starts, the output is sequential.

### `spawning_processes_namespace.py`
- Same behavior as `spawning_processes.py`.
- Imports `myFunc` from `myFunc.py` instead of defining it in the same file.

Expected output is identical to `spawning_processes.py`.

---

## Notes
- Most examples require the `if __name__ == '__main__'` guard on Windows to avoid recursive process spawning.
- `multiprocessing.Queue.empty()` and `multiprocessing.Queue.qsize()` are not always reliable across processes and may behave differently on Windows.
- Daemon processes are terminated when the main process exits, while non-daemon processes keep the interpreter alive until they finish.
- Outputs that involve multiple concurrent processes may appear in different orders between runs.

## How to Run
Use a command prompt or PowerShell and run each script directly, for example:

```powershell
python communicating_with_pipe.py
python process_pool.py
python spawning_processes.py
```

For `spawning_processes_namespace.py`, ensure that `myFunc.py` is in the same directory.
