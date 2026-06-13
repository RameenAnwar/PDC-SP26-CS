###### 

###### CHAPTER 2



\--------------------------------------------------------------------------------------------------------------------------------------------------



File Name: Thread\_definition.py



\## Description

Threading is a technique that allows a program to run multiple tasks concurrently, improving efficiency and responsiveness.



\## How and When to Execute

Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)

It is executed when you have independent tasks that don’t need require concurrency or shared resource management.



\## What We Learned

\- Threads allow a program to perform multiple tasks simultaneously.



\## Advantages

\- Easy to implement and understand.

\- Useful for understanding the concept of threading.



\## Disadvantages

\- Threads are not running concurrently(in the code).

\- Limited real world use (mainly used for learning purposes).



\--------------------------------------------------------------------------------------------------------------------------------------------------



File Name: Thread\_Determine.py



\## Description

This program demonstrates creating multiple threads with each executing a separate function simultaneously, this shows how threads can operate independently with proper lifecycle management.



\## How and When to Execute

Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device).
This program is executed when performing multiple independent tasks concurrently, such as I/O operations, background computations, or parallel function calls.



\## What We Learned

\- How concurrent execution allows multiple functions to run simultaneously, reducing overall execution time.

\- The concept of the methods start() and join() to control thread execution and completion.



\## Advantages

\- Multiple functions run concurrently, improving efficiency.

\- Using a good naming convention makes debugging easier.



\## Disadvantages

\- Race condition may occur if different threads have a shared resource among them.

\- Overhead of creating multiple threads for small tasks.



\--------------------------------------------------------------------------------------------------------------------------------------------------



File Name: Thread\_name\_and\_processes.py



\## Description

This program demonstrates creating a custom thread class in Python to run simple tasks concurrently, showing each thread’s execution while also showcasing the functionality of multithreading.



\## How and When to Execute

Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device).

This program is executed when performing multiple independent tasks simultaneously.



\## What We Learned

\- How to create a custom thread class by inheriting from Thread.

\- How to start multiple threads using start() and wait for completion using join().



\## Advantages

\- Threads can run concurrently, improving efficiency for independent tasks.

\- The use of a custom thread class allows us to give a better structure.



\## Disadvantages

\- We may encounter race condition if shared resources are added.

\- Output order is not guaranteed, as threads run concurrently.



\--------------------------------------------------------------------------------------------------------------------------------------------------



File Name: MyThreadClass.py



\## Description

Multithreading is a technique that allows multiple threads to run concurrently within a single program, improving efficiency and performance.

This program demonstrates the use of multithreading in Python by creating multiple threads that run concurrently. Each thread performs a task (sleep for a random duration) and prints its execution status.



\## How and When to Execute

Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)

It is executed when performing multiple tasks simultaneously, especially in I/O-bound operations or when controlled thread execution is required.





\## What We Learned

\- The concept of multithreading and how threads run concurrently.



\## Advantages

\- Better resource utilization.

\- Runs multiple tasks at once which reduces total execution time.



\## Disadvantages

\- Risk of race condition if threads share data.

\- No control over execution order.



\--------------------------------------------------------------------------------------------------------------------------------------------------



File Name: MyThreadClass\_lock.py



\## Description

Multithreading allows a program to run multiple tasks concurrently while locks are used to manage access to the critical section.

This program demonstrates \*\*thread synchronization using a Lock\*\* to ensure that only one thread executes a critical section (printing messages and sleeping) at a time, preventing overlapping outputs and race condition.



\## How and When to Execute

Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)

Execute this program when you want to observe and control access to shared resources among multiple threads.



\## What We Learned

\- The mechanism and working of locks.

\- How to use threading.Lock() to synchronize threads.

\- Observed how thread execution order is controlled by locks, even though threads are started concurrently.



\## Advantages

\- Access to critical section is only granted to 1 thread at a time preventing output conflicts and incorrect modifications.

\- Prevents race condition in critical section.



\## Disadvantages

\- Using locks for the entire task including sleep may lead to an increase in total execution time.

\- Locking adds overhead, especially for small tasks.



\--------------------------------------------------------------------------------------------------------------------------------------------------



File Name: MyThreadClass\_lock\_2.py



\## Description

Multithreading allows multiple tasks to run concurrently within a program.

This program demonstrates \*\*efficient use of locks\*\*, where only the critical section (printing) is protected, allowing the remaining part (sleep and execution) to run concurrently to improve performance and efficiency.



\## How and When To Execute

Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)

Execute this program when you want concurrent execution while still protecting operations like printing or shared resources.



\## What We Learned

\- How to use locks efficiently.

\- How threads can still run concurrently outside the locked section.

\- Each thread enters and exits the critical section only once in this scenario.



\## Advantages

\- Maintains readability while improving execution efficiency.

\- Allows better concurrency compared to full locking.



\## Disadvantages

\- Debugging concurrent execution can still be challenging

\- Locking adds overhead, especially for small tasks.

\- Since all threads go to sleep() at the same time, its possible that the "over" output appears in random order instead of the correct sequence.



\--------------------------------------------------------------------------------------------------------------------------------------------------



File Name: Rlock.py



\## Description

