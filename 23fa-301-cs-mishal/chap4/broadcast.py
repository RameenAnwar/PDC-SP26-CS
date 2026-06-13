# Import the MPI module from mpi4py for parallel computing
from mpi4py import MPI

# Get the MPI communicator (includes all processes)
comm = MPI.COMM_WORLD
# Get the rank (ID) of the current process (0 to size-1)
rank = comm.Get_rank()

# Only process with rank 0 (the root process) initializes the variable
if rank == 0:
   variable_to_share = 100   # Root process sets the value to broadcast
else:
   # All other processes initialize the variable as None (will receive from root)
   variable_to_share = None

# Perform a broadcast operation:
# The root process (rank 0) sends its 'variable_to_share' value to all other processes
# After this call, every process will have the same value (100) in 'variable_to_share'
variable_to_share = comm.bcast(variable_to_share, root=0)

# Print the process rank and the value it now has (should be 100 for all processes)
print("process = %d" % rank + " variable shared  = %d " % variable_to_share)


#What this code does:
# Broadcast: One process (root=0) sends the same data to all other processes
# Root process (rank 0): Creates the value 100 and broadcasts it
# Other processes (ranks 1, 2, ...): Start with None but receive the value 100 from the root
# Result: Every process ends up with variable_to_share = 100

#output
# process = 0 variable shared  = 100 
# process = 2 variable shared  = 100 
# process = 1 variable shared  = 100 