# virtualTopology.py  --  Chapter 4: Virtual Topologies (Cartesian grid)
# Arranges the processes into a 2D grid (Cartesian topology) and finds each
# process's UP/DOWN/LEFT/RIGHT neighbours. periods=(True,True) makes the grid wrap
# around (a torus). Best run with a perfect-square number of processes, e.g. 4.
# RUN COMMAND:  mpiexec -n 4 python virtualTopology.py
#
# ----------------------- CODE (commented out) -----------------------
# from mpi4py import MPI
# import numpy as np
# UP = 0; DOWN = 1; LEFT = 2; RIGHT = 3
# neighbour_processes = [0, 0, 0, 0]
# if __name__ == "__main__":
#     comm = MPI.COMM_WORLD
#     rank = comm.rank
#     size = comm.size
#     grid_row = int(np.floor(np.sqrt(comm.size)))   # rows of the grid
#     grid_column = comm.size // grid_row            # columns of the grid
#     if grid_row * grid_column > size:
#         grid_column -= 1
#     if grid_row * grid_column > size:
#         grid_row -= 1
#     if rank == 0:
#         print("Building a %d x %d grid topology:" % (grid_row, grid_column))
#     cartesian_communicator = comm.Create_cart(
#         (grid_row, grid_column), periods=(True, True), reorder=True)
#     my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords(cartesian_communicator.rank)
#     # Shift finds neighbours along each axis (wraps around because periods=True)
#     neighbour_processes[UP], neighbour_processes[DOWN] = cartesian_communicator.Shift(0, 1)
#     neighbour_processes[LEFT], neighbour_processes[RIGHT] = cartesian_communicator.Shift(1, 1)
#     print("Process = %s row = %s column = %s ----> neighbours UP/DOWN/LEFT/RIGHT = %s/%s/%s/%s"
#           % (rank, my_mpi_row, my_mpi_col,
#              neighbour_processes[UP], neighbour_processes[DOWN],
#              neighbour_processes[LEFT], neighbour_processes[RIGHT]))
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# (run with 4 processes -> a 2 x 2 wrap-around grid)
# Building a 2 x 2 grid topology:
# Process = 0 row = 0 column = 0 ----> neighbours UP/DOWN/LEFT/RIGHT = 2/2/1/1
# Process = 1 row = 0 column = 1 ----> neighbours UP/DOWN/LEFT/RIGHT = 3/3/0/0
# Process = 2 row = 1 column = 0 ----> neighbours UP/DOWN/LEFT/RIGHT = 0/0/3/3
# Process = 3 row = 1 column = 1 ----> neighbours UP/DOWN/LEFT/RIGHT = 1/1/2/2
# --------------------------------------------------------------------
