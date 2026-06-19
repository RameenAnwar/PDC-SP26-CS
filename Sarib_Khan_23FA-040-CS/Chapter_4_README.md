# Chapter 4 – MPI Communication in Parallel Computing

In this chapter, I learned different communication methods in MPI (Message Passing Interface). I also learned broadcasting, gathering, scattering, reduction operations, and communication between processes in distributed systems.

---

## Topic: helloworld_MPI.py


What I Learned
I learned the basic structure of MPI programs and how processes run in parallel.

How to Execute
mpiexec -n 4 python helloworld_MPI.py

Use / Output
Displays messages from multiple MPI processes.

When to Use
When starting MPI-based distributed programs.

Advantages
Simple introduction to MPI
Easy to understand

Disadvantages
Very basic example

Summary
This program introduces MPI execution with multiple processes.

---

## Topic: pointToPointCommunication.py


What I Learned
I learned how one process sends data directly to another process.

How to Execute
mpiexec -n 4 python pointToPointCommunication.py

Use / Output
Transfers messages between processes.

When to Use
When direct communication is needed.

Advantages
Simple communication
Easy control

Disadvantages
Not efficient for large systems

Summary
Point-to-point communication allows direct data transfer.

---

## Topic: broadcast.py


What I Learned
I learned how one process sends the same data to all processes.

How to Execute
mpiexec -n 4 python broadcast.py

Use / Output
Broadcasts data from one process to others.

When to Use
When same information is needed by all processes.

Advantages
Fast distribution
Easy synchronization

Disadvantages
All processes receive same data only

Summary
Broadcast sends common data to every process.

---

## Topic: scatter.py


What I Learned
I learned how data is divided and distributed among processes.

How to Execute
mpiexec -n 4 python scatter.py

Use / Output
Splits data into parts for different processes.

When to Use
When workload needs distribution.

Advantages
Efficient task division

Disadvantages
Needs equal distribution planning

Summary
Scatter divides data among processes.

---

## Topic: gather.py


What I Learned
I learned how data from multiple processes is collected into one process.

How to Execute
mpiexec -n 4 python gather.py

Use / Output
Collects results from all processes.

When to Use
When combining outputs is required.

Advantages
Easy result collection

Disadvantages
Main process can become overloaded

Summary
Gather combines results from multiple processes.

---

## Topic: reduction.py


What I Learned
I learned reduction operations like sum and maximum in MPI.

How to Execute
mpiexec -n 4 python reduction.py

Use / Output
Performs operations on distributed data.

When to Use
When calculating total results from processes.

Advantages
Efficient calculations

Disadvantages
Limited to specific operations

Summary
Reduction combines data using operations like sum.

---

## Topic: alltoall.py


What I Learned
I learned all-to-all communication where every process communicates with every other process.

How to Execute
mpiexec -n 4 python alltoall.py

Use / Output
Exchanges data between all processes.

When to Use
When all processes need shared communication.

Advantages
Flexible communication

Disadvantages
Can increase communication overhead

Summary
All-to-all communication exchanges data among all processes.

---

## Topic: virtualTopology.py


What I Learned
I learned how virtual topology organizes processes logically.

How to Execute
mpiexec -n 4 python virtualTopology.py

Use / Output
Creates communication structure between processes.

When to Use
When organizing process communication.

Advantages
Better management

Disadvantages
Complex for beginners

Summary
Virtual topology improves process organization.

---

## Topic: deadLockProblems.py


What I Learned
I learned how deadlocks occur in MPI communication.

How to Execute
mpiexec -n 4 python deadLockProblems.py

Use / Output
Shows processes waiting indefinitely.

When to Use
To understand communication issues.

Advantages
Improves debugging knowledge

Disadvantages
Can freeze execution

Summary
Deadlocks happen when processes wait on each other forever.

---

## Final Understanding

In this chapter, I learned MPI communication methods like point-to-point communication, broadcast, scatter, gather, and reduction. I also understood communication problems like deadlocks and how distributed systems exchange data between processes.