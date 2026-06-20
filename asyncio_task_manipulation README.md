Asyncio Task Manipulation:
A Python script demonstrating how to run multiple mathematical calculations concurrently using `asyncio.Task`.

Prerequisites:
* Python version: 3.4 to 3.10.

How to Run:
Run the script directly from your terminal:

```bash
python script_name.py
```

What it Does:
This script runs three separate mathematical functions at the exact same time cooperatively:
1. The Tasks: It defines three coroutines for calculating a `factorial`, a `fibonacci` sequence, and a `binomial_coefficient`.
2. Yielding Control: Inside the calculation loops of each function, there is a `yield from asyncio.sleep(1)` statement. This is the secret to the concurrency: every time a function hits this line, it pauses and voluntarily hands control back to the event loop, allowing the other math functions to take a turn doing a computation.
3. Task Wrapping: The coroutines are wrapped in `asyncio.Task()` objects and added to a list. This explicitly schedules them to run on the event loop.
4. Execution: `loop.run_until_complete(asyncio.wait(task_list))` starts the event loop and keeps it running until all three tasks have finished their math and completed.

Important Code Observations:
If you plan to adapt this code for modern projects, note the following:
* Legacy Asyncio Syntax: This script uses `@asyncio.coroutine` and `yield from`. This syntax was deprecated in Python 3.8 and removed in Python 3.11. To run this code on modern Python versions (3.11+), you must replace `@asyncio.coroutine` with `async def`, and replace `yield from asyncio.sleep(1)` with `await asyncio.sleep(1)`.
* Task Creation: In modern Python, the preferred way to create tasks is using `asyncio.create_task()` rather than directly instantiating `asyncio.Task()`.

Example Output:
Because the tasks yield control to each other during their sleep phases, you will see their output lines interleaved in the console, proving they are running simultaneously rather than one after the other:
Asyncio.Task: Compute factorial(2)
Asyncio.Task: Compute fibonacci(0)
Asyncio.Task: Compute binomial_coefficient(1)
Asyncio.Task: Compute factorial(3)
Asyncio.Task: Compute fibonacci(1)
Asyncio.Task: Compute binomial_coefficient(2)
...
Asyncio.Task - factorial(10) = 3628800
Asyncio.Task - fibonacci(10) = 55
Asyncio.Task - binomial_coefficient(20, 10) = 184756.0
'''
