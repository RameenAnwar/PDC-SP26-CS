# Import the MPI module from mpi4py for parallel computing
from mpi4py import MPI

# Get the MPI communicator (includes all processes)
comm = MPI.COMM_WORLD
# Get the rank (ID) of the current process (0 to size-1)
rank = comm.Get_rank()

# Only process with rank 0 (the root process) initializes the full array
if rank == 0:
   # Array containing 10 elements to be distributed among all processes
   array_to_share = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
else:
   # All other processes initialize their variable as None 
   # (will receive a portion from the root)
   array_to_share = None

# Perform a scatter operation:
# The root process (rank 0) divides array_to_share into equal chunks
# Each process receives one chunk of the array
# IMPORTANT: The array is split into 'size' number of chunks
# Each process gets a chunk of length = len(array) / size
recvbuf = comm.scatter(array_to_share, root=0)

# Each process prints its rank and the chunk of data it received
# Note: %d expects an integer, but recvbuf might be a list/tuple
# This will cause an error if recvbuf is not a single integer
print("process = %d" % rank + " variable shared = %d " % recvbuf)


# What this code does:
# Scatter Operation: The root process distributes different pieces of its data to all processes.
#  Each process receives a distinct portion of the original array.

#output
