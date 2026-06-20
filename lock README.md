Synchronization Lock

What we learned
Lock is used to protect shared resources and avoid race conditions.

Code Understanding
Two threads increment a shared counter.
Lock ensures only one thread updates counter at a time.

How to Execute
python lock_example.py

End Use
- Banking system
- Shared data
- Database operations

When to Use
When multiple threads access shared variables

How to Use
Create lock  
Acquire lock  
Execute critical section  
Release lock  

Advantages
- Prevent race condition
- Safe execution

Disadvantages
- Deadlock possibility
- Slower performance
