MPI Parallel Point-to-Point Communication:
A minimal Python script demonstrating multiple, independent point-to-point communication paths running concurrently using `send` and `recv` in the `mpi4py` library.

Prerequisites:
You need a system-level MPI implementation (like OpenMPI or MPICH) installed. Then, install the required Python package:

```bash
pip install mpi4py
```

How to Run:
Launch the script using an MPI executor. Because the code explicitly targets Process 8, you must run this with at least 9 processes (ranks 0 through 8).

Use the following command in your terminal:

```bash
mpiexec -n 9 python script_name.py
```

What it Does:
This script showcases two completely independent data transfers happening across different ranks simultaneously:
1. Path A (Integer Transfer):
* Process 0 sends an integer (`10000000`) directly to Process 4.
* Process 4 blocks until it receives the data from Process 0, then prints it.
2. Path B (String Transfer):
* Process 1 sends a string (`"hello"`) directly to Process 8.
* Process 8 blocks until it receives the data from Process 1, then prints it.
3. Idle Processes: Ranks 2, 3, 5, 6, and 7 do not participate in any communication but will still print their initialization rank line.

Example Output:
Running with 9 processes yields an output similar to the following:

text
my rank is :  0
my rank is :  1
my rank is :  2
my rank is :  3
my rank is :  5
my rank is :  6
my rank is :  7
my rank is :  4
my rank is :  8
sending data 10000000 to process 4
sending data hello :to process 8
data received is = 10000000
data1 received is = hello

Note: The console output sequence of the `my rank is : X` statements will vary on every run depending on how the operating system's CPU scheduler handles the parallel processes.