RLock is the type of lock which allows a thread to re-enter the critical section.

This program demonstrates the use of a Reentrant Lock (RLock) to safely manage a shared variable when multiple threads perform addition and removal operations.



\## How and When to Execute

Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)

Execute this when multiple threads need to modify shared data safely.



\## What We Learned

\- How multiple threads can share and modify a common resource.

\- How threads can run concurrently while maintaining data consistency.



\## Advantages

\- Ensures safe access to shared variables.

\- Demonstrates real-world shared resource handling.



\## Disadvantages

\- Requires careful design as any small changes can lead to logical errors.

\- Overuse of locks can reduce concurrency benefits.



\--------------------------------------------------------------------------------------------------------------------------------------------------



File Name: Semaphore.py



\## Description

A semaphore is a synchronization mechanism which uses a counter to allow a specified number of threads access to the shared resource while others wait till its available for access.

This program demonstrates the use of a \*\*Semaphore\*\* to synchronize a producer and a consumer, where the consumer waits until the producer generates an item before proceeding.



\## How and When to Execute

Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)

Execute this program in scenarios where tasks depend on resource availability.



\## What We Learned

\- How to use a Semaphore to control synchronization between threads.

\- Understanding the interaction of consumer and producer with one another.



\## Advantages

\- Useful for handling tasks where dependencies occur.

\- We can give shared resource to more than 1 thread at a time while ensuring consistency.



\## Disadvantages

\- If the threads utilizing the shared resource take too long, the remaining may spend a lot of time waiting which could reduce efficiency.

\- Due to code complexity, debugging may be difficult.



\--------------------------------------------------------------------------------------------------------------------------------------------------



File Name: Barrier.py



\## Description

A barrier us a synchronization tool used in multithreading where multiple threads move at their own pace and stop upon reaching a certain point, when all threads reach that point, from there they are released together to continue simultaneous execution.

This program demonstrates the use of a Barrier, where multiple threads wait for each other at a synchronization point before continuing.



\## How and When to Execute

Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)

Execute this program in scenarios like a race. It can also be used when threads need to wait for each other at any specified point.



\## What We Learned

\- How to use a Barrier to synchronize multiple threads at a common point.

\- When a thread calls wait() on a Barrier, it stalls at that point and stays in that state until all the other threads have assembled.



\## Advantages

\- Useful for coordinating staged tasks or phases in multithreading.

\- Simple and clean way to manage group coordination.



\## Disadvantages

\- Deadlock may occur if the number of threads reaching the barrier is fewer than expected.

\- Execution time depends on the slowest thread reaching the barrier.



\--------------------------------------------------------------------------------------------------------------------------------------------------



File Name: Condition.py



\## Description

This program demonstrates the consumer producer problem and how its solved using threading.condition.



\#How and When to Execute

Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)

Execute this program in scenarios like buffer management, task queues, or resource pool as you will be operating and processing upon conditions there.



\## What We Learned

\- How to use threading.condition() to control access to shared resources.

\- Threads can sleep and resume safely, maintaining data consistency.

\- notify() wakes up a waiting thread, ensuring proper coordination.



\## Advantages

\- Ensures safe access to shared resources between threads.

\- Prevents consumption when there is no produced item and prevents production if the specified production limit is reached.



\## Disadvantages

\- Improper use can lead to deadlocks if notify() is not called.

\- Performance may reduce due to frequent blocking and waking.



\--------------------------------------------------------------------------------------------------------------------------------------------------



File Name: Event.py



\## Description

threading.event is a synchronization tool that allows one or more threads to be notified when a specific condition or state is met.

This program demonstrates the consumer producer problem and how its solved using threading.event.



\## How and When to Execute

Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)

Execute this program when you want threads to give signals, such as notifying that data is ready.



\## What We Learned

\- How to use threading.event() to signal between threads.

\- The use of clear() to reset the event, wait() to block a thread and set() to notify that condition is met.

\- Enables asynchronous coordination without busy waiting.



\## Advantages

\- Avoids waiting when using wait(), which improves CPU efficiency.

\- Helps coordinate resource availability safely.

\- Provides simple signaling between threads.



\## Disdvantages

\- If due to any mistake or incorrect use set() is not called, we will reach a deadlock.

\- This is only suitable for event signaling, not general resource locking.



\--------------------------------------------------------------------------------------------------------------------------------------------------



File Name: Threading\_with\_queue.py



\## Description

Queue is a data structure which follows a FIFO (First-In First-Out) principle.

This program demonstrates the consumer producer problem and how its solved using a queue in python.



\## How and When to Execute

Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)

Execute this when you want safe communication and coordination between multiple threads producing and consuming shared data.



\## What We Learned

\- Using a queue avoids explicit locks or events for producer-consumer coordination.

\- Multiple threads can work concurrently without data corruption.

\- Using queue is a good option when practicing multithreading.



\## Advantages

\- Simplified code since no explicit locking mechanism is used.

\- Prevents race conditions on shared resources.

\- Supports multiple producers and consumers.



\## Disadvantages

\- Debugging multithreaded queue behavior can be difficult as code complexity increases.

\- Memory can grow if producers produce faster than consumers consume, which would reduce overall efficiency.

