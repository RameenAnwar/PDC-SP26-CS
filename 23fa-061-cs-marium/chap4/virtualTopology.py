from mpi4py import MPI
import numpy as np

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
neighbour_processes = [0,0,0,0]
if __name__ == "__main__":
    comm = MPI.COMM_WORLD
    rank = comm.rank
    size = comm.size

    grid_row = int(np.floor(np.sqrt(comm.size)))
    grid_column = comm.size // grid_row

        
    if grid_row*grid_column > size:
        grid_column -= 1
    if grid_row*grid_column > size:
        grid_row -= 1

    if (rank == 0) :
        print("Building a %d x %d grid topology:"\
              % (grid_row, grid_column) )
               

    cartesian_communicator = \
                           comm.Create_cart( \
                               (grid_row, grid_column), \
                               periods=(True, True), reorder=True)
    my_mpi_row, my_mpi_col = \
                cartesian_communicator.Get_coords\
                ( cartesian_communicator.rank ) 


    neighbour_processes[UP], neighbour_processes[DOWN]\
                             = cartesian_communicator.Shift(0, 1)
    neighbour_processes[LEFT],  \
                               neighbour_processes[RIGHT]  = \
                               cartesian_communicator.Shift(1, 1)
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
 
# Output

# Building a 2 x 2 grid topology:

# Process = 0 
# row = 0 
# column = 0 
# ----> 
# neighbour_processes[UP] = 2
# neighbour_processes[DOWN] = 2
# neighbour_processes[LEFT] = 1
# neighbour_processes[RIGHT] = 1

# Process = 1 
# row = 0 
# column = 1 
# ----> 
# neighbour_processes[UP] = 3
# neighbour_processes[DOWN] = 3
# neighbour_processes[LEFT] = 0
# neighbour_processes[RIGHT] = 0

# Process = 2 
# row = 1 
# column = 0 
# ----> 
# neighbour_processes[UP] = 0
# neighbour_processes[DOWN] = 0
# neighbour_processes[LEFT] = 3
# neighbour_processes[RIGHT] = 3

# Process = 3 
# row = 1 
# column = 1 
# ----> 
# neighbour_processes[UP] = 1
# neighbour_processes[DOWN] = 1
# neighbour_processes[LEFT] = 2
# neighbour_processes[RIGHT] = 2 