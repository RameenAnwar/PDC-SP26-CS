# Import the MPI module from mpi4py for parallel computing
from mpi4py import MPI

# Get the MPI communicator (includes all processes)
comm = MPI.COMM_WORLD
# Get the total number of processes in the communicator
size = comm.Get_size()
# Get the rank (ID) of the current process (0 to size-1)
rank = comm.Get_rank()
# Each process calculates its own value: square of (rank+1)
# Rank 0: 1^2 = 1, Rank 1: 2^2 = 4, Rank 2: 3^2 = 9, etc.
data = (rank + 1) ** 2

# Perform a gather operation:
# All processes send their 'data' to the root process (rank 0)
# The root process collects all values into a list
# Non-root processes receive a None/empty value after gather
data = comm.gather(data, root=0)

# Only the root process (rank 0) executes this block
if rank == 0:
    print("rank = %s " % rank + \
          "...receiving data from other processes")
    
    # Loop through all other processes (ranks 1 to size-1)
    for i in range(1, size):
        # Extract the value received from process i
        value = data[i]
        # Print which process sent what data to the root
        print(" process %s receiving %s from process %s" \
              % (rank, value, i))
   #What this code does:
   # Gather Operation:
   # Root process (rank 0) collects data from ALL processes
   # Each process sends its data value to the root
   # Root receives a list where data[i] contains the value from process i
   # Data values (for 4 processes):
   # Process 0: (0+1)² = 1
   # Process 1: (1+1)² = 4
   # Process 2: (2+1)² = 9
   # Process 3: (3+1)² = 16   
     
  #output
  #       