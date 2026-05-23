**************************************************************************************************
**Chapter: 05       Name: Javaria Owais        Roll Number: 23FA-017-CS**
**************************************************************************************************

## Asynchronous Programming with Futures
Asynchronous programming allows multiple tasks to run concurrently without blocking the entire program. In Python, the `asyncio` module is used to create asynchronous tasks called coroutines.
In async programs:
- Tasks run concurrently  
- Coroutines can pause and resume execution  
- Futures store results of asynchronous operations  
- Event loop manages task execution  

### Key Concepts
**Coroutine**
A special function that can pause and resume execution using `await`.

**Future**
An object that stores a result which will become available later.

**Event Loop**
The core component of `asyncio` that schedules and runs asynchronous tasks.

**Callback**
A function executed automatically when another task completes.

### Code Interpretation
*Importing Modules*
- `asyncio` => asynchronous programming support  
- `sys` => reads command-line arguments  

*First Coroutine*
async def first_coroutine(future, num):
- Defines an asynchronous coroutine  

count = 0
for i in range(1, num + 1):
    count += 1
- Counts iterations from 1 to `num`  

await asyncio.sleep(4)
- Pauses coroutine for 4 seconds asynchronously  
- Other tasks can run during this time  

future.set_result(...)
- Stores result inside Future object  

*Second Coroutine*
async def second_coroutine(future, num):
- Another asynchronous coroutine  

count *= i
- Calculates factorial  

await asyncio.sleep(4)
- Non-blocking asynchronous delay  

*Callback Function*
def got_result(future):
    print(future.result())
- Called automatically when Future completes  
- Prints stored result  

*Reading Input*
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])
- Reads numbers from terminal  
- Example:
    python asyncio_and_futures.py 5 4

*Creating Futures*
future1 = asyncio.Future()
future2 = asyncio.Future()
- Creates placeholder objects for future results  

*Creating Tasks*
tasks = [
    first_coroutine(future1, num1),
    second_coroutine(future2, num2)
]
- Creates asynchronous tasks  

*Adding Callbacks*
future1.add_done_callback(got_result)
future2.add_done_callback(got_result)
- Executes callback automatically after completion  

*Running Tasks*
await asyncio.gather(*tasks)
- Runs all tasks concurrently  

*Program Start*
asyncio.run(main())
- Starts event loop and executes async program  

### Program Execution
Run using: python asyncio_and_futures.py 5 4

### Output Behavior
First coroutine (sum of N ints) result = 5
Second coroutine (factorial) result = 24
- Both coroutines run concurrently  
- Total execution time is reduced because tasks overlap  

### Advantages of Async Programming
- Efficient for waiting operations  
- Improves responsiveness  
- Allows concurrent task execution  
- Reduces idle CPU time  

### Limitations
- More complex than synchronous programming  
- Debugging can be difficult  
- Not ideal for heavy CPU-bound tasks  

**************************************************************************************************

## Async Coroutine (Finite State Machine)
This program demonstrates asynchronous programming using `asyncio` coroutines by simulating a **Finite State Machine (FSM)**.
A Finite State Machine consists of different states and transitions between those states based on conditions.

### Main Concept
- Program starts from an initial state  
- Random values determine state transitions  
- Coroutines move between states asynchronously  
- Execution stops when End State is reached  

### Code Interpretation
*Importing Modules*
- `asyncio` => asynchronous programming support  
- `randint` => generates random transition values  

*Start State*
async def start_state():
- First state of the program  

input_value = randint(0, 1)
- Randomly selects `0` or `1`  

await asyncio.sleep(1)
- Asynchronous delay for 1 second  

*Transition Logic*
if input_value == 0:
    result = await state2(input_value)
else:
    result = await state1(input_value)
- Program transitions to another state based on random value  

*State1 Coroutine*
async def state1(transition_value):
- Represents State 1 of FSM  

print('...evaluating...')
- Simulates decision making  

if input_value == 0:
    result = await state3(input_value)
else:
    result = await state2(input_value)
- State1 can move to State2 or State3  

*State2 Coroutine*
async def state2(transition_value):
- Represents State2  

- Can transition to:
  - State1
  - State3  

*State3 Coroutine*
async def state3(transition_value):
- Represents State3  

- Can transition to:
  - State1
  - End State  

*End State*
async def end_state(transition_value):
- Final stopping state  

print('...stop computation...')
- Ends execution  

*Running the Program*
asyncio.run(start_state())
- Starts event loop and executes coroutines  

