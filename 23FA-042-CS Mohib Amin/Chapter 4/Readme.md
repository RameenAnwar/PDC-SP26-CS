
CHAPTER 4

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: helloworld_MPI.py

## Description
This script is a basic introductory program for parallel computing with MPI (Message Passing Interface).
It initializes the multi-process environment and has each process figure out and print its own unique ID number.

## When to Execute
Run using "mpiexec -n 4 python helloworld_MPI.py". 
Execute this specialized process during massive multi-directional state changes, such as parallel Fast Fourier Transforms (FFTs) or complete matrix transpositions.

## What We Learned
- How to pull in the core MPI module using the mpi4py library.
- Working with the global group of processes known as COMM_WORLD.
- Using Get_rank() so a process can find out its own ID.

## Advantages
- Extremely simple and clean code, which makes it perfect for troubleshooting network or setup issues.
- Scales up completely on its own; you can run it with 2 processes or 200 without changing a single line of code.

## Disadvantages
- It doesn't actually pass any data or messages back and forth between the processes.
- The terminal text can look scrambled and print out of order because all the processes are trying to talk to the screen at the exact same time.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: pointToPointCommunication.py

## Description
This script shows the most basic way to send messages directly from one process to another. 
It uses explicit, direct commands to pass an integer value from process 0 to process 4, and a text string from process 1 to process 8.

## When to Execute
Run using "mpiexec -n 9 python pointToPointCommunication.py".

## What We Learned
- Using comm.send() to target a message to a very specific process destination.
- Using comm.recv() to make a process pause and wait for incoming data from a specific sender.

## Advantages
- Gives you complete control over the path data takes without involving or slowing down other processes in the network.
- Great for building tailored master-worker setups where different workers get completely different tasks.

## Disadvantages
- High risk of causing a total freeze (deadlock) if you accidentally misnumber a sender or receiver destination.
- Becomes incredibly messy and difficult to manage by hand as your pool of processes grows larger.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: deadLockProblems.py
## Description
This code is a deliberate example of a programming trap called a deadlock. It sets up two processes that both try to read a message before sending anything out, causing them to get stuck waiting for each other forever.

## When to Execute
Run using "mpiexec -n 6 python deadLockProblems.py".
Run this as a learning exercise when you want to study execution bugs, see how blocking functions behave, or practice debugging a frozen application.

## What We Learned
- Seeing firsthand how a poor ordering of communication commands can completely freeze a parallel application.
- Understanding why matching send and receive actions must be carefully timed and aligned.

## Advantages
- Works as an excellent teaching tool to help developers spot and avoid bad communication design early on.
- Helps explain why using non-blocking commands or safer collective operations is usually a better choice.

## Disadvantages
- The program will lock up completely, forcing you to manually shut it down using Ctrl+C in your terminal.
- Tracking down these kinds of circular dependency bugs in massive, real-world systems can be a massive headache.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: broadcast.py
## Description
This script demonstrates a collective communication pattern known as broadcasting. One main process (rank 0) holds a specific value and shares it globally so that every single process in the network gets a copy.

## When to Execute
Run using "mpiexec -n 4 python broadcast.py". 
Execute this pattern whenever every execution thread requires an identical copy of shared state data, such as neural network weights, hyperparameters, or simulation boundaries.

## What We Learned
- Sharing data instantly across an entire group using the comm.bcast() function.
- Restricting initial setup tasks to the root process (rank 0) before sharing the results.

## Advantages
- Massive time saver compared to using a manual loop to message every single process one by one.
- Cleans up your code significantly by turning a multi-step delivery process into a single line.

## Disadvantages
- Creates a temporary bottleneck because faster processes have to sit idle and wait until the root process is ready to broadcast.
- Can waste system memory if certain processes in your cluster don't actually need that data for their specific tasks.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: scatter.py
## Description
This script shows how to chop up a large dataset and hand it out across a parallel system. The main process takes a master list of numbers and evenly splits it, giving one unique piece to each available process.

## When to Execute
Run using "mpiexec -n 10 python scatter.py".
Use this when you are starting a "divide and conquer" task where a massive dataset needs to be split up among multiple workers so they can process it simultaneously.

