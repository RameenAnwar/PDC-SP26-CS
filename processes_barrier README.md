Multiprocessing with Barrier and Lock 🔒

How It Works

1. `test_with_barrier`

* Processes wait at a Barrier
* Both processes continue only when all reach the barrier
* A Lock ensures clean, one-by-one printing

Result: Synchronized execution with ordered output

2. `test_without_barrier`

* Processes run independently
* No waiting or synchronization
* Output may appear in random order

Example Output

```id="out889"
process p3 - test_without_barrier ----> 2026-04-21 10:00:01
process p4 - test_without_barrier ----> 2026-04-21 10:00:02

process p1 - test_with_barrier ----> 2026-04-21 10:00:03
process p2 - test_with_barrier ----> 2026-04-21 10:00:03
```

How to Run

bash id="run909"
python main.py


Important Notes

* `Barrier(n)` blocks processes until n processes reach it
* `Lock()` ensures only one process prints at a time
* Without synchronization, outputs can be unordered
* Useful in tasks requiring coordination between processes

What You Learn

* Process synchronization using Barrier
* Preventing race conditions using Lock
* Difference between synchronized and unsynchronized execution
