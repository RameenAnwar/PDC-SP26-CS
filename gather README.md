MPI Gather Example:
A minimal Python script demonstrating the `gather` collective communication operation using the `mpi4py` library.

Prerequisites:
You need a system-level MPI implementation (like OpenMPI or MPICH) installed. Then, install the required Python package:

```bash
pip install mpi4py
```

How to Run
Launch the script using an MPI executor. To run with 4 processes, use the following command in your terminal:

```bash
mpiexec -n 4 python script_name.py

```

What it Does:
This script demonstrates many-to-one communication, where multiple processes send data to a single "root" process:

1. Local Computation: Each process computes a unique value based on its rank using the formula $(rank + 1)^2$.
* Process 0 computes $1^2 = 1$
* Process 1 computes $2^2 = 4$
* Process 2 computes $3^2 = 9$ (and so on...)
2. The Gather Operation: `comm.gather(data, root=0)` takes the individual values from all processes and consolidates them into a single list on the designated root process (Process 0). For all other processes, this function returns `None`.
3. Processing the Result: Process 0 checks the gathered list and iterates through it, printing the values it collected from the other processes (skipping its own value at index 0).

Example Output:
Running with 4 processes yields the following output from Process 0:
'''
rank = 0 ...receiving data to other process
 process 0 receiving 4 from process 1
 process 0 receiving 9 from process 2
 process 0 receiving 16 from process 3
'''
