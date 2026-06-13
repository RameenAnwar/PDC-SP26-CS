from mpi4py import MPI  # Imports the MPI library to enable parallel communication between processes

comm = MPI.COMM_WORLD  # Creates the main group that connects all processes together
rank = comm.Get_rank()  # Gives each process its own unique ID number (rank) to identify it

if rank == 0:  # Checks if this is the "Root" process (usually the boss process)
    variable_to_share = 100  # The Root process sets the value that it wants to send to everyone else
            
else:  # This part runs for every other process that is not the Root
    variable_to_share = None  # These processes start with nothing until the Root sends the data



# The Root process sends the data to all other processes in the group
variable_to_share = comm.bcast(variable_to_share, root=0) 

# Every process prints its rank and the shared value to prove it received the data
print("process = %d" %rank + " variable shared  = %d " %variable_to_share)