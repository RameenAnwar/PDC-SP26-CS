**************************************************************************************************
**Chapter: 04       Name: Javaria Owais        Roll Number: 23FA-017-CS**
**************************************************************************************************

## Message Passing 
Message Passing is a parallel programming technique where multiple processes communicate with each other by sending and receiving messages. It is commonly used in distributed systems where each process has its own memory space.

### MPI (Message Passing Interface)
MPI is a standardized library used for communication between processes in parallel computing. In Python, it is implemented using the `mpi4py` module.

### Main Concept
- Multiple processes run independently  
- Each process has a unique ID (rank)  
- Processes communicate using messages  
- No shared memory (unlike threading)  

### Code Interpretation (helloworld_MPI.py)
*Importing Module*
from mpi4py import MPI
- imports MPI functionality for message passing  

*Creating Communicator*
comm = MPI.COMM_WORLD
- Defines a communication group  
- `COMM_WORLD` includes **all processes**  

*Getting Process Rank*
rank = comm.Get_rank()
- Each process gets a **unique ID (rank)**  
- Rank starts from **0 to (n-1)**  

*Printing Output*
print("hello world from process ", rank)
- Each process prints its own message  
- Output depends on number of processes  

### Program Execution
Run using:
    mpiexec -n 4 python hello.py
- `-n 4` runs program with 4 processes  

### Output Behavior
hello world from process  0
hello world from process  1
hello world from process  2
hello world from process  3
- Order of output may vary 

### Advantages of Message Passing
- Scalable for large systems  
- Suitable for high-performance computing  

### Limitations
- Communication overhead  
- More complex than threading  
- Requires MPI setup  

**************************************************************************************************

## Point-to-Point Communication (MPI)
Point-to-Point communication is a method where **one process sends data directly to another specific process**. It is the simplest form of message passing in MPI.

### Main Concept
- Communication happens between two processes  
- One process sends, another receives  
- Uses `send()` and `recv()` functions  
- One-to-one communication  

### Code Interpretation
*Importing Module*
`from mpi4py import MPI` => MPI communication  

*MPI Setup*
comm = MPI.COMM_WORLD
rank = comm.rank

*Printing Rank*
print("my rank is :", rank)
- Each process prints its own ID  

*Sending Data (Process 0 to Process 4)*
if rank == 0:
    data = 10000000
    destination_process = 4
    comm.send(data, dest=destination_process)
- Process 0 sends integer data to process 4  

*Sending Data (Process 1 to Process 8)*
if rank == 1:
    data = "hello"
    destination_process = 8
    comm.send(data, dest=destination_process)
- Process 1 sends string data to process 8  

*Receiving Data (Process 4)*
if rank == 4:
    data = comm.recv(source=0)
- Process 4 receives data from process 0  

*Receiving Data (Process 8)*
if rank == 8:
    data1 = comm.recv(source=1)
- Process 8 receives data from process 1  

### Output Behavior (Example)
my rank is : 0
sending data 10000000 to process 4

my rank is : 1
sending data hello to process 8

my rank is : 4
data received is = 10000000

my rank is : 8
data1 received is = hello

- Only involved processes send/receive  
- Other processes just print their rank  
- Output order may vary  

### Advantages of Point-to-Point
- Simple and direct communication  
- Flexible (can send any data type)  
- Useful for specific data transfer  

### Limitations
- Not scalable for many processes  
- Requires manual management of sender/receiver  
- Risk of deadlock if not handled properly  

**************************************************************************************************

## All-to-All Communication (MPI)
All-to-All communication is a message passing operation where **each process sends data to every other process and receives data from every process**. It is used when all processes need to exchange information simultaneously.

### Main Concept
- Every process sends data to all processes  
- Every process receives data from all processes  
- Communication happens in a structured pattern  
- Requires equal-sized data from each process  

### Code Interpretation (alltoall.py)
*Importing Modules*
`from mpi4py import MPI` => MPI communication  
`import numpy` => array handling  

*MPI Setup*
comm = MPI.COMM_WORLD
size = comm.Get_size()
rank = comm.Get_rank()
- `COMM_WORLD` => all processes  
- `size` => total number of processes  
- `rank` => unique ID of each process  

