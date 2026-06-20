Custom Process Class using Multiprocessing 

How It Works

Custom Class (`MyProcess`)

* Inherits from `multiprocessing.Process`
* Overrides the `run()` method
* Prints the name of the process when executed

Main Program

* A loop runs 10 times
* In each iteration:

  1. A new `MyProcess` object is created
  2. `start()` begins the process
  3. `join()` waits for it to finish before starting the next one

👉 This means processes run one after another (sequentially), not in parallel.

Example Output
id="out991"
called run method in Process-1
called run method in Process-2
called run method in Process-3
...
called run method in Process-10

Important Notes

* `run()` defines what each process will do
* `start()` triggers the `run()` method internally
* `join()` makes execution sequential (waits for each process)
* Remove `join()` inside the loop to run processes in parallel


