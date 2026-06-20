# Chapter 03

This chapter moves from threads to processes and demonstrates multiple multiprocessing patterns.

## `spawning_processes.py`

- Spawns a separate process for each loop iteration.
- The worker function is defined inside the same file.

## `spawning_processes_namespace.py`

- Spawns processes the same way, but imports the worker from `myFunc.py`.
- This shows how process targets can be placed in a reusable module.

## `myFunc.py`

- Contains the helper function used by `spawning_processes_namespace.py`.
- The function prints the process index and a short sequence of values.

## `process_in_subclass.py`

- Demonstrates subclassing `multiprocessing.Process`.
- Each process overrides `run()` and prints its own process name.

## `naming_processes.py`

- Compares a custom process name with a default process name.
- Each child process prints when it starts and when it exits.

## `run_background_processes.py`

- Shows the effect of setting one process as a daemon.
- The script starts both processes but does not `join()` them, which helps demonstrate background-process behavior.

## `run_background_processes_no_daemons.py`

- Uses the same structure but sets both processes as non-daemon.
- This keeps both workers as normal child processes.

## `killing_processes.py`

- Starts a process, terminates it, joins it, and prints lifecycle information such as `is_alive()` and `exitcode`.

## `processes_barrier.py`

- Demonstrates `multiprocessing.Barrier` together with a `Lock`.
- Two processes wait at the barrier while two others print immediately.

## `communicating_with_queue.py`

- Uses a `multiprocessing.Queue` shared by a producer and a consumer process.
- The producer inserts random items and the consumer removes them until the queue becomes empty.

## `communicating_with_pipe.py`

- Builds a two-stage pipeline using `multiprocessing.Pipe`.
- One child sends numbers, another squares them, and the parent prints the results until `EOFError`.

## `process_pool.py`

- Uses `multiprocessing.Pool(processes=4)` and `map()` to square a range of integers.
- This is the chapter's pool-based parallelism example.

## How to run

Examples:

```bash
python spawning_processes.py
python process_pool.py
```
