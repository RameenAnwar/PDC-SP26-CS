**************************************************************************************************
**Chapter: 03       Name: Javaria Owais        Roll Number: 23FA-017-CS**
**************************************************************************************************

## Multiprocessing using Subclass (Custom Process)
Multiprocessing allows execution of multiple processes simultaneously. In Python, we can create processes by subclassing the `multiprocessing.Process` class and overriding the `run()` method.
- Processes run independently with separate memory  
- Subclassing allows custom process behavior  
- `run()` method defines process execution  
- `start()` triggers process execution  

### Code Interpretation
*Importing Module*
- multiprocessing => used to create and manage processes  

*Subclassing Process*
class MyProcess(multiprocessing.Process):
- Custom process class  
- Inherits functionality from Process class  

*Overriding run() Method*
def run(self):
    print('called run method in %s' % self.name)
- Defines what each process will execute  
- `self.name` gives unique process name  

*Main Execution Block*
if __name__ == '__main__':
- Required for multiprocessing  
- Prevents recursive process creation  

*Process Creation*
for i in range(10):
    process = MyProcess()
- Creates 10 process instances  

*Starting Process*
process.start()
- Starts a new process  
- Automatically calls `run()` method  

*Process Synchronization*
process.join()
- Main program waits for process to complete  

*Program Flow*
- Loop runs 10 times  
- Each time:
  - A process is created  
  - Process starts  
  - Process executes `run()`  
  - Main waits (join)  
- Processes execute sequentially  

*Output Behavior*
called run method in MyProcess-1  
called run method in MyProcess-2  
...  

### Advantages 
- True parallelism (uses multiple CPU cores)  
- Better performance for CPU-intensive tasks  
- Independent memory space  

### Limitations
- Higher memory usage  
- Process creation overhead  
- Sequential behavior if join() used inside loop  

**************************************************************************************************

## Multiprocessing with Named and Default Processes
Multiprocessing allows execution of multiple processes simultaneously. In Python, processes can be created by assigning a target function and optionally giving a custom name.
- Each process runs independently  
- Target function defines process task  
- Processes can have custom or default names  
- Multiple processes can run in parallel  

### Code Interpretation
*Importing Modules*
- multiprocessing => for creating processes  
- time => to simulate execution delay  

*Function Definition*
def myFunc():
- Function executed by each process  

name = multiprocessing.current_process().name
- Retrieves current process name  

print("Starting process...")
print("Exiting process...")
- Displays start and end of process  

time.sleep(3)
- Simulates processing time  

*Main Execution Block*
if __name__ == '__main__':

*Process with Custom Name*
process_with_name = multiprocessing.Process(name='myFunc process', target=myFunc)
- Assigns custom name  
- Executes myFunc  

*Process with Default Name*
process_with_default_name = multiprocessing.Process(target=myFunc)
- Uses default naming (Process-1, Process-2)  

*Daemon Process (Optional)*
**# process_with_name.daemon = True**
- Runs process in background  
- Ends automatically when main program ends  

*Starting Processes*
process_with_name.start()
process_with_default_name.start()
- Starts both processes  
- Executes in parallel  

*Process Synchronization*
process_with_name.join()
process_with_default_name.join()
- Main waits for processes to finish  

*Program Flow*
- Two processes are created  
- One has custom name, one has default  
- Both start execution simultaneously  
- Each prints start message  
- Each sleeps for 3 seconds  
- Each prints exit message  
- Main program ends after both complete  

*Output Behavior*
Starting process name = myFunc process  
Starting process name = Process-2  

Exiting process name = myFunc process  
Exiting process name = Process-2  

### Advantages 
- True parallel execution  
- Customizable process behavior  
- Efficient for CPU-bound tasks  

### Limitations
- Higher memory usage  
- Process creation overhead  
- Requires proper synchronization  

**************************************************************************************************

## Process Termination in Multiprocessing
Multiprocessing allows creating and managing processes. Python provides methods to monitor and terminate processes during execution.
- A process executes a function independently  
- Process state can be monitored using `is_alive()`  
- Processes can be forcefully terminated using `terminate()`  
- Exit status can be checked using `exitcode`  

### Code Interpretation
*Importing Modules*
- multiprocessing => for process creation  
- time => simulate execution delay  

*Function Definition*
def foo():
- Function executed by process  

*Execution Loop*
for i in range(0,10):
    print(i)
    time.sleep(1)
- Simulates long-running task  

