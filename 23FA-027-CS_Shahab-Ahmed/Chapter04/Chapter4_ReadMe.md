# MPI Alltoall Communication (mpi4py)

## Description
This code demonstrates parallel communication using `mpi4py`, where each process sends and receives data from all other processes using `Alltoall`.

## What This Code Does
- Initializes MPI environment  
- Gets total number of processes and current process rank  
- Each process creates a data array based on its rank  
- Uses `Alltoall` to exchange data between all processes  
- Prints sent and received data  

## Execution Flow
1. Initialize MPI communicator (`COMM_WORLD`)  
2. Get number of processes (`size`)  
3. Get process ID (`rank`)  
4. Each process creates `senddata` array  
5. Create empty `recvdata` array  
6. Perform `Alltoall` communication  
7. Print sent and received values  

## How to Execute
1. Install MPI and mpi4py:
   ```bash
   pip install mpi4py


# MPI Broadcast (mpi4py)

## Description
This code demonstrates broadcasting using `mpi4py`, where one process shares data with all other processes.

## What This Code Does
- Initializes MPI environment  
- Process 0 creates a variable  
- All other processes start with `None`  
- Uses `bcast()` to broadcast value from root process  
- All processes receive the same value  

## Execution Flow
1. Initialize MPI communicator (`COMM_WORLD`)  
2. Get process rank  
3. If rank is 0:
   - Set variable value (100)  
4. Other processes set variable to `None`  
5. Use `comm.bcast()` to broadcast value  
6. All processes receive same value  
7. Print process rank and received value  

## How to Execute
1. Install mpi4py:
   ```bash
   pip install mpi4py


# MPI Send and Receive Communication (mpi4py)

## Description
This code demonstrates point-to-point communication in MPI using `send()` and `recv()` between two processes.

## What This Code Does
- Initializes MPI environment  
- Identifies process rank  
- Process 1 and Process 5 exchange messages  
- Uses `send()` and `recv()` for direct communication  
- Each process sends and receives data from the other  

## Execution Flow
1. Initialize MPI communicator (`COMM_WORLD`)  
2. Get process rank  
3. If rank = 1:
   - Send data `"a"` to process 5  
   - Receive data from process 5  
   - Print sent and received values  
4. If rank = 5:
   - Send data `"b"` to process 1  
   - Receive data from process 1  
   - Print sent and received values  

## How to Execute
1. Install mpi4py:
   ```bash
   pip install mpi4py


# MPI Gather Communication (mpi4py)

## Description
This code demonstrates the use of `gather()` in MPI, where all processes send data to a single root process.

## What This Code Does
- Initializes MPI environment  
- Each process generates its own data value  
- All processes send data to process 0 (root)  
- Root process collects and prints all received data  

## Execution Flow
1. Initialize MPI communicator (`COMM_WORLD`)  
2. Get total number of processes (`size`)  
3. Get process rank (`rank`)  
4. Each process calculates data: `(rank + 1)^2`  
5. Use `gather()` to send data to root process (0)  
6. Root process:
   - Receives all data  
   - Prints values from all processes  

## How to Execute
1. Install mpi4py:
   ```bash
   pip install mpi4py


# MPI Send and Receive (Multiple Processes)

## Description
This code demonstrates point-to-point communication in MPI where different processes send and receive data using `send()` and `recv()`.

## What This Code Does
- Initializes MPI environment  
- Multiple processes communicate using ranks  
- Process 0 sends numeric data to process 4  
- Process 1 sends string data to process 8  
- Processes 4 and 8 receive and print data  

## Execution Flow
1. Initialize MPI communicator (`COMM_WORLD`)  
2. Get process rank  
3. If rank = 0:
   - Send integer data to process 4  
4. If rank = 1:
   - Send string data to process 8  
5. If rank = 4:
   - Receive data from process 0  
6. If rank = 8:
   - Receive data from process 1  
7. Each process prints its rank and received/sent data  

## How to Execute
1. Install mpi4py:
   ```bash
   pip install mpi4py


# MPI Reduce Operation (mpi4py)

## Description
This code demonstrates the use of `Reduce` in MPI, where data from all processes is combined into a single result at the root process.

## What This Code Does
- Initializes MPI environment  
- Each process creates a NumPy array  
- Each process sends its data to root process (0)  
- `Reduce` performs summation of all arrays  
- Result is stored in `recvdata` at root  

## Execution Flow
1. Initialize MPI communicator (`COMM_WORLD`)  
2. Get process rank and size  
3. Create send array for each process  
4. Initialize receive array (only used at root)  
5. Each process sends data using `Reduce()`  
6. MPI sums all arrays (`MPI.SUM`)  
7. Root process receives final result  
8. All processes print output  

## How to Execute
1. Install required libraries:
   ```bash
   pip install mpi4py numpy


# MPI Scatter Communication (mpi4py)

## Description
This code demonstrates the use of `scatter()` in MPI, where data is distributed from one root process to all other processes.

## What This Code Does
- Initializes MPI environment  
- Process 0 creates a list of data  
- Data is split and distributed among all processes  
- Each process receives one element  
- Each process prints its received value  

## Execution Flow
1. Initialize MPI communicator (`COMM_WORLD`)  
2. Get process rank  
3. If rank = 0:
   - Create list `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`  
4. Other processes set data to `None`  
5. Use `scatter()` to distribute data  
6. Each process receives one value  
7. Print process rank and received value  

## How to Execute
1. Install mpi4py:
   ```bash
   pip install mpi4py


# MPI Cartesian Topology (mpi4py)

## Description
This code demonstrates the creation of a Cartesian grid topology in MPI, where processes are arranged in a 2D grid and each process identifies its neighboring processes.

## What This Code Does
- Initializes MPI environment  
- Organizes processes into a 2D grid (rows × columns)  
- Creates a Cartesian communicator  
- Finds each process’s position in the grid  
- Identifies neighboring processes (UP, DOWN, LEFT, RIGHT)  
- Prints process location and neighbors  

## Execution Flow
1. Initialize MPI communicator (`COMM_WORLD`)  
2. Get total number of processes  
3. Compute grid size (rows and columns)  
4. Create Cartesian topology using `Create_cart()`  
5. Get coordinates of each process in grid  
6. Use `Shift()` to find neighbors:
   - UP / DOWN  
   - LEFT / RIGHT  
7. Print process rank, position, and neighbors  

## How to Execute
1. Install required package:
   ```bash
   pip install mpi4py numpy
