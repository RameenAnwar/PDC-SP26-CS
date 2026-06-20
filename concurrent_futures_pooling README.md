Concurrent Futures Pooling:
This repository contains a Python script that benchmarks three different ways to execute a CPU-bound task: sequential execution, multi-threading, and multi-processing using the `concurrent.futures` module.

Prerequisites:
You only need Python installed on your system. However, please read the "Important Code Observations" section below regarding Python versions, as this script uses a legacy timing function.

How to Run:
Run the script directly from your terminal:

bash
python script_name.py
(Replace `script_name.py` with your actual filename)

What it Does:
The code defines a `count` function that simply loops 10,000,000 times to simulate a heavy workload on the CPU. It runs this function ten times (passing in the numbers 1 through 10) using three distinct approaches:
1. Sequential Execution: Runs each task one after the other on the main thread.
2. Thread Pool Execution: Attempts to run the tasks concurrently using `ThreadPoolExecutor` with up to 5 worker threads.
3. Process Pool Execution: Runs the tasks in parallel using `ProcessPoolExecutor` with up to 5 independent worker processes.

Important Code Observations:
If you are using this as a learning tool or adapting it for a modern project, keep these crucial details in mind

Legacy Timer Function:
The script uses `time.clock()` to measure performance. This function was deprecated in Python 3.3 and completely removed in Python 3.8. If you run this on a modern version of Python, it will throw an AttributeError. To fix it, replace all instances of `time.clock()` with `time.perf_counter()`.

The Python GIL (Global Interpreter Lock):
Because the `count` function is purely mathematical and relies entirely on the CPU, you will likely see that the Thread Pool method is not much faster than Sequential execution. This is because Python's GIL prevents multiple threads from executing Python code at the exact same time. On the other hand, the Process Pool creates entirely separate Python instances, completely bypassing the GIL. You should notice the Process Pool execution is significantly faster, perfectly illustrating when to use processes over threads in Python!
