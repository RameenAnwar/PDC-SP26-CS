Multiprocessing with External Function Module 

How It Works:
1.myFunc.py:
* Contains the function `myFunc(i)`
* Prints:
  * Process number (`i`)
  * A loop of values from `0` to `i-1'  
2.main.py:
* Imports `myFunc` from `myFunc.py`
* Creates processes in a loop (0 → 5)
* Each process runs `myFunc(i)`
* Uses `join()` to wait for each process
Execution is sequential because of `join()` inside the loop

Example Output:

id="out777"
calling myFunc from process n°: 2
output from myFunc is :0
output from myFunc is :1
...

How to Run:

```bash id="run888"
python main.py
```

Important Notes:

* Functions used in multiprocessing must be importable (not nested)
* `start()` runs the process
* `join()` waits for completion
* Keeping `join()` inside loop makes execution sequential
Move `join()` outside loop to run processes in parallel
