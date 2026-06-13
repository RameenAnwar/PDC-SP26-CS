# Chapter 04 – Message Passing Interface (MPI)

## 1) helloworld_MPI.py
This file is the simplest MPI program, demonstrating how multiple processes are launched and identified using MPI.

- **MPI (Message Passing Interface)**: A standard for parallel programming where multiple processes run and communicate across cores or machines.
- `MPI.COMM_WORLD`: The default communicator that includes all running processes.
- `comm.Get_rank()` returns the unique ID (rank) of each process.
- Every process runs the same code but prints its own rank, showing they are all independent.
- This is the "Hello World" of parallel programming with MPI.

**Advantages:**
- Best starting point to understand MPI and how processes are launched.
- Shows that all processes run the same code independently.

**Disadvantages:**
- No actual communication between processes.
- No practical use beyond learning purposes.

**Time behavior:**
- All processes run simultaneously, so execution is nearly instant.


## 2) pointToPointCommunication.py
This file demonstrates direct one-to-one communication between specific processes using `send()` and `recv()`.

- **Point-to-Point Communication**: A specific process sends data directly to another specific process.
- `comm.send(data, dest=destination_process)` sends data to a target rank.
- `comm.recv(source=source_process)` blocks until it receives data from the specified rank.
- Process 0 sends an integer to process 4; process 1 sends a string to process 8.
- Processes 4 and 8 receive and print their respective data.
- Each process only executes the `if` block matching its rank.

**Advantages:**
- Precise control over which processes communicate with each other.
- Simple model for direct data transfer between processes.

**Disadvantages:**
- Doesn't scale well when many processes need to communicate.
- Requires careful matching of send and recv to avoid hangs.
- Blocking calls mean processes wait until communication completes.

**Time behavior:**
- Time depends on how long send/recv takes between processes.
- Processes not involved in communication finish instantly.


## 3) broadcast.py
This file demonstrates broadcasting, where one process sends the same data to all other processes at once.

- **Broadcast**: One process (root) sends a single value to every process in the communicator.
- Process 0 sets `variable_to_share = 100`; all others set it to `None`.
- `comm.bcast(variable_to_share, root=0)` sends the value from process 0 to everyone.
- After the broadcast, every process has the same value regardless of what it started with.
- All processes then print the received value to confirm.

**Advantages:**
- Efficient way to share data with all processes at once.
- Simpler than sending individually to each process.
- Built-in MPI optimization for large-scale broadcasting.

**Disadvantages:**
- All processes receive the same data — no customization per process.
- Root process must have the data ready before others can proceed.

**Time behavior:**
- Very fast since MPI handles distribution internally.
- All processes receive data at roughly the same time.


## 4) scatter.py
This file demonstrates scattering, where data from one process is split and distributed to all processes.

- **Scatter**: Root process splits an array and sends one chunk to each process.
- Process 0 defines `array_to_share = [1, 2, ..., 10]`; others set it to `None`.
- `comm.scatter(array_to_share, root=0)` sends one element to each process based on rank.
- Each process receives its own unique value from the array.
- Every process prints its rank and the value it received.

**Advantages:**
- Distributes different data to each process efficiently.
- Great for parallel processing where each process handles its own chunk.
- Cleaner than manual point-to-point sends.

**Disadvantages:**
- Array size must match the number of processes exactly.
- Root process must prepare all data before scattering.

**Time behavior:**
- Fast distribution since MPI handles splitting internally.
- All processes receive their data at roughly the same time.


## 5) gather.py
This file demonstrates gathering, where all processes send their data back to one root process.

- **Gather**: Each process sends its data to the root, which collects everything into a list.
- Each process computes `(rank+1)**2` as its contribution.
- `comm.gather(data, root=0)` collects all values into a list at process 0.
- Process 0 then loops through the received list and prints each value with its source rank.
- This is the reverse operation of scatter.

**Advantages:**
- Efficient way to collect results from all processes into one place.
- Pairs naturally with scatter for a complete distribute-compute-collect pattern.