### Program Flow
- Start State begins execution  
- Random transition value is generated  
- Program moves between states  
- States continue calling other states  
- Eventually End State is reached  
- Program stops  

### Output Behavior (Example)
Finite State Machine simulation with Asyncio Coroutine
Start State called

...evaluating...
...evaluating...
...evaluating...
...evaluating...
...evaluating...
...evaluating...
...evaluating...
...evaluating...
...evaluating...
...evaluating...
...evaluating...
...stop computation...
Resume of the Transition : 
Start State calling State 2 with transition value = 0
State 2 calling State 1 with transition value = 0
State 1 calling State 2 with transition value = 1
State 2 calling State 1 with transition value = 0
State 1 calling State 2 with transition value = 1
State 2 calling State 1 with transition value = 0
State 1 calling State 2 with transition value = 1
State 2 calling State 3 with transition value = 1
State 3 calling State 1 with transition value = 0
State 1 calling State 2 with transition value = 1
State 2 calling State 3 with transition value = 1
State 3 calling End State with transition value = 1

### Advantages of Async Coroutines
- Efficient task execution  
- Non-blocking asynchronous behavior  
- Better resource utilization  
- Useful for event-driven systems  

### Limitations
- More difficult to debug  
- Complex program flow  
- Not ideal for CPU-intensive tasks  

**************************************************************************************************

## Asynchronous Task Manipulation 
This program demonstrates asynchronous programming using `asyncio.Task` to execute multiple mathematical functions concurrently.

The program runs:
- Factorial calculation  
- Fibonacci sequence calculation  
- Binomial coefficient calculation  

simultaneously using asynchronous tasks.

### Main Concept
- Multiple tasks run concurrently  
- Tasks pause using `await`  
- Event loop manages task scheduling  
- Improves efficiency through asynchronous execution  


### Code Interpretation
*Importing Module*
- `asyncio` => asynchronous programming support  

*Factorial Coroutine*
async def factorial(number):
- Calculates factorial of a number  

fact *= i
- Multiplies numbers iteratively  
- Example: 5! = 5 × 4 × 3 × 2 × 1 = 120

await asyncio.sleep(1)
- Non-blocking asynchronous delay  

*Fibonacci Coroutine*
async def fibonacci(number):
- Computes Fibonacci sequence  

a, b = b, a + b
- Updates Fibonacci values  
- Example: 0, 1, 1, 2, 3, 5, 8...

*Binomial Coefficient Coroutine*
async def binomial_coefficient(n, k):
- Calculates binomial coefficient  
- Formula: n! / (k! × (n-k)!)

result = result * (n - i + 1) / i
- Computes coefficient iteratively  

*Creating Tasks*
asyncio.create_task(...)
- Converts coroutines into asynchronous tasks  

task_list = [
    asyncio.create_task(factorial(10)),
    asyncio.create_task(fibonacci(10)),
    asyncio.create_task(binomial_coefficient(20, 10))
]
- Creates three concurrent tasks  

*Running Tasks*
await asyncio.wait(task_list)
- Executes all tasks concurrently  

*Starting Event Loop*
asyncio.run(main())
- Starts asynchronous execution  

### Program Flow
- Event loop starts  
- Three asynchronous tasks are created  
- Tasks execute concurrently  
- Each task pauses during sleep  
- Other tasks continue execution meanwhile  
- Final results are printed  

### Output Behavior (Example)
Asyncio.Task: Compute factorial(2)
Asyncio.Task: Compute fibonacci(0)
Asyncio.Task: Compute binomial_coefficient(1)

Asyncio.Task: Compute factorial(3)
Asyncio.Task: Compute fibonacci(1)
...

Asyncio.Task - factorial(10) = 3628800
Asyncio.Task - fibonacci(10) = 55
Asyncio.Task - binomial_coefficient(20, 10) = 184756

- Output order may vary because tasks execute concurrently  

### Advantages of Async Tasks
- Efficient execution of concurrent tasks  
- Better responsiveness  
- Non-blocking behavior  
- Improved resource utilization  

### Limitations
- More complex than synchronous programming  
- Harder debugging and tracing  
- Not ideal for CPU-heavy computations  

**************************************************************************************************

## Async Event Loop
This program demonstrates the working of the `asyncio` event loop by scheduling and executing multiple asynchronous tasks repeatedly.
Three tasks (`task_A`, `task_B`, and `task_C`) execute in a cyclic manner until a specified time limit is reached.

