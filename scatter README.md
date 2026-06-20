MPI Scatter Example:
A minimal Python script demonstrating the `scatter` collective communication operation using the `mpi4py` library.

Prerequisites:
You need a system-level MPI implementation (like OpenMPI or MPICH) installed. Then, install the required Python package:

```bash
pip install mpi4py

```

How to Run:
Launch the script using an MPI executor.
Important Note: Because this script uses `mpi4py`'s lowercase `scatter` method, the size of the array being scattered must exactly match the number of processes running. Since the array `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]` has 10 elements, you must run this script with exactly 10 processes.

Use the following command in your terminal:

```bash
mpiexec -n 10 python script_name.py

```

What it Does:
This script demonstrates one-to-many communication, where a single data structure on the root process is divided up and distributed across all available processes:
1. Initialization: The root process (Process `0`) initializes a list of 10 integers. All other processes initialize their variable to `None`.
2. The Scatter Operation: `comm.scatter(array_to_share, root=0)` takes the list from the root process, splits it apart, and sends one specific element to each process based on its rank.
* Process 0 gets the 0th element (`1`).
* Process 1 gets the 1st element (`2`).
* Process 9 gets the 9th element (`10`).
3. Result: Every process stores its individually assigned piece of the original array into the `recvbuf` variable and prints it.

Example Output:
Running with 10 processes yields an output similar to the following:

text
process = 0 variable shared  = 1 
process = 1 variable shared  = 2 
process = 2 variable shared  = 3 
process = 3 variable shared  = 4 
process = 4 variable shared  = 5 
process = 5 variable shared  = 6 
process = 6 variable shared  = 7 
process = 7 variable shared  = 8 
process = 8 variable shared  = 9 
process = 9 variable shared  = 10 

(Note: The exact print order in your terminal may vary depending on how the OS schedules the parallel processes, but the assigned numbers will always match the rank).*