**Disadvantages:**
- Only root process gets the full data — others have no access.
- Root process becomes a bottleneck if gathering large amounts of data.

**Time behavior:**
- All processes compute simultaneously, then send to root at once.
- Faster than collecting results one by one using point-to-point.


## 6) alltoall.py
This file demonstrates all-to-all communication, where every process sends and receives data from every other process.

- **Alltoall**: Each process sends a unique chunk of data to every other process and receives one from each.
- `senddata = (rank+1) * numpy.arange(size)` creates different data per process.
- `comm.Alltoall(senddata, recvdata)` performs the full exchange simultaneously.
- Each process ends up with data contributed by all other processes.
- Every process prints what it sent and what it received.

**Advantages:**
- Complete data exchange between all processes in one operation.
- Useful for matrix transposition and data redistribution in parallel algorithms.
- More efficient than doing individual point-to-point sends.

**Disadvantages:**
- Communication volume grows with number of processes (can be expensive).
- Requires all processes to be ready simultaneously.

**Time behavior:**
- All exchanges happen at the same time, so time is relatively short.
- Performance scales with number of processes and data size.


## 7) reduction.py
This file demonstrates reduction, where data from all processes is combined into a single result at the root using an operation.

- **Reduce**: Applies an operation (like SUM) across all processes and stores the result at root.
- Each process creates `senddata = (rank+1) * numpy.arange(10)`.
- `comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)` sums arrays from all processes.
- Only process 0 gets the final summed result; others get zeros in `recvdata`.
- Every process prints its sent data and its local `recvdata` after the operation.

**Advantages:**
- Efficient way to aggregate results from all processes.
- MPI handles the combining operation internally and optimally.
- Supports multiple operations: SUM, MAX, MIN, PROD, etc.

**Disadvantages:**
- Only root process gets the final result.
- Non-root processes have no access to the aggregated data without a broadcast.

**Time behavior:**
- All processes send simultaneously, reduction is very fast.
- Time depends on array size and number of processes.


## 8) deadLockProblems.py
This file demonstrates a deadlock situation in MPI, where two processes wait on each other and neither can proceed.

- **Deadlock**: A situation where two or more processes are each waiting for the other, causing both to hang forever.
- Process 1 calls `recv()` first, then `send()`.
- Process 5 calls `send()` first, then `recv()`.
- Because process 1 is waiting to receive before it sends, and process 5 sends first, they end up blocking each other.
- This code is intentionally broken to show what deadlock looks like in practice.

**Advantages:**
- Great learning example to understand why deadlock happens.
- Shows the importance of matching send/recv order carefully.

**Disadvantages:**
- Program will hang indefinitely if the deadlock is not resolved.
- Hard to debug in real applications with many processes.
- Fix requires reordering send/recv calls to be non-blocking or symmetric.

**Time behavior:**
- Program never finishes — it hangs due to the deadlock.


## 9) virtualTopology.py
This file demonstrates creating a virtual Cartesian grid topology for organizing MPI processes in a structured layout.

- **Virtual Topology**: Arranges processes into a logical structure (like a 2D grid) to simplify communication patterns.
- `comm.Create_cart()` creates a Cartesian communicator with a grid of rows and columns.
- Grid size is computed automatically based on total number of processes using `numpy.floor(numpy.sqrt(size))`.
- `periods=(True, True)` makes the grid wrap around (toroidal), so edges connect to the opposite side.
- Each process finds its row and column using `Get_coords()`.
- `cartesian_communicator.Shift()` identifies UP, DOWN, LEFT, RIGHT neighbors for each process.
- Every process prints its position and its four neighbors.

**Advantages:**
- Simplifies communication in grid-based parallel algorithms (like image processing, simulations).
- Shift() automatically handles boundary wrapping.
- Makes neighbor communication clean and structured.

**Disadvantages:**
- More complex setup than basic MPI communication.
- Grid size depends on number of processes — not always a perfect fit.
- Requires understanding of Cartesian coordinates in parallel context.

**Time behavior:**
- Setup time is minimal; all processes compute their positions simultaneously.
- Communication pattern efficiency depends on grid size and process count.