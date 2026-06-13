# Chapter 2 Threading Examples

This chapter demonstrates Python threading and synchronization primitives using multiple small example scripts. Each file shows a different threading concept: thread creation, locks, barriers, conditions, events, semaphores, queues, and custom thread classes.

## Files and What They Do

### `Thread_definition.py`
- **Purpose**: Show how to create and start simple threads.
- **Behavior**: Creates 10 threads, each calling `my_func` with a thread number.
- **Code Explanation**: Uses `threading.Thread` to spawn threads that execute a function with arguments. Each thread starts and joins immediately.
- **Expected Output**: Prints `my_func called by thread N°0` through `N°9` sequentially.
- **Result of Execution**: Since threads are joined right after starting, they run sequentially, not concurrently. Total execution time is the sum of all thread executions.

### `Thread_determine.py`
- **Purpose**: Run three named threads concurrently.
- **Behavior**: Starts `function_A`, `function_B`, and `function_C` in separate threads, each sleeping for 2 seconds.
- **Code Explanation**: Demonstrates thread naming and concurrent execution. Threads print start and exit messages.
- **Expected Output**: Interleaved messages like `function_A--> starting`, sleeps, then `function_A--> exiting`, similarly for others.
- **Result of Execution**: Threads run concurrently; total time is about 2 seconds (longest sleep), not 6 seconds.

### `Thread_name_and_processes.py`
- **Purpose**: Demonstrate thread creation and thread naming.
- **Behavior**: Starts two threads that print a message identifying the thread.
- **Code Explanation**: Custom Thread subclass that prints its name. Note: It says "process" but actually prints thread label.
- **Expected Output**: `ID of process running Thread#1`, `ID of process running Thread#2`, then `End`.
- **Result of Execution**: Simple concurrent execution of two threads.

### `MyThreadClass.py`
- **Purpose**: Define a custom `Thread` subclass and run multiple threads concurrently.
- **Behavior**: Creates 9 threads that print a running message, sleep for a random duration (1-10 seconds), then print `over`.
- **Code Explanation**: Inherits from Thread, overrides run(). Uses random sleep to simulate variable work.
- **Expected Output**: Each thread prints start message with PID, sleeps, prints over. Messages may interleave.
- **Result of Execution**: Parallel execution; total time equals the maximum sleep duration among threads.

### `MyThreadClass_lock.py`
- **Purpose**: Show how a lock can serialize thread execution.
- **Behavior**: Each thread acquires a global lock before sleeping, holds it for its full duration, then releases it.
- **Code Explanation**: Uses `threading.Lock` to ensure only one thread runs at a time.
- **Expected Output**: Thread start and finish messages appear one after another, no interleaving.
- **Result of Execution**: Serial execution; total runtime is the sum of all sleep times (up to 90 seconds).

### `MyThreadClass_lock_2.py`
- **Purpose**: Compare locking only around a critical section.
- **Behavior**: Threads acquire the lock only for the initial print, then release it before sleeping.
- **Code Explanation**: Lock protects only the critical section (print), allowing concurrency in the sleep phase.
- **Expected Output**: Initial startup prints are serialized, but finish messages may interleave.
- **Result of Execution**: Mostly concurrent; total time close to max sleep, with serialized prints.

### `Barrier.py`
- **Purpose**: Demonstrate `threading.Barrier` for waiting until a group of threads reaches the same point.
- **Behavior**: Three runner threads each sleep a random time (2-5 seconds), print when they reach the barrier, then wait for the others.
- **Code Explanation**: Barrier ensures all threads wait until all have arrived before proceeding.
- **Expected Output**: Three arrival messages at different times, then `Race over!` when all have waited.
- **Result of Execution**: Program waits for the slowest thread; demonstrates synchronization point.

### `Condition.py`
- **Purpose**: Show producer/consumer coordination with `threading.Condition`.
- **Behavior**: Producer adds items to a shared list (up to 10), waits if full. Consumer removes items, waits if empty.
- **Code Explanation**: Uses Condition for waiting/notifying between producer and consumer threads.
- **Expected Output**: Logging messages showing production, consumption, waiting, and notifications.
- **Result of Execution**: Coordinated access; producer waits when buffer full, consumer when empty.

### `Event.py`
- **Purpose**: Demonstrate `threading.Event` signaling between threads.
- **Behavior**: Producer generates 5 items, appends to list, sets event. Consumer waits for event, pops item.
- **Code Explanation**: Event allows one thread to signal others. Producer sets/clears event for each item.
- **Expected Output**: Logs for production and consumption.
- **Result of Execution**: Consumer processes items as produced; demonstrates event-based signaling.

### `Rlock.py`
- **Purpose**: Demonstrate a reentrant lock (`threading.RLock`).
- **Behavior**: Box class uses RLock; add/remove methods call execute, which is also locked.
- **Code Explanation**: RLock allows the same thread to acquire the lock multiple times (reentrancy).
- **Expected Output**: Print statements for adding and removing item counts.
- **Result of Execution**: Safe nested locking; prevents deadlocks in recursive calls.

### `Semaphore.py`
- **Purpose**: Demonstrate a semaphore for producer/consumer signaling.
- **Behavior**: Consumer waits on acquire; producer releases after producing. Runs 10 times.
- **Code Explanation**: Semaphore starts at 0; producer releases to allow consumer to proceed.
- **Expected Output**: Logs showing consumer waiting, producer producing, consumer notified.
- **Result of Execution**: Each producer release allows one consumer to proceed.

### `Threading_with_queue.py`
- **Purpose**: Show thread-safe communication using `queue.Queue`.
- **Behavior**: One producer puts 5 items; three consumers get them.
- **Code Explanation**: Queue provides thread-safe FIFO. Consumers run in infinite loop.
- **Expected Output**: Producer append messages, consumer pop messages.
- **Result of Execution**: Items processed by consumers; program hangs on join since consumers don't exit.

## How to Run the Examples

Use Python from the terminal in this directory:

```powershell
python Thread_definition.py
python Thread_determine.py
python Thread_name_and_processes.py
python MyThreadClass.py
python MyThreadClass_lock.py
python MyThreadClass_lock_2.py
python Barrier.py
python Condition.py
python Event.py
python Rlock.py
python Semaphore.py
python Threading_with_queue.py
```

## Advantages for Users

Threading in Python offers several key advantages:

- **Concurrency and Performance**: Allows multiple operations to run simultaneously, improving performance for I/O-bound tasks and better utilizing multi-core CPUs.
- **Responsiveness**: Keeps applications responsive by offloading long-running tasks to background threads (e.g., UI remains interactive).
- **Resource Sharing**: Threads share memory space, enabling efficient data sharing without complex inter-process communication.
- **Simplified Programming**: Easier to implement concurrent behavior compared to multiprocessing, with lower overhead.
- **Synchronization Primitives**: Tools like locks, barriers, conditions, events, semaphores, and queues prevent race conditions and ensure thread safety.
- **Scalability**: Better handling of multiple clients or tasks in server applications.
- **Learning Tool**: These examples help understand threading concepts, which are essential for advanced programming in concurrent systems.

By mastering these primitives, users can build robust, efficient multi-threaded applications that handle concurrency challenges effectively.
