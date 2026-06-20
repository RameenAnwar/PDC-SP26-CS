Multiprocessing with Daemon and Non-Daemon Processes

Overview:

This project demonstrates the difference between daemon and non-daemon processes using Python’s `multiprocessing` module.

* Daemon process → runs in background and stops automatically when the main program exits
* Non-daemon process → continues running until it completes its task
  
How It Works:

Function (`foo`)

* Gets the current process name
* Prints starting message
* Runs a loop:

  * `background_process` → prints numbers *0–4*
  * `NO_background_process` → prints numbers *5–9*
* Waits for 1 second
* Prints exiting message
  
Main Program:

1. Daemon Process

   * Name: `background_process`
   * `daemon = True`
   * Runs in background

2. Non-Daemon Process

   * Name: `NO_background_process`
   * `daemon = False`
   * Runs normally

3. Start Processes

   * Both processes are started using `start()`
     
Example Output:

```id="out551"
Starting background_process

---> 0
---> 1
---> 2
---> 3
---> 4

Starting NO_background_process

---> 5
---> 6
---> 7
---> 8
---> 9

Exiting NO_background_process
The daemon process may stop early if the main program exits before it finishes.

How to Run:

```bash id="run661"
python main.py
```

Important Notes:

* Daemon processes:

  * Run in background
  * Automatically terminate when the main program ends
* Non-daemon processes:

  * Complete their execution normally
* Output order may vary due to parallel execution
* No `join()` is used, so the program may exit quickly

What You Learn:

* Difference between daemon and non-daemon processes
* Background task handling in multiprocessing
* Process behavior when the main program exits
