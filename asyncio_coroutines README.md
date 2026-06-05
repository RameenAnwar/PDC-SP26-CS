Finite State Machine Simulation with Asyncio
A Python script that simulates a randomized Finite State Machine (FSM) using `asyncio` coroutines to represent states and handle transitions.

Prerequisites:
* Python version: 3.4 to 3.10.

How to Run:
Run the script from your terminal:

```bash
python script_name.py
```

What it Does:
This code treats individual coroutines as nodes (states) in a Finite State Machine. The program randomly traverses these states until it hits the final exit state:

1. Start State: The entry point. It randomly generates a `0` or `1`. If `0`, it transitions to State 2. If `1`, it transitions to State 1.
2. State 1: Randomly generates a `0` (goes to State 3) or a `1` (goes to State 2).
3. State 2: Randomly generates a `0` (goes to State 1) or a `1` (goes to State 3).
4. State 3: Randomly generates a `0` (loops back to State 1) or a `1` (goes to the End State).
5. End State: Stops the computation and returns the final transition trace back up the call stack.
6. The Result: As the FSM unwinds back to the start, each state appends its transition log to the final result string, printing the entire path the machine took.

Important Code Observations:
If you plan to use this script in a modern production environment, note the following:

* Legacy Asyncio Syntax: This script uses `@asyncio.coroutine` and `yield from`. This syntax was deprecated in Python 3.8 and completely removed in Python 3.11. To modernize this code, replace `@asyncio.coroutine` with `async def` and replace `yield from` with `await`.
* Blocking the Event Loop: The script uses the standard `time.sleep(1)` inside the coroutines. In a real-world asynchronous application, this is an anti-pattern because it entirely blocks the single-threaded asyncio event loop, preventing any other concurrent tasks from running. The correct asynchronous approach is to use `yield from asyncio.sleep(1)` (or `await asyncio.sleep(1)` in modern Python).

Example Output:
Because the state transitions are randomized, the output will vary every time you run it. An example path might look like this:

```text
Finite State Machine simulation with Asyncio Coroutine
Start State called

...evaluating...
...evaluating...
...evaluating...
...evaluating...
...stop computation...
Resume of the Transition : 
Start State calling State 2 with transition value = 0
State 2 calling State 1 with transition value = 0
State 1 calling State 3 with transition value = 0
State 3 calling End State with transition value = 1

```
