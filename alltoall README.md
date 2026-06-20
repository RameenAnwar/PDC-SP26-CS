MPI All-to-All Example
A minimal Python script demonstrating the `Alltoall` collective communication operation using `mpi4py` and `numpy`.

Prerequisites
You need a system-level MPI implementation (like OpenMPI) installed. Then, install the required Python packages:

'''
pip install numpy mpi4py
'''

How to Run

Launch the script using an MPI executor. To run with 4 processes, use:

'''
mpiexec -n 4 python script_name.py
'''

(Replace `script_name.py` with your actual filename).

What it Does

1. Each process generates a NumPy array (`senddata`) where the values are multiplied by `rank + 1`.
2. Using `comm.Alltoall()`, the processes distribute their arrays so that **Process `i**` sends its **`j`-th** element to **Process `j**`.
3. The result is stored in `recvdata` for each process.

Example Output
Running with 3 processes (`mpiexec -n 3 python script_name.py`) yields:


 process 0 sending [0 1 2] receiving [0 0 0]
 process 1 sending [0 2 4] receiving [1 2 3]
 process 2 sending [0 3 6] receiving [2 4 6]
