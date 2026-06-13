# Chapter 2


## `Barrier.py`

`Barrier.py` demonstrates barrier synchronization with a race-style example.

The script defines three runners, creates a `Barrier` for the same count, and starts one thread per runner. Inside each thread, a name is picked, the thread sleeps for a random short time, prints when it reaches the finish point, and then calls `wait()` on the barrier. No thread can pass that point until all runners arrive, so you can clearly see synchronized completion.

This is a clean way to understand how `Barrier` keeps threads in sync.

## `Condition.py`

`Condition.py` is a producer-consumer example built with `threading.Condition`.

It creates a shared `items` list and one condition object that both threads use. The producer runs faster, appends values until the list reaches a size limit, and then blocks with `wait()`. The consumer runs slower, removes values, and waits when the list is empty. Each side calls `notify()` after changing the list so the other side can continue, which shows classic coordinated handoff under a shared lock.

This file is great for learning coordinated waiting and signaling between threads.

## `Event.py`

`Event.py` shows event-based synchronization.

A producer thread generates random items in a loop, appends them to a shared list, sets the event to signal availability, and then clears it for the next cycle. The consumer thread repeatedly sleeps, blocks on `event.wait()`, then pops an item once signaled. This keeps the signaling logic simple: producer announces readiness, consumer reacts to that signal.

The core idea is simple: one thread signals readiness, the other reacts.

## `MyThreadClass.py`

`MyThreadClass.py` introduces a custom thread class.

It subclasses `Thread`, stores a thread name and sleep duration, and overrides `run()` to print a start message, sleep, and print an end message. In `main()`, it creates nine thread objects with random durations, starts all of them, then joins all of them so the program waits for complete execution before printing the total elapsed time.

This file teaches the basic pattern for custom thread classes.

## `MyThreadClass_lock.py`

`MyThreadClass_lock.py` builds on the previous example by adding a lock.

Each thread acquires one shared `Lock` at the start of `run()`, performs its print-and-sleep work while holding the lock, and releases it at the end. Because the lock is held across the full section, threads effectively run that section one at a time. This makes execution safer for shared resources, but also more serialized.

This helps show how locks prevent overlapping access to shared work.

## `MyThreadClass_lock_2.py`

`MyThreadClass_lock_2.py` uses the same setup but changes lock scope.

Here, each thread acquires the lock only for the protected print block and releases it immediately after. The sleep call happens outside the lock, so other threads do not have to wait for that delay. This makes the critical section shorter and demonstrates why lock scope matters for concurrency.

This file highlights how lock placement affects concurrency and performance.

## `Rlock.py`

`Rlock.py` demonstrates re-entrant locking with `RLock`.

The `Box` class wraps a shared counter and protects updates with `RLock`. Methods like `add()` and `remove()` acquire the lock and call `execute()`, which also acquires the same lock. With a normal `Lock`, nested acquisition by the same thread could deadlock; with `RLock`, that nested call is allowed. Two worker threads run add/remove loops and print progress as the count changes.

This is useful when nested method calls need the same lock.

## `Semaphore.py`

`Semaphore.py` is a simple semaphore signaling example.

For each iteration, the consumer thread starts and blocks on `semaphore.acquire()`. The producer sleeps briefly, creates a random item value, logs it, and calls `semaphore.release()`. That release grants one permit, allowing the consumer to continue and print the item. Running this repeatedly makes it easy to see permit-based synchronization in action.

It is a straightforward demonstration of permit-based synchronization.

## `Threading_with_queue.py`

`Threading_with_queue.py` shows thread communication through `Queue`.

A producer thread creates a few random items and pushes them into the queue with `put()`. Multiple consumer threads run an infinite loop, block on `get()` until an item arrives, process that item, and call `task_done()`. Since `Queue` handles internal locking, this approach avoids manual lock code for message passing and models real producer-consumer pipelines.

This file is a practical producer-consumer pattern used in real projects.

## `Thread_definition.py`

`Thread_definition.py` covers the minimal thread setup.

It defines one simple worker function that prints which thread number called it. In `main()`, a loop creates a thread for each index, starts it, and joins it before moving to the next one. The immediate join keeps execution ordered, making this a very clear first example of thread creation and argument passing.

This is the easiest starting point for understanding Python threading syntax.

## `Thread_determine.py`

`Thread_determine.py` demonstrates named threads.

It defines three worker functions with similar logic: print a start message, sleep, and print an exit message. The script creates three threads with explicit names tied to those functions, starts them almost together, and joins all of them. Because each function prints `currentThread().getName()`, the output clearly shows which named thread is active.

The output helps you see which named thread is running at each stage.

## `Thread_name_and_processes.py`

`Thread_name_and_processes.py` is another custom thread identity example.

It defines a small `Thread` subclass whose `run()` method prints a message containing the thread identity. In `main()`, two thread objects are created, started, and joined, followed by an `End` message. The flow is simple, but it reinforces the standard lifecycle: construct, start, run, join, then exit.

This file reinforces thread naming and basic thread lifecycle flow.