*Process Creation*
p = multiprocessing.Process(target=foo)
- Defines process with target function  

*Before Execution*
p.is_alive()
- Returns False (process not started)  

*Starting Process*
p.start()
- Begins process execution  

*Checking Process State*
p.is_alive()
- Returns True (process running)  

*Process Termination*
p.terminate()
- Forcefully stops the process  
- Does not allow normal completion  

*After Termination*
p.is_alive()
- Returns False (process stopped)  

*Process Synchronization*
p.join()
- Ensures main program waits  

*Exit Code*
p.exitcode
- 0 => normal completion  
- Negative value => terminated process  

*Program Flow*
- Process is created  
- Process starts execution  
- Process begins loop  
- Process is terminated before completion  
- Main waits using join()  
- Exit code is displayed  

*Output Behavior*
Process before execution: <Process name='Process-1' parent=16080 initial> False
Process running: <Process name='Process-1' pid=9944 parent=16080 started> True
Process terminated: <Process name='Process-1' pid=9944 parent=16080 started> True
Process joined: <Process name='Process-1' pid=9944 parent=16080 stopped exitcode=-SIGTERM> False
Process exit code: -15   

### Advantages
- Allows control over process lifecycle  
- Can stop unnecessary or long-running tasks  
- Useful in error handling  

### Limitations
- Termination is abrupt (no cleanup)  
- May leave resources in inconsistent state  
- Should be used carefully  

**************************************************************************************************

## Process Spawning in Multiprocessing
Multiprocessing allows creation of multiple processes. A process can be spawned by assigning a target function and passing arguments to it.

### Main Concept
- Each process runs a function independently  
- Arguments can be passed to processes  
- `start()` begins execution  
- `join()` ensures synchronization  

### Code Interpretation
*Importing Module*
- multiprocessing => used to create processes  

*Function Definition*
def myFunc(i):
- Function executed by each process  
- Takes argument `i`  

print('calling myFunc...')
- Displays process identifier  

for j in range(0, i):
    print(j)
- Prints values based on input `i`  

*Main Execution Block*
if __name__ == '__main__':
- Required for multiprocessing  
- Prevents recursive execution  

*Process Creation*
for i in range(6):
- Creates 6 processes  

*Passing Arguments*
args=(i,)
- Passes value of `i` to function  
- Tuple syntax required  

*Starting Process*
process.start()
- Begins execution of process  

*Process Synchronization*
process.join()
- Main waits for process completion  

*Program Flow*
- Loop runs from 0 to 5  
- Each iteration:
  - Process is created  
  - Function executes with argument `i`  
  - Prints output  
  - Main waits before next process  
- Execution is sequential  

*Output Behavior*
calling myFunc from process n°: 0  

calling myFunc from process n°: 1  
output from myFunc is :0  

calling myFunc from process n°: 2  
output from myFunc is :0  
output from myFunc is :1  
...

### Advantages
- Easy to pass arguments to processes  
- Simple process creation  
- Useful for modular tasks  

### Limitations
- Sequential execution due to join() inside loop  
- No parallel speedup  
- Process creation overhead  

**************************************************************************************************

## Process Spawning using Namespace (Separate Module)
This example demonstrates process creation where the target function is defined in a **separate file (namespace/module)** instead of the same file.

### Main Difference from Previous Approach
- Function is **not defined in the same file**
- Imported using:
  from myFunc import myFunc  
- Introduces **modular programming**

### Namespace Concept
- A **namespace** refers to a separate Python file/module  
- Helps organize code into different files  
- Improves readability and maintainability  

### Code Change Highlight
Previous approach:
def myFunc(i):
    ...

New approach:
from myFunc import myFunc
...

- Logic is moved to another file (`myFunc.py`)  
- Main file only handles process creation  

### Execution Behavior
- No change in execution  
- Processes still run the same function  
- Output remains identical  

### Advantages of Namespace Approach
- Better code organization  
- Reusability of functions  
- Cleaner project structure   

**************************************************************************************************

## Process Pool in Multiprocessing
A **Process Pool** is used to manage multiple worker processes efficiently. It distributes tasks across a fixed number of processes and executes them in parallel.
- Pool creates multiple worker processes  
- Tasks are distributed automatically  
- Enables parallel execution    

### Code Interpretation

*Function Definition*
def function_square(data):
- Returns square of input  

*Input Data*
inputs = list(range(0,100))
- Generates numbers from 0 to 99  

*Creating Pool*
pool = multiprocessing.Pool(processes=4)
- Creates 4 worker processes  