### Main Concept
- Event loop manages asynchronous execution  
- Tasks are scheduled dynamically using: `loop.call_later()` 
- Tasks execute repeatedly in sequence  
- Execution stops after time limit expires  

### Code Interpretation
*Importing Modules*
- `asyncio` => asynchronous programming support  
- `random` => generates random delays  

*Task A*
async def task_A(end_time):
- First asynchronous task  

await asyncio.sleep(random.randint(0, 5))
- Non-blocking random delay  

loop.call_later(...)
- Schedules another task after delay  

asyncio.create_task(task_B(end_time))
- Creates and schedules Task B  

*Task B*
async def task_B(end_time):
- Second asynchronous task  
- Schedules `task_C` after execution  

*Task C*
async def task_C(end_time):
- Third asynchronous task  
- Schedules `task_A` after execution  

*Time Check*
if (loop.time() + 1.0) < end_time:
- Checks whether total execution time is exceeded  

loop.stop()
- Stops event loop after timeout  

*Creating Event Loop*
loop = asyncio.get_running_loop()
- Gets currently running event loop  

*Setting End Time*
end_loop = loop.time() + 60
- Program runs for 60 seconds  

*Starting First Task*
loop.call_soon(...)
- Schedules first task immediately  

*Running Program*
asyncio.run(main())
- Starts asynchronous execution  

### Program Flow
- Event loop starts  
- `task_A` executes first  
- `task_A` schedules `task_B`  
- `task_B` schedules `task_C`  
- `task_C` schedules `task_A` again  
- Cycle continues until time limit expires  
- Event loop stops  

### Output Behavior
task_A called
task_B called
task_C called
task_A called
task_B called
...
- Tasks execute repeatedly in cyclic order  
- Random delays change execution timing  

### Advantages of Async Event Loop
- Efficient asynchronous execution  
- Non-blocking task scheduling  
- Handles multiple tasks efficiently  
- Improves responsiveness  

### Limitations
- Complex flow control  
- Difficult debugging  
- Not suitable for CPU-intensive tasks  

**************************************************************************************************

## Concurrent Future Pooling
This program demonstrates concurrent execution using:
- Sequential execution  
- Thread Pool Executor  
- Process Pool Executor  
The program compares their execution times for CPU-intensive tasks.

### Main Concept
- Sequential execution runs tasks one by one  
- Thread pool uses multiple threads  
- Process pool uses multiple processes  
- Execution times are compared  

**Thread Pool** A collection of worker threads executing tasks concurrently.

**Process Pool** A collection of worker processes executing tasks in parallel.

**CPU-bound Task** A task requiring heavy processor computation.

**Concurrent Execution** Multiple tasks progress during overlapping time periods.

### Code Interpretation
*Importing Modules*
- `concurrent.futures` => thread and process pooling  
- `time` => measures execution time  

*Creating Number List*
number_list = list(range(1, 11))
- Creates numbers from 1 to 10  

*Count Function*
def count(number):
- Simulates CPU-intensive computation  

for i in range(0,10000000):
    i += 1
- Performs heavy looping operation  

return i * number
- Returns computed value  

*Evaluate Function*
def evaluate(item):
- Calls `count()` function  
- Prints result  

**Sequential Execution**
for item in number_list:
    evaluate(item)
- Executes tasks one after another  

time.perf_counter()
- Measures total execution time  

**Thread Pool Execution**
ThreadPoolExecutor(max_workers=5)
- Creates pool of 5 threads  

executor.submit(evaluate, item)
- Assigns task to thread  
- Suitable for I/O-bound tasks  

**Process Pool Execution**
ProcessPoolExecutor(max_workers=5)
- Creates pool of 5 processes  
- Suitable for CPU-intensive tasks  
- Provides true parallel execution  

### Program Flow
- Number list is created  
- Sequential execution runs first  
- Thread pool executes tasks concurrently  
- Process pool executes tasks in parallel  
- Execution times are displayed  

### Output Behavior 
Item 1, result 9999999
Item 2, result 19999998
...
Sequential Execution in 6.796286800177768 seconds
Thread Pool Execution in 6.73171509988606 seconds
Process Pool Execution in 3.8842391001526266 seconds

> The results show that Process Pool execution was significantly faster for this CPU-intensive task, while Thread Pool provided little improvement over Sequential execution due to Python’s GIL limitation.

### Advantages
- Improves performance  
- Efficient task management  
- Simplifies concurrent programming  
- Process pools utilize multiple CPU cores  

### Limitations
- Thread pools affected by GIL  
- Process creation has overhead  
- More complex debugging  

**************************************************************************************************