*Creating Send Data*
senddata = (rank+1)*numpy.arange(size, dtype=int)
- Each process creates its own array  
- `numpy.arange(size)` => [0, 1, 2, ..., size-1]  
- Multiplied by `(rank+1)` => unique data per process  

Example (size = 4):
- Process 0 → [0, 1, 2, 3]  
- Process 1 → [0, 2, 4, 6]  
- Process 2 → [0, 3, 6, 9]  
- Process 3 → [0, 4, 8, 12]  

*Receiving Buffer*
recvdata = numpy.empty(size, dtype=int)
- Empty array to store received data  
- Size must match number of processes  

*All-to-All Communication*
comm.Alltoall(senddata, recvdata)
- Each process sends one element to every other process  
- Each process receives one element from every process  
- Communication happens simultaneously  

*Printing Output*
print("process %s sending %s receiving %s" % (rank, senddata, recvdata))
- Shows what each process sends and receives  

### Output Behavior (Example)
process 0 sending [0 1 2 3] receiving [0 0 0 0]
process 1 sending [0 2 4 6] receiving [1 2 3 4]
process 2 sending [0 3 6 9] receiving [2 4 6 8]
process 3 sending [0 4 8 12] receiving [3 6 9 12]
- Each process gets one value from every other process  
- Output order may vary  

### Advantages of All-to-All
- Efficient for full data exchange  
- Useful in parallel algorithms  
- Supports distributed computation  

### Limitations
- High communication cost  
- Requires equal data sizes  
- Not efficient for large-scale communication  

**************************************************************************************************

## Broadcast Communication (MPI)
Broadcast is a message passing operation where **one process sends data to all other processes**. It is commonly used when the same data needs to be shared across all processes.

### Main Concept
- One process acts as **root (sender)**  
- All other processes act as **receivers**  
- Data is copied from root to every process  
- Efficient one-to-many communication  

### Code Interpretation
*Importing Module*
`from mpi4py import MPI` => MPI communication  

*MPI Setup*
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

*Defining Data at Root*
if rank == 0:
    variable_to_share = 100
else:
    variable_to_share = None
- Only **process 0 (root)** has actual data  
- Other processes initialize variable as `None`  

*Broadcast Operation*
variable_to_share = comm.bcast(variable_to_share, root=0)
- Root process sends value to all processes  
- After execution all processes have same value  

*Printing Output*
print("process = %d" % rank + " variable shared = %d " % variable_to_share)
- Each process prints its rank and received value  

### Output Behavior (Example)
process = 0 variable shared = 100
process = 1 variable shared = 100
process = 2 variable shared = 100
process = 3 variable shared = 100
- All processes receive the same value  
- Order may vary  

### Advantages of Broadcast
- Efficient one-to-many communication  
- Reduces redundant data sending  
- Simple and fast data distribution  

### Limitations
- Only one sender (root)  
- All processes must participate  
- Not suitable for selective communication  

**************************************************************************************************

## Gather Communication (MPI)
Gather is a message passing operation where **all processes send their data to a single process (root)**. It is used to collect results from multiple processes into one place.

### Main Concept
- All processes send data  
- One process (root) receives everything  
- Many-to-one communication  
- Result stored as a list/collection at root  

### Code Interpretation
*Importing Module*
`from mpi4py import MPI` => MPI communication  

*MPI Setup*
comm = MPI.COMM_WORLD
size = comm.Get_size() **total number of processes**
rank = comm.Get_rank() **unique id of each process**

*Creating Local Data*
data = (rank+1)**2
- Each process generates its own value  
- Example:
  - Process 0 => 1  
  - Process 1 => 4  
...

*Gather Operation*
data = comm.gather(data, root=0)
- All processes send their data to **process 0 (root)**  
- Root receives data as a list  
- Other processes get `None`  

*Printing Output (Root Only)*
if rank == 0:
- Only root prints the collected data  

for i in range(1, size):
    value = data[i]
    print("process %s receiving %s from process %s" % (rank, value, i))
- Iterates through received values  
- Displays which process sent which data  

### Output Behavior (Example)
rank = 0 ...receiving data to other process
process 0 receiving 4 from process 1
process 0 receiving 9 from process 2
process 0 receiving 16 from process 3
- Only root process prints output  
- Root collects data from all processes  

