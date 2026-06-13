# Chapter 03 — Process-Based Parallelism

This README explains each Python file in this folder and how the example works.

- `processes_barrier.py`:
  - Demonstrates `multiprocessing.Barrier` synchronization and a `Lock` used to serialize output.
  - `test_with_barrier` waits on the `Barrier`, records a timestamp and prints it inside a `Lock`.
  - `test_without_barrier` prints a timestamp immediately. The `__main__` block starts two barrier-synchronized processes and two unsynchronized ones.

- `naming_processes.py`:
  - Shows how to name `multiprocessing.Process` instances and observe their `name` attribute.
  - Starts two processes (one with an explicit name, one with the default name) that sleep then exit.

- `myFunc.py`:
  - Simple helper function `myFunc(i)` used by other examples; prints a few lines and returns.

- `killing_processes.py`:
  - Demonstrates creating a process, starting it, and terminating it with `p.terminate()`.
  - Prints `is_alive()` and `exitcode` to show process lifecycle changes.

- `communicating_with_queue.py`:
  - Defines a `producer` and `consumer` subclassing `multiprocessing.Process` and sharing a `multiprocessing.Queue`.
  - Producer puts random items into the queue; consumer pops until the queue is empty. Shows use of `queue.qsize()` and `queue.empty()`.

- `communicating_with_pipe.py`:
  - Demonstrates `multiprocessing.Pipe` in a pipeline: one process creates items, another reads and squares them, and the main process prints results.
  - Uses nonblocking transfer patterns and closes pipe endpoints explicitly; handles `EOFError` to detect stream end.

- `run_background_processes.py` and `run_background_processes_no_daemons.py`:
  - Both illustrate `daemon` vs non-daemon processes. `run_background_processes.py` sets one process as daemon (`daemon = True`), while the latter sets `daemon = False` for both.
  - Each process prints different ranges depending on its name; useful to see how daemon processes behave on program exit.

- `process_pool.py`:
  - Shows `multiprocessing.Pool` usage with `pool.map` to compute squares of a list of integers using a pool of worker processes.
  - Demonstrates `pool.close()` and `pool.join()` lifecycle.

- `process_in_subclass.py`:
  - Illustrates subclassing `multiprocessing.Process` by overriding `run()` in `MyProcess`.
  - Starts and joins several instances.

- `spawning_processes.py` and `spawning_processes_namespace.py`:
  - `spawning_processes.py` spawns multiple processes by calling a locally defined `myFunc` in a loop.
  - `spawning_processes_namespace.py` imports `myFunc` from `myFunc.py` and spawns processes the same way; demonstrates using module-level functions across files.

How to run

- Run examples from the chapter folder, e.g.:

```
python processes_barrier.py
python communicating_with_queue.py
```

Notes

- Many examples print to stdout from multiple processes; using `Lock` (as in `processes_barrier.py`) helps keep output readable.
- Some scripts (like `communicating_with_pipe.py`) rely on `EOFError` handling and explicit pipe closing.
