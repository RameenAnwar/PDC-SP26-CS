MPI Virtual Topology: 
A minimal Python script demonstrating how to organize processes into a 2D grid (Cartesian topology) and identify neighboring processes using the `mpi4py` and `numpy` libraries.

Prerequisites:
You need a system-level MPI implementation (like OpenMPI or MPICH) installed. Then, install the required Python packages:

```bash
pip install numpy mpi4py

```

How to Run:
Launch the script using an MPI executor. To see a perfect square grid, running with 4 processes (which creates a 2x2 grid) or 9 processes (3x3 grid) is ideal. Use the following command in your terminal:

```bash
mpiexec -n 4 python script_name.py

```

What it Does:
This script moves beyond standard linear process ranks by organizing them into a spatial grid, which is incredibly useful for physics simulations or image processing:

1. Grid Calculation: It dynamically calculates a 2D grid shape (rows and columns) that best fits the total number of running processes using `numpy.sqrt()`.
2. Cartesian Communicator: `comm.Create_cart()` creates a new communicator with this 2D grid topology.
* The `periods=(True, True)` argument means the grid wraps around on both axes. The "top" connects to the "bottom," and the "left" connects to the "right" (creating a torus shape).
3. Coordinates: Each process gets its specific `(row, column)` coordinates in this new grid.
4. Neighbor Discovery: The `Shift()` method is used to instantly find the ranks of the processes immediately UP, DOWN, LEFT, and RIGHT of the current process.

Example Output:
Running with 4 processes yields an output similar to the following (building a 2x2 grid):

```text
Building a 2 x 2 grid topology:
Process = 0 row = 0 column = 0 
----> 
neighbour_processes[UP] = 2
neighbour_processes[DOWN] = 2
neighbour_processes[LEFT] = 1
neighbour_processes[RIGHT]= 1

Process = 1 row = 0 column = 1 
----> 
neighbour_processes[UP] = 3
neighbour_processes[DOWN] = 3
neighbour_processes[LEFT] = 0
neighbour_processes[RIGHT]= 0

Process = 2 row = 1 column = 0 
----> 
neighbour_processes[UP] = 0
neighbour_processes[DOWN] = 0
neighbour_processes[LEFT] = 3
neighbour_processes[RIGHT]= 3

Process = 3 row = 1 column = 1 
----> 
neighbour_processes[UP] = 1
neighbour_processes[DOWN] = 1
neighbour_processes[LEFT] = 2
neighbour_processes[RIGHT]= 2

```

Note: Because this specific 2x2 grid wraps around (periodic boundaries), the "Up" neighbor is the same as the "Down" neighbor, and the "Left" is the same as the "Right." Try running with 9 processes (`mpiexec -n 9`) to see distinct neighbors in all 4 directions!
