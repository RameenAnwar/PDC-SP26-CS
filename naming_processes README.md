Multiprocessing with Process Names in Python 🧵

How It Works

Function (`myFunc`)
* Retrieves the current process name using:

python
  multiprocessing.current_process().name

* Prints:

  * When the process starts
  * When the process exits
* Waits for 3 seconds to simulate work

Main Program

1. Custom Named Process

   * Created with a specific name: "myFunc process"

2. Default Named Process

   * Created without specifying a name
   * Python assigns a default name like `Process-1`

3. Start Processes

   * Both processes run in parallel using `start()`

4. Wait for Completion

   * `join()` ensures the main program waits until both processes finish

Example Output

id="out778"
Starting process name = myFunc process

Starting process name = Process-1

Exiting process name = myFunc process

Exiting process name = Process-1

How to Run
bash id="run445"
python main.py

Important Notes

* Each process runs independently and in parallel
* Output order may vary due to scheduling
* `join()` is important to wait for processes to complete
* You can enable daemon mode by uncommenting:

