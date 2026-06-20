What This Code Does:

* One process creates numbers from 0 to 9
* Another process squares those numbers
* The main program prints the results
  
How It Works:

1. First Process (`create_items`)

   * Sends numbers (0 → 9) through a pipe

2. Second Process (`multiply_items`)

   * Receives numbers
   * Squares them (e.g., 3 → 9)
   * Sends results to another pipe

3. Main Process

   * Reads results
   * Prints them
     
Output:
0
1
4
9
16
25
36
49
64
81
End

Notes:

* Pipes are used to pass data between processes
* Always close unused pipe ends
* `EOFError` means no more data

What You Learn:

* Basic multiprocessing
* How processes communicate using pipes
* Simple parallel workflow in Python
