from mpi4py import MPI  # Imports the MPI library to allow communication between multiple processes

comm = MPI.COMM_WORLD  # Sets up the group that connects all processes together
size = comm.Get_size()  # Finds out how many total processes are running in the system
rank = comm.Get_rank()  # Gives each process its own unique ID number (starting from 0)
data = (rank+1)**2  # Each process calculates its own data (rank + 1 squared)



# The 'Gather' command collects the 'data' from every process and sends it all to the Root (rank 0)
data = comm.gather(data, root=0) 

if rank == 0:  # This part only runs on the Root process (rank 0)
   print ("rank = %s " %rank +\
          "...receiving data to other process") # Prints a message saying it's receiving data
   
   for i in range(1,size):  # Loops through the list of data collected from all other processes

      value = data[i]  # Picks out the specific value that came from process 'i'
      print(" process %s receiving %s from process %s"\
            %(rank , value , i)) # Prints which process sent which value to the Root