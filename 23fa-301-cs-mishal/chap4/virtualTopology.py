# Import the MPI module from mpi4py for parallel computing
from mpi4py import MPI
# Import numpy for mathematical operations (sqrt, floor)
import numpy as np

# Define constants for direction indices
UP = 0      # Index for neighbor above (row - 1)
DOWN = 1    # Index for neighbor below (row + 1)
LEFT = 2    # Index for neighbor to the left (column - 1)
RIGHT = 3   # Index for neighbor to the right (column + 1)

# Initialize list to store neighbor ranks (will be filled later)
neighbour_processes = [0, 0, 0, 0]

# Standard Python guard to ensure code runs only when script is executed directly
if __name__ == "__main__":
    # Get the MPI communicator (includes all processes)
    comm = MPI.COMM_WORLD
    # Get the rank (ID) of the current process
    rank = comm.rank
    # Get the total number of processes
    size = comm.size

    # Calculate grid dimensions: try to make it as square as possible
    # grid_row = floor(sqrt(total_processes))
    grid_row = int(np.floor(np.sqrt(comm.size)))
    # grid_column = total_processes / grid_row
    grid_column = comm.size // grid_row

    # Adjust grid dimensions if the product exceeds total processes
    if grid_row * grid_column > size:
        grid_column -= 1
    if grid_row * grid_column > size:
        grid_row -= 1

    # Only root process (rank 0) prints the topology information
    if (rank == 0):
        print("Building a %d x %d grid topology:" \
              % (grid_row, grid_column))

    # Create a Cartesian (2D grid) virtual topology
    # Parameters:
    # - (grid_row, grid_column): dimensions of the grid
    # - periods=(True, True): wrap-around at edges (periodic boundary conditions)
    # - reorder=True: allow MPI to reorder ranks for optimal communication
    cartesian_communicator = \
        comm.Create_cart( \
            (grid_row, grid_column), \
            periods=(True, True), reorder=True)

    # Get the coordinates (row, column) of the current process in the Cartesian grid
    my_mpi_row, my_mpi_col = \
        cartesian_communicator.Get_coords \
        (cartesian_communicator.rank)

    # Determine neighbor ranks using Shift operations
    # Shift(direction, displacement): direction 0 = rows, direction 1 = columns
    # Shift(0, 1): get neighbors in row direction (UP and DOWN)
    neighbour_processes[UP], neighbour_processes[DOWN] = \
        cartesian_communicator.Shift(0, 1)

    # Shift(1, 1): get neighbors in column direction (LEFT and RIGHT)
    neighbour_processes[LEFT], neighbour_processes[RIGHT] = \
        cartesian_communicator.Shift(1, 1)

    # Print the rank, grid coordinates, and all neighbor ranks for each process
    print("Process = %s \
row = %s \
column = %s \n----> \nneighbour_processes[UP] = %s\n\
neighbour_processes[DOWN] = %s\n\
neighbour_processes[LEFT] = %s\nneighbour_processes[RIGHT] = %s\n" \
          % (rank, my_mpi_row, \
             my_mpi_col, neighbour_processes[UP], \
             neighbour_processes[DOWN], \
             neighbour_processes[LEFT], \
             neighbour_processes[RIGHT]))
    


# What this code does:
# Creates a 2D grid (Cartesian) topology for MPI processes, which is useful for:

# Matrix operations

# Image processing

# Finite difference methods

# Any problem with 2D data decomposition

#output
# Process = 1 row = 0 column = 1 
# ----> 
# neighbour_processes[UP] = 1
# neighbour_processes[DOWN] = 1
# neighbour_processes[LEFT] = 0
# neighbour_processes[RIGHT] = 2

# Building a 1 x 3 grid topology:
# Process = 0 row = 0 column = 0 
# ----> 
# neighbour_processes[UP] = 0
# neighbour_processes[DOWN] = 0
# neighbour_processes[LEFT] = 2
# neighbour_processes[RIGHT] = 1

# Process = 2 row = 0 column = 2 
# ----> 
# neighbour_processes[UP] = 2
# neighbour_processes[DOWN] = 2
# neighbour_processes[LEFT] = 1
# neighbour_processes[RIGHT] = 0
