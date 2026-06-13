from mpi4py import MPI  # Imports the MPI library so processes can communicate with each other

comm=MPI.COMM_WORLD  # Sets up the global group for all running processes
rank = comm.rank  # Gets the unique ID number of the current process
print("my rank is %i" % (rank))  # Each process prints its own ID to the console

if rank==1:  # This block only executes for the process with ID number 1
    data_send= "a"  # Defines the message that process 1 wants to send
    destination_process = 5  # Sets the ID of the process that should receive the message
    source_process = 5  # Sets the ID of the process it expects to get a message from

    data_received=comm.recv(source=source_process)  # Process 1 waits to receive data from process 5 first
    comm.send(data_send,dest=destination_process)  # After receiving, process 1 sends its data to process 5
    
    print ("sending data %s " %data_send + \
           "to process %d" %destination_process)  # Prints a confirmation of the sent data
    print ("data received is = %s" %data_received)  # Prints the data it successfully got from process 5


     
if rank==5:  # This block only executes for the process with ID number 5
    data_send= "b"  # Defines the message that process 5 wants to send
    destination_process = 1  # Sets process 1 as the target for the message
    source_process = 1  # Sets process 1 as the source to get a message from

    comm.send(data_send,dest=destination_process)  # Process 5 sends its data to process 1 first
    data_received=comm.recv(source=source_process)  # After sending, process 5 waits to receive data from process 1
    
    print ("sending data %s :" %data_send + \
           "to process %d" %destination_process)  # Prints a confirmation of the sent data
    print ("data received is = %s" %data_received)  # Prints the data it successfully got from process 1