### Advantages of Gather
- Efficient result collection  
- Simplifies data aggregation  
- Useful in parallel computations  

### Limitations
- Root becomes bottleneck  
- Not scalable for very large data  
- All data stored in one process  

**************************************************************************************************

## Scatter Communication (MPI)
Scatter is a message passing operation where **one process (root) distributes parts of data to all processes**. It is the opposite of Gather.

### Main Concept
- One process (root) sends data  
- Data is divided into parts  
- Each process receives one part  
- One-to-many communication  

### Code Interpretation
*Importing Module*
`from mpi4py import MPI` => MPI communication  

*MPI Setup*
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

*Defining Data at Root*
if rank == 0:
    array_to_share = [1,2,3,4,5,6,7,8,9,10]
else:
    array_to_share = None
- Root process holds full list  
- Other processes have no data initially  

*Scatter Operation*
recvbuf = comm.scatter(array_to_share, root=0)
- Root splits list into equal parts  
- Each process receives one element  
- Data distributed based on process rank  

*Printing Output*
print("process = %d" % rank + " variable shared = %d " % recvbuf)
- Each process prints its received value  

### Output Behavior (Example)
process = 0 variable shared = 1
process = 1 variable shared = 2
process = 2 variable shared = 3
process = 3 variable shared = 4
- Each process gets one element  
- Order depends on rank  

### Advantages of Scatter
- Efficient data distribution  
- Reduces workload per process  
- Useful for parallel tasks  

### Limitations
- Data must be evenly divisible  
- Only one sender (root)  
- Limited flexibility in distribution  

**************************************************************************************************

## Reduce Communication (MPI)
Reduce is a message passing operation where **all processes send data to a root process, and a computation (like sum, max, etc) is performed on that data**.

### Main Concept
- All processes contribute data  
- A reduction operation is applied (e.g., SUM)  
- Result is stored at root process  
- Many-to-one communication with computation  

### Code Interpretation
*Importing Modules*
`from mpi4py import MPI` => MPI communication  
`import numpy` => array handling  

*MPI Setup*
comm = MPI.COMM_WORLD
size = comm.size
rank = comm.rank

*Array Initialization*
array_size = 10
recvdata = numpy.zeros(array_size, dtype=numpy.int)
senddata = (rank+1)*numpy.arange(array_size, dtype=numpy.int)
- `senddata` => each process creates its own array, values differ based on rank  
- `recvdata` => empty array to store result (only useful at root)  

*Printing Send Data*
print("process %s sending %s" % (rank, senddata))
- Shows data each process is contributing  

*Reduce Operation*
comm.Reduce(senddata, recvdata, root=0, op=MPI.SUM)
- Combines data from all processes  
- Operation used: `SUM`  
- Result stored only in root (process 0)  

*Printing Result*
print('on task', rank, 'after Reduce: data = ', recvdata)
- Root process prints final computed result  
- Other processes may show empty/default array  

### Output Behavior (Example)
process 0 sending [...]
process 1 sending [...]
process 2 sending [...]
process 3 sending [...]

on task 0 after Reduce: data = [sum of all arrays]
on task 1 after Reduce: data = [0 0 0 ...]
on task 2 after Reduce: data = [0 0 0 ...]
on task 3 after Reduce: data = [0 0 0 ...]
...
- Only root gets the final reduced result  
- Others do not receive the result  

### Advantages of Reduce
- Performs computation during communication  
- Efficient aggregation of results  
- Widely used in parallel algorithms  

### Limitations
- Result available only at root (can create bottleneck) 
- Limited to predefined operations (SUM, MAX, etc.)  

**************************************************************************************************

## Deadlock Problem in MPI
A deadlock occurs when two or more processes are waiting for each other indefinitely, and none of them can proceed. In MPI, deadlocks commonly happen when using blocking communication i.e. send() and recv() in the wrong order.

### Main Concept
- Processes depend on each other to proceed  
- If both processes wait - program freezes  
- Occurs due to improper ordering of send/receive  
- Common in blocking communication  

### Code Interpretation
*Importing Module*
`from mpi4py import MPI` MPI communication  

*MPI Setup*
comm = MPI.COMM_WORLD
rank = comm.rank

*Printing Rank*
print("my rank is %i" % (rank))

