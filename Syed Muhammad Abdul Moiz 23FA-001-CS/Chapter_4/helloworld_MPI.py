#hello.py
from mpi4py import MPI  # Imports the MPI library so the script can run on multiple CPU cores at once

comm = MPI.COMM_WORLD  # Connects all the running processes into one communication group
rank = comm.Get_rank()  # Asks each process for its unique ID number (rank) so it can identify itself



print ("hello world from process ", rank)  # Prints a message showing that this specific process is active and running