## What We Learned
- Automatically dividing data blocks using the comm.scatter() collective function.
- Managing the rule that your data list size must match the exact number of running processes.

## Advantages
- Handles all the math for data slicing internally, which saves you from writing error-prone manual loops.
- Sets up true data parallelism by giving every single processor its own exclusive chunk of work.

## Disadvantages
- Very rigid; the program will crash if your array size doesn't divide perfectly among your active workers.
- Puts heavy memory pressure on the main process (rank 0) since it has to load the entire dataset before splitting it up.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: gather.py
## Description
This script is the exact opposite of the scatter process. It gathers individual data points generated independently by every process across the system and stacks them back together into one organized list on the main process.

## When to Execute
Run using "mpiexec -n 4 python gather.py".
Use this at the very end of a parallel computation phase to pull all the individual results back into a single place for final reporting, math checks, or saving to a file.

## What We Learned
- Using comm.gather() to collect distributed data back into a single process array.
- Writing logic so that only the main process processes or prints out the final gathered collection.

## Advantages
- Provides a clean, automated way to pack results together without writing messy collection logic.
- Keeps everything organized by automatically keeping the data in order based on the process ID number.

## Disadvantages
- The main process can easily run out of memory if it tries to gather massive datasets from a huge number of workers all at once.
- Forces all workers to stop and wait until the collection is fully complete before anyone can move forward.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: reduction.py
## Description
This script shows how to use a collective operation called a reduction. It collects numbers from all the processes but, instead of making a list, it condenses them into a single value (like a total sum) using a math operator.

## When to Execute
Run using "mpiexec -n 4 python reduction.py".
Use this when you need to calculate global metrics across your entire system, such as adding up partial calculations, finding an average, or looking for the min/max value.

## What We Learned
- Combining distributed numbers using comm.Reduce() alongside high-speed numpy arrays.
- Using built-in MPI operation flags like MPI.SUM to handle math calculations on the fly.

## Advantages
- Incredibly fast and highly optimized because it combines data while it is moving through the network.
- Uses very little memory since it crushes the data down into a single result instead of storing a massive list.

## Disadvantages
- You are strictly limited to basic mathematical or logical operations that can be processed in any order.
- The final answer is only saved on the main process; if other workers need to know the result, you have to add an extra step to share it.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: alltoall.py
## Description
This script shows a complex, full-mesh data swap. Every single process holds an initial list of data, breaks it apart, and distributes a unique portion of it to every other process in the entire system.

## When to Execute
Run using "mpiexec -n 4 python alltoall.py".
Use this during heavy multi-directional data shuffles, such as transposing a large matrix or running complex scientific math like parallel Fast Fourier Transforms (FFTs).

## What We Learned
- Handling advanced global data swaps using the comm.Alltoall() method.
- Formatting rigid numpy array buffers to ensure data moves through the network without hitches.

## Advantages
- Replaces hundreds of confusing process-to-process messages with just one clean, highly optimized collective call.
- Allows an entire cluster to completely restructure and trade data with each other all at once.

## Disadvantages
- Puts a massive strain on network bandwidth, which can severely slow things down as you add more processes.
- Extremely strict about formatting; every single send and receive buffer across all processes must match in size perfectly.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: virtualTopology.py
## Description
This script organizes a simple list of processes into a structured 2D grid layout (a Cartesian map). This allows every process to easily look up its coordinates and identify its immediate neighbors (Up, Down, Left, Right).

## When to Execute
Run using "mpiexec -n 4 python virtualTopology.py".
Use this when writing grid-based simulations, like mapping out weather patterns, fluid dynamics, or any system where data naturally flows between neighboring physical areas.

## What We Learned
- Mapping a flat list of processes into a 2D plane using comm.Create_cart().
- Using the Shift() command to automatically find the ID numbers of adjacent neighbor processes.

## Advantages
- Simplifies the math and logic for data sharing, making neighbor-to-neighbor communication much easier to write.
- Helps the underlying software optimize performance by matching your virtual grid to the actual physical layout of the computer cores.

## Disadvantages
- Adds a layer of setup complexity when configuring and debugging your initial process layout.
- Limits your flexibility, as the number of processes you launch must fit into your grid dimensions.