*Parallel Execution*
pool.map(function_square, inputs)
- Distributes tasks across processes  
- Executes function in parallel  

*Closing Pool*
pool.close()
- Stops accepting new tasks  

pool.join()
- Waits for all processes to finish  

*Output*
print(pool_outputs)
- Displays computed results  

### Key Difference from Previous Methods
- No manual process creation  
- Automatic task distribution  
- True parallel execution  

### Output 
// `Square of (0-99)`
Pool    : [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1369, 1444, 1521, 1600, 1681, 1764, 1849, 1936, 2025, 2116, 2209, 2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225, 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724, 6889, 7056, 7225, 7396, 7569, 7744, 7921, 8100, 8281, 8464, 8649, 8836, 9025, 9216, 9409, 9604, 9801] 

### Advantages
- Efficient use of CPU cores  
- Simple parallel processing  
- Reduces manual process handling  

### Limitations
- Less control over individual processes  
- Overhead for small tasks  

**************************************************************************************************

## Background (Daemon) vs Non-Background Processes
This example demonstrates the difference between **daemon (background)** and **non-daemon (foreground)** processes in multiprocessing.

### Main Concept
- A **daemon process** runs in the background  
- A **non-daemon process** runs normally (foreground)  
- Daemon processes are **terminated automatically** when the main program exits  

### Code Interpretation
*Process Creation*
background_process = multiprocessing.Process(name='background_process', target=foo)  
NO_background_process = multiprocessing.Process(name='NO_background_process', target=foo)  
- Two processes are created  
- Both execute the same function `foo()`  

*Daemon Setting*
**Case 1 (First Code):**
background_process.daemon = False  
NO_background_process.daemon = False  
- Both are **non-daemon processes**  
- Both complete execution fully  

**Case 2 (Second Code):**
background_process.daemon = True  
NO_background_process.daemon = False  
- One process is **daemon (background)**  
- One process is **non-daemon (foreground)**  

*Execution Behavior*
- Both processes start using `.start()`  
- Function behavior depends on process name  
- Each prints numbers and exits  

### Key Difference
**Non-Daemon Process**
- Runs normally 
- Always completes 
- Independent

**Daemon Process**
- Runs in background
- May terminate early
- Depends on main process
- Ends when main ends 

### Important Behavior
- In **Case 1**:
  - Both processes finish execution  
  - Output is complete  

- In **Case 2**:
  - Daemon process may **stop abruptly**  
  - Non-daemon process completes normally  

### Output Insight
- Daemon process may not print all values  
- "Exiting background_process" may not appear  
- Non-daemon process prints full output  

### Advantages
**Daemon Process**
- Useful for background tasks  
- Automatically cleaned up  

**Non-Daemon Process**
- Reliable execution  
- Ensures task completion  

### Limitations
**Daemon Process**
- No guarantee of completion  
- Can terminate abruptly  

**Non-Daemon Process**
- Must be managed manually  
- Can delay program termination  

### Conclusion
- `daemon = True`: background process (auto-terminated)  
- `daemon = False`: normal process (runs to completion)  
- Choice depends on whether task must complete or not  

**************************************************************************************************

## Barrier Synchronization in Multiprocessing
A **Barrier** is a synchronization mechanism that forces a group of processes to wait until a specified number of processes reach a certain point before continuing execution.
- Barrier blocks processes until required number arrive  
- Ensures synchronized execution  
- Lock is used to prevent mixed (interleaved) output  

### Code Interpretation
*Importing Modules*
- Barrier => synchronization mechanism  
- Lock => ensures orderly printing  
- Process => process creation  

*Barrier Initialization*
synchronizer = Barrier(2)
- Barrier waits for **2 processes**  

*Lock Initialization*
serializer = Lock()
- Ensures only one process prints at a time  

**With Barrier**
def test_with_barrier(synchronizer, serializer):

synchronizer.wait()
- Process waits at barrier  
- Execution pauses until 2 processes arrive  

now = time()
with serializer:
    print(...)
- Lock ensures clean output  

**Without Barrier**
def test_without_barrier():

now = time()
print(...)
- No waiting  
- Processes execute immediately  

### Process Creation
Process(name='p1', target=test_with_barrier, args=(...)).start()  
Process(name='p2', target=test_with_barrier, args=(...)).start()  

Process(name='p3', target=test_without_barrier).start()  
Process(name='p4', target=test_without_barrier).start()  


