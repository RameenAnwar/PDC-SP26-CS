    # Import MPI for parallel processing
from mpi4py import MPI

# Get the communicator
comm = MPI.COMM_WORLD

# Get total number of processes running
size = comm.Get_size()

# Get this process's ID (0, 1, 2, ...)
rank = comm.Get_rank()

# Each process calculates: (my_rank + 1) squared
# Rank 0: (0+1)^2 = 1
# Rank 1: (1+1)^2 = 4
# Rank 2: (2+1)^2 = 9
# Rank 3: (3+1)^2 = 16
data = (rank+1)**2

# GATHER: All processes send their data to process 0 (root)
# Process 0 collects all data into a list
data = comm.gather(data, root=0)

# ONLY process 0 (root) prints the received data
if rank == 0:
   print("rank = %s " %rank + \
         "...receiving data from other processes")
   
   # Loop through all other processes (1 to size-1)
   for i in range(1, size):
      # Get the value sent by process i
      value = data[i]
      
      # Print what was received and from whom
      print(" process %s receiving %s from process %s" \
            %(rank, value, i)
#output
rank = 0 ...receiving data from other processes
process 0 receiving 4 from process 1
process 0 receiving 9 from process 2
process 0 receiving 16 from process 3