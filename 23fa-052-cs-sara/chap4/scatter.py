# Import MPI for parallel processing
from mpi4py import MPI

# Get the communicator
comm = MPI.COMM_WORLD

# Get this process's ID (0, 1, 2, ...)
rank = comm.Get_rank()

# Only process 0 (root) has the complete array
if rank == 0:
   array_to_share = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
           
# All other processes start with None
else:
   array_to_share = None

# SCATTER: Process 0 distributes array elements to ALL processes
# Each process gets ONE element from the array
recvbuf = comm.scatter(array_to_share, root=0)

# Print what each process received
print("process = %d" % rank + " variable shared = %d " % recvbuf)
#output:
process = 0 variable shared = 1 
process = 1 variable shared = 2 
process = 2 variable shared = 3 
process = 3 variable shared = 4 
process = 4 variable shared = 5 
process = 5 variable shared = 6 
process = 6 variable shared = 7 
process = 7 variable shared = 8 
process = 8 variable shared = 9 
process = 9 variable shared = 10 