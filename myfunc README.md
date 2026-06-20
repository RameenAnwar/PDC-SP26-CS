Simple Function for Multiprocessing Example 

Overview

This project contains a simple Python function (`myFunc`) often used in multiprocessing examples.

The function prints:

* Which process is calling it
* A sequence of numbers based on the input value

Function Explanation

myFunc(i)

* Takes an integer `i` as input
* Prints the process number (`i`)
* Runs a loop from `0` to `i-1`
* Prints each number in the loop

Code Behavior

* If i = 3 , output will be:

  * Process number: 3
  * Loop output: 0, 1, 2

Example Output

id="ex990"
calling myFunc from process n°: 3
output from myFunc is :0
output from myFunc is :1
output from myFunc is :2

How to Use

You can use this function with multiprocessing like:

python id="use11"
import multiprocessing

processes = []
for i in range(3):
    p = multiprocessing.Process(target=myFunc, args=(i,))
    processes.append(p)
    p.start()

for p in processes:
    p.join()

Key Points

* Demonstrates basic function behavior in multiprocessing
* Each process runs independently
* Output order may vary due to parallel execution