**Communication Logic**
*Process 1*
if rank == 1:
    data_received = comm.recv(source=5)
    comm.send("a", dest=5)
- First waits to **receive** from process 5  
- Then sends data  

*Process 5*
if rank == 5:
    comm.send("b", dest=1)
    data_received = comm.recv(source=1)
- First **sends** data to process 1  
- Then waits to receive  

### Why This Avoids Deadlock
- Process 5 sends first  
- Process 1 receives first  
> Communication succeeds because one process is sending while the other is receiving  

### What Causes Deadlock 
If both processes do this:
comm.recv()
comm.send()
Then:
- Both wait to receive  
- No one sends  
- Program gets stuck (deadlock) 

### Output Behavior (Example)
my rank is 1
my rank is 5

sending data b to process 1
data received is = a

sending data a to process 5
data received is = b

### Advantages
- Demonstrates how deadlock situations occur  
- Helps understand synchronization issues  
- Useful for learning correct communication patterns  

### Limitations
- Easy to create deadlocks in complex systems  
- Requires careful ordering of operations  
- Blocking calls can freeze the program  

### Key Takeaway
> Deadlock happens when processes wait forever.  
> To avoid it, ensure one process sends while the other receives.

**************************************************************************************************

## Virtual Topology (MPI Cartesian Grid)
A virtual topology arranges processes in a structured way (like a grid) instead of treating them as independent units. In this example, processes are organized into a **2D Cartesian grid**, and each process identifies its neighbors.

### Main Concept
- Processes are arranged in a grid structure  
- Each process has coordinates (row, column)  
- Each process can find its neighbors  
- Supports structured communication patterns  

### Code Interpretation
*Importing Modules*
`from mpi4py import MPI` MPI communication  
`import numpy as np` mathematical operations  

*Direction Constants*
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
neighbour_processes = [0,0,0,0]
- Used to store neighbor ranks  
- Index-based direction mapping  

*MPI Setup*
comm = MPI.COMM_WORLD
rank = comm.rank
size = comm.size

*Grid Creation*
grid_row = int(np.floor(np.sqrt(comm.size)))
grid_column = comm.size // grid_row
- Converts processes into a 2D grid  

*Grid Adjustment*
if grid_row * grid_column > size:
    grid_column -= 1
if grid_row * grid_column > size:
    grid_row -= 1
- Ensures grid fits total processes  

*Printing Grid*
if rank == 0:
    print("Building a %d x %d grid topology" % (grid_row, grid_column))
- Root prints grid size  

*Creating Cartesian Topology*
cartesian_communicator = comm.Create_cart(
    (grid_row, grid_column),
    periods=(True, True),
    reorder=True
)
- Creates 2D grid topology  
- `periods=True` > wrap-around (circular grid)  
- `reorder=True` > MPI may optimize rank placement  

*Getting Coordinates*
my_mpi_row, my_mpi_col = cartesian_communicator.Get_coords(
    cartesian_communicator.rank
)
- Each process gets its position in grid  

*Finding Neighbors*
neighbour_processes[UP], neighbour_processes[DOWN] = cartesian_communicator.Shift(0, 1)
neighbour_processes[LEFT], neighbour_processes[RIGHT] = cartesian_communicator.Shift(1, 1)
- `Shift(0,1)` > row movement (up/down)  
- `Shift(1,1)` > column movement (left/right)  

*Printing Output*
print("Process = %s row = %s column = %s ..." % (...))
- Displays rank, position, and neighbors  

### Output Behavior (Example)
Building a 3 x 3 grid topology

Process = 0 row = 0 column = 0
UP = 6
DOWN = 3
LEFT = 2
RIGHT = 1

Process = 1 row = 0 column = 1
UP = 7
DOWN = 4
LEFT = 0
RIGHT = 2
...
- Each process prints its neighbors  
- Due to wrap-around, edge processes connect to opposite side  

### Advantages of Virtual Topology
- Organized communication structure  
- Efficient neighbor-based communication  
- Useful in grid-based problems (matrix, simulations)  

### Limitations
- More complex than basic communication  
- Requires careful grid design  
- Overhead in topology creation  

### Key Takeaway
> Virtual topology organizes processes in a structured grid, allowing efficient communication with neighboring processes.

**************************************************************************************************