# Import MPI for parallel processing
from mpi4py import MPI

# Get the communicator (allows processes to communicate)
comm = MPI.COMM_WORLD

# Get this process's ID (0, 1, 2, ...)
rank = comm.Get_rank()

# Only process 0 (the root) creates the variable with value 100
if rank == 0:
   variable_to_share = 100 
           
# All other processes set it to None (empty)
else:
   variable_to_share = None

# BROADCAST: Process 0 sends its variable to ALL other processes
# Every process receives the value (100) from process 0
variable_to_share = comm.bcast(variable_to_share, root=0)

# Print what each process has after broadcast
print("process = %d" %rank + " variable shared  = %d " %variable_to_share)
#output
# process = 0 variable shared  = 100 
# process = 2 variable shared  = 100 
# process = 1 variable shared  = 100 
