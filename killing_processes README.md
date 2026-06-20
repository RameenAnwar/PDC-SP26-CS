 Multiprocessing Process Lifecycle in Python 

Overview

This program demonstrates how to create, start, terminate, and manage a process using Python’s `multiprocessing` module.

A separate process runs a function, while the main program monitors and controls its execution.

How It Works

Function (`foo`)

* Prints "Starting function"`
* Loops from 0 to 9
* Prints each number with a 1-second delay
* Prints `"Finished function"` at the end

 Main Process Flow

1. Create Process

   * A new process is created with target function `foo`

2. Before Start

   * Checks if the process is alive (`is_alive()` → False)

3. Start Process

   * start() begins execution in a separate process

4. Terminate Process

   * terminate() stops the process before it finishes

5. Join Process

   * join() waits for the process to fully stop


Example Output

id= out55
Process before execution: <Process ...> False
Process running: <Process ...> True
Process terminated: <Process ...> False
Process joined: <Process ...> False
Process exit code: -SIGTERM

Important Notes

* terminate() forcefully stops the process (it may not complete its task)
* is_alive() helps track process status
* join() ensures the main program waits for the process
* Exit code:

  * `0` → normal completion
  * Negative value → terminated forcefully
