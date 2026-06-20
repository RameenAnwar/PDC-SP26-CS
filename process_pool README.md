Multiprocessing with Process Pool: 

How It Works:
Function (`function_square`)
* Takes a number as input
* Returns its square

Main Program:

1. Create Input Data

   * A list of numbers from `0` to `99`

2. Create Process Pool

   * `Pool(processes=4)` creates 4 worker processes

3. Distribute Work

   * `pool.map()` assigns tasks to processes
   * Each process computes squares of assigned numbers

4. Close and Join

   * `close()` stops new tasks
   * `join()` waits for all processes to finish

5. Print Output

   * Displays the list of squared numbers

Example Output:

id="out222"
Pool : [0, 1, 4, 9, 16, 25, ..., 9801]

How to Run:

bash id="run333"
python main.py

Important Notes:

* `Pool` is useful for handling multiple tasks efficiently
* `map()` distributes work automatically across processes
* Number of processes can be adjusted based on CPU cores
* Always call `close()` and `join()` to clean up resources


