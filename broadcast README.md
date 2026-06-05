MPI Broadcast Example
A minimal Python script demonstrating the `bcast` (broadcast) collective communication operation using the `mpi4py` library.

Prerequisites
You need a system-level MPI implementation (like OpenMPI or MPICH) installed. Then, install the required Python package:

```bash
pip install mpi4py

```

How to Run
Launch the script using an MPI executor. To run with 4 processes, use the following command in your terminal:

```bash
mpiexec -n 4 python script_name.py

```

(Replace `script_name.py` with your actual filename).

What it Does
This script demonstrates one-to-all communication:

1. Initialization: The root process (Process `0`) sets `variable_to_share` to `100`. All other processes initialize it to `None`.
2. The Broadcast: The `comm.bcast(..., root=0)` function takes the value from the root process and copies it to every other process in the communicator.
3. Result: After the broadcast, every process holds the value `100`, regardless of their initial state.

Example Output:
Running with 4 processes (`mpiexec -n 4 python script_name.py`) yields:

process = 0 variable shared  = 100 
process = 1 variable shared  = 100 
process = 2 variable shared  = 100 
process = 3 variable shared  = 100 
```

Note: The exact print order may vary depending on how the OS schedules the parallel processes, but the shared variable will be `100` for all of them.
