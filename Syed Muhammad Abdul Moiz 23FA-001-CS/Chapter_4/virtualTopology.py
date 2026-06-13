from mpi4py import MPI  # Imports the MPI library for parallel computing
import numpy as np  # Imports NumPy to help with mathematical calculations

# Assigns simple numbers to represent directions for better code readability
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
neighbour_processes = [0,0,0,0] # Creates a list to store the ID of neighbors in each direction

if __name__ == "__main__":
    comm = MPI.COMM_WORLD  # Sets up the group for all running processes
    rank = comm.rank  # Gets the unique ID of the current process
    size = comm.size  # Gets the total number of processes available

    # Calculates the number of rows and columns needed to arrange processes in a square-like grid
    grid_row = int(np.floor(np.sqrt(comm.size)))
    grid_column = comm.size // grid_row

    # Adjusts the grid dimensions to make sure they fit within the total number of processes
    if grid_row*grid_column > size:
        grid_column -= 1
    if grid_row*grid_column > size:
        grid_row -= 1

    if (rank == 0) : # Only the first process prints the grid setup info
        print("Building a %d x %d grid topology:"\
              % (grid_row, grid_column) )

    

    # Creates a "Cartesian Communicator" which arranges the processes into a logical grid map
    # periods=(True, True) means the grid edges wrap around (like a donut shape)
    cartesian_communicator = \
                           comm.Create_cart( \
                               (grid_row, grid_column), \
                               periods=(True, True), reorder=True)
                               
    # Finds the specific X and Y coordinates (row and column) of the current process in the grid
    my_mpi_row, my_mpi_col = \
                cartesian_communicator.Get_coords\
                ( cartesian_communicator.rank ) 

    # Finds the neighbor IDs in the vertical direction (Up and Down)
    neighbour_processes[UP], neighbour_processes[DOWN]\
                               = cartesian_communicator.Shift(0, 1)
    
    # Finds the neighbor IDs in the horizontal direction (Left and Right)
    neighbour_processes[LEFT],  \
                               neighbour_processes[RIGHT]  = \
                               cartesian_communicator.Shift(1, 1)

    # Prints the process ID, its grid position, and the IDs of all its direct neighbors
    print ("Process = %s \
row = %s \
column = %s \n----> \nneighbour_processes[UP] = %s\n\
neighbour_processes[DOWN] = %s\n\
neighbour_processes[LEFT] =%s\nneighbour_processes[RIGHT]=%s\n" \
           %(rank, my_mpi_row, \
             my_mpi_col,neighbour_processes[UP], \
             neighbour_processes[DOWN], \
             neighbour_processes[LEFT] , \
             neighbour_processes[RIGHT]))