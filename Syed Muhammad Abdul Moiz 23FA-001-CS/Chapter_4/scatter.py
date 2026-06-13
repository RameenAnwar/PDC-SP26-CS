from mpi4py import MPI  # Imports the MPI library to allow communication between parallel processes

comm = MPI.COMM_WORLD  # Sets up the group containing all the processes in the program
rank = comm.Get_rank()  # Assigns a unique ID number (starting from 0) to every process

if rank == 0:  # This block only runs on the "Root" process
    # The Root process creates a list of data that it wants to split up and share
    array_to_share = [1, 2, 3, 4 ,5 ,6 ,7, 8 ,9 ,10] 
           
else:  # This runs on all other processes
    # Non-root processes start with nothing in their shared variable
    array_to_share = None



# The 'scatter' command takes the list from the Root and divides it into equal pieces
# Each process (including the Root) receives one piece from the list into its 'recvbuf'
recvbuf = comm.scatter(array_to_share, root=0)

# Every process prints its rank and the specific piece of data it received from the Root
print("process = %d" % rank + " variable shared  = %d " % recvbuf )