from mpi4py import MPI  # Imports the MPI library to allow communication between separate processes

comm=MPI.COMM_WORLD  # Sets up the global group for all running processes to communicate
rank = comm.rank  # Gets the unique ID number of the current process
print("my rank is : " , rank)  # Each process identifies itself by printing its rank

if rank==0:  # This block only runs for process 0
    data= 10000000  # Sets a large integer as the message to send
    destination_process = 4  # Targets process 4 to receive this specific message
    comm.send(data,dest=destination_process)  # Sends the data directly to process 4
    print ("sending data %s " %data +\
           "to process %d" %destination_process)  # Prints a confirmation of the sent message
   
if rank==1:  # This block only runs for process 1
    destination_process = 8  # Targets process 8 to receive this specific message
    data= "hello"  # Sets a string as the message to send
    comm.send(data,dest=destination_process)  # Sends the string data directly to process 8
    print ("sending data %s :" %data + \
           "to process %d" %destination_process)  # Prints a confirmation of the sent message
   


if rank==4:  # This block only runs for process 4
    data=comm.recv(source=0)  # Process 4 waits to receive data specifically from process 0
    print ("data received is = %s" %data)  # Prints the data it successfully got from process 0
    
    
if rank==8:  # This block only runs for process 8
    data1=comm.recv(source=1)  # Process 8 waits to receive data specifically from process 1
    print ("data1 received is = %s" %data1)  # Prints the data it successfully got from process 1