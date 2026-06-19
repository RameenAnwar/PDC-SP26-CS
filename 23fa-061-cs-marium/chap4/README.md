README - Chapter 4: MPI (Message Passing Interface)
📌 Topics Covered in Chapter 4
1. Hello World MPI (helloworld_MPI.py)
What I Learned:
Basic MPI program structure
rank of each process
Running parallel processes
Key Idea:

Each process prints its own identity.

2. Broadcast (broadcast.py)
What I Learned:
One process sends data to all processes
bcast() function
Advantages:
Fast data sharing
Single source distribution
Disadvantages:
Only root controls data
3. Scatter (scatter.py)
What I Learned:
Splitting data among processes
Each process gets a part of array
Advantages:
Parallel data distribution
Efficient workload sharing
Disadvantages:
Fixed data size required
4. Gather (gather.py)
What I Learned:
Collecting data from all processes
Root process gathers results
Advantages:
Easy result collection
Useful for final output
5. Reduction (reduction.py)
What I Learned:
Combining data using operations (SUM, MAX, etc.)
Reduce() function
Advantages:
Efficient computation
Aggregates results quickly
Disadvantages:
Only root gets final result
6. Alltoall (alltoall.py)
What I Learned:
Every process sends data to every other process
Complete exchange pattern
Advantages:
Full data communication
Useful in complex algorithms
Disadvantages:
High communication cost
7. Point to Point Communication (pointToPointCommunication.py)
What I Learned:
Direct send/receive between processes
send() and recv()
Advantages:
Flexible communication
Controlled messaging
Disadvantages:
Can cause deadlocks if not careful
8. Deadlock Problems (deadLockProblems.py)
What I Learned:
What causes deadlocks in MPI
Blocking communication issues
Key Idea:

Improper send/recv order can freeze program.

9. Virtual Topology (virtualTopology.py)
What I Learned:
Creating grid/Cartesian topology
Using Create_cart()
Finding neighbors using Shift()