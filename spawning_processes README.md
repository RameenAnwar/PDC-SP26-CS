Spawning Processes in Python (Multiprocessing) 

How It Works:

Function (`myFunc(i)`)
* Takes an integer `i`
* Prints the process number
* Loops from `0` to `i-1`
* Prints values inside the loop

Main Program:

* A loop runs from `0` to `5`
* For each value:

  1. A new process is created
  2. The function `myFunc(i)` is executed
  3. `join()` waits for the process to finish before starting the next

This makes execution sequential, not parallel.

Example Output:

id="out123"
calling myFunc from process n°: 3
output from myFunc is :0
output from myFunc is :1
output from myFunc is :2
...

How to Run:

```bash id="run123"
python main.py
```

Important Notes:

* `Process()` creates a new process
* `start()` begins execution
* `join()` waits for completion
* Because of `join()` inside the loop, processes run one by one
Remove `join()` inside the loop to run processes in parallel

What You Learn:

* How to spawn processes
* Passing arguments to processes
* Difference between sequential and parallel execution
