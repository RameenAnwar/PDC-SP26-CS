# Chapter 02

This chapter focuses on Python threading and the main synchronization tools available in the `threading` module.

## `Thread_definition.py`

- Minimal example of creating a thread with a target function and one argument.
- Each thread is started and joined inside the same loop, so execution stays effectively sequential.

## `Thread_determine.py`

- Creates three named threads.
- Each function prints the thread name when it starts and when it exits.

## `Thread_name_and_processes.py`

- Defines a custom thread class by inheriting from `Thread`.
- The `run()` method prints the logical thread name and the script ends after both threads finish.

## `MyThreadClass.py`

- Builds a reusable `Thread` subclass with a random sleep duration.
- Nine threads are created, started, and then joined together.

## `MyThreadClass_lock.py`

- Uses one shared `Lock`.
- Each thread holds the lock across both its print statement and its sleep, so the critical section becomes long and execution is heavily serialized.

## `MyThreadClass_lock_2.py`

- Uses the same thread structure but reduces the lock scope.
- Only the first print is protected, while `sleep()` happens outside the lock.

## `Rlock.py`

- Demonstrates `threading.RLock`.
- `Box.add()` and `Box.remove()` both call another method that also acquires the same lock, which is exactly the situation where a re-entrant lock is useful.

## `Semaphore.py`

- Shows a simple producer-consumer style handshake with `threading.Semaphore`.
- A consumer waits on `acquire()` and the producer releases the semaphore after creating an item.

## `Condition.py`

- Uses `threading.Condition` around a shared `items` list.
- The producer waits when the list reaches ten items and the consumer waits when the list is empty.

## `Event.py`

- Demonstrates `threading.Event` for signal-based coordination.
- The producer appends an item, sets the event, and clears it again.
- The consumer runs forever, so the final `join()` on the consumer can keep the program from terminating normally.

## `Barrier.py`

- Creates three threads that all stop at the same barrier until everyone arrives.
- The script uses a race-style example with runner names and random delays.

## `Threading_with_queue.py`

- Uses `Queue` to pass items from one producer thread to multiple consumer threads.
- The consumers run forever, so the `join()` calls on those threads can block indefinitely after the produced items are exhausted.

## How to run

Run any file directly, for example:

```bash
python Thread_definition.py
python Barrier.py
```
