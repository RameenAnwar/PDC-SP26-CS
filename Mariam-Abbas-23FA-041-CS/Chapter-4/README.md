# Chapter # 4

---

## 1. alltoall.py

### Description:
Demonstrates MPI Alltoall collective operation where every process sends data to every other process simultaneously. Each process both sends and receives data from all others.

### How it Works:
- Each process creates a senddata array based on its rank
- `comm.Alltoall(senddata, recvdata)` exchanges data between all processes
- Every process sends a unique chunk to every other process
- Each process prints what it sent and what it received

### Result:
Every process prints its rank, the data it sent, and the data it received from all other processes.

### Advantages:
- Efficient all-to-all communication in one call
- No need to manually send/receive between each pair of processes

### Disadvantages:
- High communication overhead when number of processes is large
- All processes must participate simultaneously

### Where to Use:
- Matrix transposition in parallel computing
- Distributed data redistribution across all processes

---

## 2. broadcast.py

### Description:
Demonstrates MPI broadcast where process 0 (root) sends a single value to all other processes in the communicator simultaneously.

### How it Works:
- Process 0 sets `variable_to_share = 100`, all others set it to None
- `comm.bcast(variable_to_share, root=0)` broadcasts from process 0
- All processes receive the same value after broadcast
- Each process prints its rank and the received value

### Result:
All processes print the same value 100 regardless of their rank.

### Advantages:
- Single call distributes data to all processes efficiently
- Simple to implement for sharing common data

### Disadvantages:
- Only one process (root) sends — others cannot contribute data
- Wasteful if only few processes need the data

### Where to Use:
- Sharing configuration or parameters to all worker processes
- Distributing initial data at the start of parallel computation

---

## 3. deadLockProblems.py

### Description:
Demonstrates a deadlock scenario in MPI where two processes wait for each other to receive before sending, causing both to block indefinitely.

### How it Works:
- Process 1 calls `recv()` first then `send()` — waits for process 5
- Process 5 calls `send()` first then `recv()` — sends to process 1
- Process 1 is blocked waiting to receive while process 5 tries to send
- This mismatch in send/recv order causes deadlock

### Result:
Process 5 sends successfully but process 1 is stuck waiting — program hangs or produces incomplete output.

### Advantages:
- Clearly demonstrates what deadlock looks like in MPI
- Helps understand importance of correct send/recv ordering

### Disadvantages:
- Program hangs indefinitely if deadlock occurs
- Difficult to debug in large parallel programs

### Where to Use:
- Learning and understanding deadlock conditions
- Testing deadlock detection and prevention strategies

---

## 4. gather.py

### Description:
Demonstrates MPI gather operation where all processes send their data to root process (rank 0) which collects everything into a single list.

### How it Works:
- Each process computes `(rank+1)**2` as its data
- `comm.gather(data, root=0)` sends all values to process 0
- Only process 0 receives the complete gathered list
- Process 0 prints each received value with its source process rank

### Result:
Process 0 prints the squared values received from all other processes (1, 4, 9, 16...).

### Advantages:
- Simple way to collect results from all processes into one place
- Only root process handles the collected data

### Disadvantages:
- Root process can become a bottleneck with many processes
- Other processes cannot access the gathered data

### Where to Use:
- Collecting results from parallel computations
- Aggregating data from worker processes to a master process

---

## 5. helloworld_MPI.py

### Description:
Basic MPI hello world program — the starting point for learning MPI. Each process prints its rank to show parallel execution.

### How it Works:
- `MPI.COMM_WORLD` gives access to all processes
- `comm.Get_rank()` returns unique ID of each process
- Every process independently prints its rank
- Output order may vary since all run in parallel

### Result:
Each process prints "hello world from process N" where N is its rank number.

### Advantages:
- Simplest possible MPI program — easy to understand
- Confirms MPI is working correctly with multiple processes

### Disadvantages:
- Output order is not guaranteed — varies each run
- Does no real computation — only for learning purposes

### Where to Use:
- First program to verify MPI installation and setup
- Learning basic MPI concepts like rank and communicator

---

## 6. pointToPointCommunication.py

### Description:
Demonstrates MPI point-to-point communication where specific processes send data directly to specific other processes using send() and recv().

### How it Works:
- Process 0 sends integer 10000000 to process 4
- Process 1 sends string "hello" to process 8
- Process 4 receives from process 0 and prints it
- Process 8 receives from process 1 and prints it

### Result:
Process 4 prints the integer received from process 0. Process 8 prints the string received from process 1.

### Advantages:
- Direct communication between specific processes
- Can send any Python object — integers, strings, etc.

### Disadvantages:
- Must have matching send/recv pairs — mismatch causes deadlock
- Not efficient for broadcasting to all processes

### Where to Use:
- Sending task results between specific worker processes
- Any scenario requiring direct process-to-process communication

---

## 7. reduction.py

### Description:
Demonstrates MPI Reduce operation which collects data from all processes and applies an operation (SUM) to combine them into a single result at root process.

### How it Works:
- Each process creates a senddata array based on its rank
- `comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)` sums all arrays
- Only process 0 (root) gets the final summed result
- All processes print their sent data and received data after reduce

### Result:
Process 0 receives the element-wise sum of arrays from all processes. Other processes receive zeros in recvdata.

### Advantages:
- Combines data from all processes in one efficient call
- Supports multiple operations — SUM, MAX, MIN, PROD etc.

### Disadvantages:
- Only root process gets the final result
- All processes must have same array size

### Where to Use:
- Computing global sum, max, or min across all processes
- Aggregating results in scientific simulations

---

## 8. scatter.py

### Description:
Demonstrates MPI scatter where root process (rank 0) splits an array and sends one chunk to each process — opposite of gather.

### How it Works:
- Process 0 creates array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
- `comm.scatter(array_to_share, root=0)` splits and sends one element to each process
- Each process receives its own unique element
- Every process prints its rank and the value it received

### Result:
Each process prints its rank and its assigned value from the array (process 0 gets 1, process 1 gets 2, etc.).

### Advantages:
- Efficiently distributes different data to each process in one call
- Simple way to divide work among processes

### Disadvantages:
- Array size must match number of processes exactly
- Only root process has the original complete data

### Where to Use:
- Distributing dataset chunks to worker processes
- Dividing large arrays for parallel processing

---

## 9. virtualTopology.py

### Description:
Demonstrates MPI virtual Cartesian topology — arranges processes in a 2D grid and identifies each process's neighbors (UP, DOWN, LEFT, RIGHT).

### How it Works:
- Processes arranged in a 2D grid using `comm.Create_cart()`
- Grid size calculated based on total number of processes
- `Get_coords()` returns row and column of each process in grid
- `Shift()` finds neighboring process ranks in each direction
- `periods=(True, True)` makes grid wrap-around like a torus

### Result:
Each process prints its rank, grid position (row, column), and the ranks of its four neighbors.

### Advantages:
- Simplifies neighbor communication in grid-based problems
- Wrap-around topology avoids boundary condition issues

### Disadvantages:
- Grid size depends on number of processes — not always a perfect square
- More complex setup than simple linear communication

### Where to Use:
- Image processing and stencil computations on grids
- Parallel simulations like weather modeling or fluid dynamics

---