### Output Behavior
**p1 & p2 (with barrier):**
process p1 - test_with_barrier ----> 2026-04-17 19:38:05.296893
process p2 - test_with_barrier ----> 2026-04-17 19:38:05.296945
- Wait for each other  
- Print almost same timestamp  

**p3 & p4 (without barrier):**
process p4 - test_without_barrier ----> 2026-04-17 19:38:05.198806
process p3 - test_without_barrier ----> 2026-04-17 19:38:05.278883
- Execute immediately  
- Print different timestamps  

### Advantages of Barrier
- Ensures synchronized execution  
- Useful for parallel stages/checkpoints  
- Prevents premature execution  

### Limitations
- All processes must reach barrier  
- Can cause delays  
- Risk of deadlock if one process fails   

**************************************************************************************************

## Communication using Queue in Multiprocessing 
This example demonstrates communication between processes using a **Queue** in multiprocessing. One process produces data, while another consumes it.

### Main Concept
- Queue is used to share data between processes  
- Producer adds items to queue  
- Consumer removes items from queue  
- Enables safe communication between processes  

### Code Interpretation
*Importing Modules*
- multiprocessing => process creation & queue  
- random => generate data  
- time => simulate delay  

*Queue Creation*
queue = multiprocessing.Queue()
- Shared data structure between processes  

**Producer Process**
class producer(multiprocessing.Process):

self.queue.put(item)
- Adds item to queue  

print("item appended...")
- Displays produced item  

self.queue.qsize()
- Shows current queue size  

**Consumer Process**
class consumer(multiprocessing.Process):

self.queue.get()
- Removes item from queue  

self.queue.empty()
- Checks if queue is empty  

### Execution Flow
- Producer generates random items  
- Adds them to queue  
- Consumer reads items from queue  
- Stops when queue becomes empty  

### Key Insights
- Queue ensures **safe data sharing**  
- No need for locks (internally synchronized)  
- Supports FIFO (First In First Out)  

### Output Behavior
Process Producer : item 87 appended to queue producer-1
The size of queue is 1
Process Producer : item 243 appended to queue producer-1
The size of queue is 2
Process Producer : item 129 appended to queue producer-1
Process Consumer : item 87 popped from by consumer-2 
The size of queue is 2 
...

### Advantages
- Safe communication between processes  
- No shared memory issues  
- Simple producer-consumer model  

### Limitations
- Slight overhead due to queue management  
- Blocking behavior if not handled properly  
- Consumer may exit early if queue check is not synchronized  

**************************************************************************************************

## Communication using Pipe in Multiprocessing 
This example demonstrates communication between processes using **Pipes**. Data flows from one process to another through pipe connections.

### Main Concept
- Pipe is used for communication between two processes  
- Data is sent using `send()` and received using `recv()`  
- Supports one-to-one communication  
- Can be unidirectional or bidirectional  

### Code Interpretation
*Importing Module*
- multiprocessing => process and pipe creation  

*Pipe Creation*
pipe_1 = multiprocessing.Pipe(True)  
pipe_2 = multiprocessing.Pipe(True)  
- Creates two communication channels  
- `True` means bidirectional pipe  

**Process 1 (Producer)**
def create_items(pipe):

output_pipe.send(item)
- Sends numbers (0–9) into pipe  

output_pipe.close()
- Closes pipe after sending  

**Process 2 (Processor)**
def multiply_items(pipe_1, pipe_2):

input_pipe.recv()
- Receives data from first pipe  

output_pipe.send(item * item)
- Sends squared result to second pipe  

**Main Process (Receiver)**
pipe_2[1].recv()
- Receives processed data  

print(...)
- Displays squared values  

### Key Program Flow
Process 1 sends numbers to Pipe 1  
Process 2 reads from Pipe 1, squares and sends to Pipe 2  
Main reads from Pipe 2 and prints output  

### Key Difference from Queue

A **Pipe** is used for communication between two processes through a direct connection. It is generally simpler and is best suited for one-to-one communication where data flows between a fixed pair of processes.

In contrast, a **Queue** is a shared data structure that allows communication between multiple processes. It is more flexible and supports many-to-many communication, where multiple producers and consumers can interact safely..

### Output Behavior
0  
1  
4  
9  
16  
...  

### Advantages
- Fast communication  
- Simple implementation  
- Direct process-to-process transfer  

### Limitations
- Limited to fewer processes  
- Not ideal for complex communication  
- Requires careful handling of pipe ends  

**************************************************************************************************