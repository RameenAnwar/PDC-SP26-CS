# Import needed libraries
from mpi4py import MPI
import numpy as np

# Directions for neighbours (like North, South, West, East)
UP = 0      # North
DOWN = 1    # South  
LEFT = 2    # West
RIGHT = 3   # East

# List to store neighbour IDs (empty for now)
neighbour_processes = [0, 0, 0, 0]

# Main program
if __name__ == "__main__":
    # Setup MPI
    comm = MPI.COMM_WORLD
    rank = comm.rank          # My ID number
    size = comm.size          # Total processes

    # Make a grid from processes (like rows and columns)
    # Example: 9 processes → 3x3 grid
    grid_row = int(np.floor(np.sqrt(comm.size)))     # How many rows
    grid_column = comm.size // grid_row              # How many columns
    
    # Fix grid if it doesn't fit perfectly
    if grid_row * grid_column > size:
        grid_column -= 1
    if grid_row * grid_column > size:
        grid_row -= 1

    # Only boss (process 0) prints grid size
    if (rank == 0):
        print("Building a %d x %d grid topology:" % (grid_row, grid_column))

    # Create a 2D grid where processes can talk to neighbours
    # periods=True means edges connect (like a circle/donut)
    cartesian_communicator = comm.Create_cart(
        (grid_row, grid_column),     # Grid size
        periods=(True, True),         # Wrap around edges
        reorder=True                  # Let MPI rearrange for speed
    )

    # Find my position in the grid (which row and column)
    my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords(
        cartesian_communicator.rank
    )

    # Find my neighbours (who is above, below, left, right)
    # Shift(0,1) = move in row direction (up/down)
    neighbour_processes[UP], neighbour_processes[DOWN] = \
        cartesian_communicator.Shift(0, 1)
    
    # Shift(1,1) = move in column direction (left/right)
    neighbour_processes[LEFT], neighbour_processes[RIGHT] = \
        cartesian_communicator.Shift(1, 1)

    # Print my position and who my neighbours are
    print("Process = %s \
row = %s \
column = %s \n----> \nneighbour_processes[UP] = %s\n\
neighbour_processes[DOWN] = %s\n\
neighbour_processes[LEFT] = %s\nneighbour_processes[RIGHT] = %s\n" \
        % (rank, my_mpi_row, my_mpi_col, neighbour_processes[UP],
           neighbour_processes[DOWN], neighbour_processes[LEFT],
           neighbour_processes[RIGHT]))
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
