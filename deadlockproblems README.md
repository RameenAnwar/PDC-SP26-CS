MPI Point-to-Point Communication
A minimal Python script demonstrating basic two-way, point-to-point communication using `send` and `recv` in the `mpi4py` library.

Prerequisites:
You need a system-level MPI implementation (like OpenMPI or MPICH) installed. Then, install the required Python package:
```bash
pip install mpi4py

```

How to Run:
Launch the script using an MPI executor. Since the code explicitly requires Process 1 and Process 5 to communicate, you must run this with at least 6 processes (ranks 0 through 5).

Use the following command in your terminal:
```bash
mpiexec -n 6 python script_name.py
```

(Replace 'script_name.py' with your actual filename).

What it Does:
This script highlights targeted communication between two specific processes while the others remain idle:

1. Rank Check: Every process prints its rank upon starting.
2. Process 5 (The Initiator): Sends the string "b" to Process 1 using `comm.send()`.
Waits to receive data back from Process 1 using `comm.recv()`.


3. Process 1 (The Responder): First, waits to receive data from Process 5.
After receiving, it sends the string "a" back to Process 5.

Note on Deadlocks: The order of operations is critical here. Because Process 5 sends first and Process 1 receives first, the code runs smoothly. If both processes tried to receive first, the program would freeze (deadlock) waiting for each other.

Example Output:
Running with 6 processes yields output similar to this:

text
my rank is 0
my rank is 2
my rank is 3
my rank is 4
my rank is 1
my rank is 5
sending data b :to process 1
data received is = a
sending data a to process 5
data received is = b
```

*(Note: The exact order of the "my rank is..." lines may vary depending on how your OS schedules the parallel processes, but the send/receive logs will execute once the data is exchanged).*
