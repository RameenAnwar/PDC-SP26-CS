Asyncio Event Loop Scheduling Example:
A minimal Python script demonstrating how to schedule and execute standard functions cyclically on an `asyncio` event loop using `call_soon` and `call_later`.

Prerequisites:
* Python version: 3.x

How to Run
Run the script from your terminal:

```bash
python script_name.py
```

What it Does:
This script sets up a continuous, circular chain of tasks (A → B → C → A) that pass control to one another until a 60-second timer expires:

1. Initialization: It fetches the current event loop and calculates an `end_time` which is 60 seconds in the future, based on the loop's internal clock (`loop.time()`).
2. Kicking it off: `loop.call_soon(task_A, ...)` schedules `task_A` to run as soon as the event loop starts. `loop.run_forever()` then starts the loop.
3. The Cycle: * A task executes, printing its name.
* It pauses for a random interval between 0 and 5 seconds using `time.sleep()`.
* It checks if there is still at least 1 second left before `end_time`.
* If there is time left, it schedules the *next* task in the chain to run exactly 1 second from now using `loop.call_later(1, next_task, ...)`.
4. Termination: If the `end_time` has been reached, the task calls `loop.stop()`, breaking the cycle and allowing the script to finish and exit cleanly.

Important Code Observations:
If you are using this as a learning tool for `asyncio`, keep these details in mind:

* Blocking the Loop: This script uses standard functions (`def`) and `time.sleep()`. Because these functions run synchronously on the event loop's main thread, `time.sleep()` will completely block the event loop. While the script is sleeping, the loop cannot process any other events or timers. In a real-world asynchronous application, you would use coroutines (`async def`) and non-blocking sleeps (`await asyncio.sleep()`).
* `loop.time()` vs `time.time()`: The script correctly uses `loop.time()` for scheduling. The event loop uses its own internal monotonic clock, which is required for `call_later` and `call_at` to function accurately.

Example Output:
The output will continuously print the task sequence, pausing randomly between each line, until the 60 seconds are up:

```text
task_A called
task_B called 
task_C called
task_A called
task_B called 
task_C called
...

```
