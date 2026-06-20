Python Asyncio Coroutines & Futures Example
A script demonstrating concurrent execution using Python's `asyncio` library, specifically showcasing coroutines, `Future` objects, and event-driven callbacks.

Prerequisites:
* Python version: 3.4 to 3.10.

Important Modernization Note: This script uses the `@asyncio.coroutine` decorator and `yield from`. This legacy syntax was deprecated in Python 3.8 and completely removed in Python 3.11. If you are running this on a modern Python environment (3.11+), it will throw an error. For modern code, it is recommended to replace these with `async def` and `await`.

How to Run:
This script requires two command-line arguments (integers) to pass to the coroutines. Run it from your terminal like this:

```bash
python script_name.py 5 6

```

What it Does:
This code runs two asynchronous tasks concurrently, rather than blocking and waiting for one to finish before starting the other:

1. Task Setup: It reads two numbers from the terminal (`num1` and `num2`) and creates two `asyncio.Future` objects. Futures act as empty placeholders for results that haven't been computed yet.
2. First Coroutine: Intended to calculate the sum of numbers up to `num1`.
* *(Code Note: There is a minor logical bug in the script here; `count += 1` just counts the iterations, effectively returning `num1`. To actually sum the integers, it should be updated to `count += i`)*.
3. Second Coroutine: Calculates the factorial of `num2` (e.g., if num2 is 4, it calculates 4 * 3 * 2 * 1).
4. Concurrency in Action: Both coroutines hit a 4-second sleep delay (`asyncio.sleep(4)`). Because they are asynchronous, they sleep *at the exact same time*. The entire script finishes in roughly 4 seconds, instead of 8.
5. Callbacks: Once the 4 seconds are up, the coroutines populate their respective Futures using `.set_result()`. This instantly triggers the `.add_done_callback(got_result)` listeners, which print the final outputs.

Example Output:
Running the script with the inputs `5` and `6`:

```bash
python script_name.py 5 6
```
Yields the following output after a 4-second pause:
```text
First coroutine (sum of N ints) result = 5
Second coroutine (factorial) result = 720
```
