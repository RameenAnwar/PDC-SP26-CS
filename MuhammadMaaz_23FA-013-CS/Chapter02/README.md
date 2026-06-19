Chapter 02 Summary

1. Barrier.py
What I studied: I studied Barrier in threading which is used to make threads wait until all threads reach a certain point.
How I executed: I created multiple threads and used a Barrier so all threads wait at the same point before continuing.
End uses: Used in synchronization tasks where multiple threads must complete a step before moving forward together.
Advantages: It makes sure proper synchronization is done, easy to manage multiple threads, avoids early execution.
Disadvantages: Can cause deadlock if threads don’t reach barrier.

2. Condition.py
What I studied: I studied Condition variables for communication between threads (producer-consumer problem).
How I executed: I created and ran producer and consumer threads using condition.wait() and condition.notify() to control execution.
End uses: Used in real-time systems like task queues, resource sharing, and producer-consumer scenarios.
Advantages: Efficient thread communication. It also avoids busy waiting and gives good control over shared resources.
Disadvantages: Complex to understand, risk of deadlock, requires careful handling.

3. Event.py
What I studied: I studied Event objects, they are used for signaling between threads.
How I executed: I created Producer and Consumer threads where producer sets event and consumer waits for event before executing.
End uses: Used for signaling events like notifications, triggers, and synchronization between threads.
Advantages: Simple to use, good for signaling and avoids constant checking.
Disadvantages: Can miss signals if not handled properly. They are not suitable for complex synchronization.

4. MyThreadClass.py
What I studied: I studied basic thread creation using classes in Python.
How I executed: I created and ran multiple threads using a custom class and executed them using start() and join().
End uses: Used for running multiple tasks concurrently like background jobs or parallel operations.
Advantages: Simple and easy to implement and improves performance with concurrency.
Disadvantages: No control over shared resources, can cause race conditions.

5. MyThreadClass_Lock.py
What I studied: I studied use of Lock to control access to shared resources in threads.
How I executed: I used threading.Lock() and applied acquire() and release() so that only one thread runs in critical section at a time.
End uses: It is used in situations where multiple threads access shared data like databases or files.
Advantages: It prevents race conditions, ensures data consistency and improves safety.
Disadvantages: Can slow down performance, risk of deadlock if lock not released properly.

6. Rlock.py
What I studied: I studied Reentrant Lock (RLock), which allows the same thread to acquire the same lock multiple times without causing a deadlock. It is useful when a function calls another function that also uses the same lock.
How I executed: I created a Box class with add and remove methods and used RLock, and ran two threads (adder and remover) that modify the shared data.
End uses: It is used in complex programs where the same thread needs to safely access shared resources multiple times.
Advantages: It prevents self-deadlock and it is safe for nested locking.
Disadvantages: Slower than normal Lock, harder to understand.

7. Semaphore.py
What I studied: I studied Semaphore, which controls access to a shared resource by limiting the number of threads that can access it at a time.
How I executed: I created and ran producer and consumer functions where the producer releases the semaphore and the consumer waits using the acquire() function.
End uses: Used in resource management like database connections, thread pools and limiting access to critical sections.
Advantages: Controls resource usage, prevents overaccess. It is useful in multithreaded environments.
Disadvantages: Can be confusing, improper use may lead to deadlocks or starvation.

8. ThreadDefinition.py
What I studied: I studied basic thread creation using functions and passing arguments to threads.
How I executed: I created multiple threads using threading.Thread and passed a function with arguments to the threads.
End uses: Used for simple parallel tasks like running multiple functions at the same time.
Advantages: Easy to implement, simple syntax, good for beginners.
Disadvantages: Limited control.

9. Thread_Determine.py
What I studied: I studied how to identify threads using names and track their execution using currentThread().
How I executed: I created three threads and printed when each thread starts and exits.
End uses: Useful for debugging, logging, and tracking thread execution in multi-threaded programs.
Advantages: Helps in understanding thread behavior, improves debugging and monitoring.
Disadvantages: Only used for identification and logging.

10. Thread_name_and_processes.py
What I studied: I studied assigning names to threads and understanding how thread works.
How I executed: I created threads using a class and printed their names during execution.
End uses: Used for identifying threads in logs and debugging multi-threaded applications.
Advantages: Simple implementation, helps in tracking threads.
Disadvantages: Limited functionality

11. Threading_with_queue.py
What I studied: I studied thread synchronization using Queue. It is a data structure for sharing data between threads. It automatically handles locking.
How I executed: I created Producer and Consumer threads where producer adds items to queue and consumers remove them using get() and task_done().
End uses: Used in task scheduling systems, job queues, producer-consumer problems.
Advantages: Safe for threads and there is no need for manual locks. Efficient communication between threads.
Disadvantages: Infinite loops in consumers can cause issues so it needs proper termination.