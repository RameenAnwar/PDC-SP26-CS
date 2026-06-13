
CHAPTER 5

## How To Execute : Run the program using "python filename.py" (you need to have python installed for this, replace filename with the name you used when saving it on your device)

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: asyncio_event_loop.py

## Description
This script showcases the absolute foundations of asynchronous coordination using Python's event loop. 
Instead of utilizing multiple threads or processes, it spins up a single-threaded loop that orchestrates three distinct tasks (A, B, and C) by scheduling them dynamically using timed callbacks.

## When to Execute
Execute this to study asynchronous event scheduling or to verify how a single-threaded coordination loop schedules delayed tasks dynamically without multi-threading overhead.

## What We Learned
- Accessing and managing a low-level asynchronous runtime engine using asyncio.get_event_loop().
- Bootstrapping a process with loop.call_soon() and setting up future actions down the timeline using loop.call_later().
- Keeping an engine active using loop.run_forever() and cleanly shutting it down via loop.stop() and loop.close().

## Advantages
- Incredibly lightweight because it eliminates the massive system overhead of spinning up or juggling multiple operating system threads.
- Excellent for building network-heavy components, like chat routers or data scrapers, where tasks spend most of their time waiting for a network response.
- Bypasses race conditions and resource deadlocks completely since your core coordination logic is guaranteed to run on a single thread.

## Disadvantages
- A single bad line of code utilizing a blocking function like time.sleep() will instantly freeze the entire application and crash your schedule.
- The program cannot distribute tasks across multiple CPU cores natively, making it completely useless for heavy mathematical data crunching.
- The manual callback chaining model can quickly morph your code structure into a confusing, unreadable mess if your task loops get deep.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: asyncio_and_futures.py

## Description
This script handles asynchronous task management by utilizing Future objects to track background execution. 
It kicks off two coroutines—one calculating a summation and the other a factorial—and links them to Futures that automatically capture results and trigger callbacks the millisecond they finish.

## When to Execute
Run using "python asyncio_and_futures.py 1000 15" (You must pass two  integer values with space between them as command-line arguments to feed values to the summation and factorial calculations).
Execute this pattern when designing event-driven systems that require non-blocking, asynchronous result tracking and immediate callback execution upon task completion.

## What We Learned
- Allocating explicit placeholder containers for asynchronous results using the asyncio.Future class.
- Setting execution milestones inside coroutines by passing data backward using future.set_result().
- Binding decoupled handler functions to async events using future.add_done_callback() to react instantly to completions.

## Advantages
- Completely decouples your heavy processing code from your reporting code, making the application components highly modular.
- Eliminates the need to write active polling routines or infinite loops just to check if a background task has finished its calculation.
- Streamlines exception tracking, as a Future can store runtime failures safely and pass them to error handlers rather than crashing the loop.

## Disadvantages
- Uses deprecated decorator syntaxes (@asyncio.coroutine and yield from) which will completely fail on modern Python runtimes without updates.
- Debugging can turn into a nightmare because stack traces are broken up across the event loop timeline, obscuring where an error originated.
- If a coroutine hangs or fails to call set_result(), the associated Future will wait indefinitely, leading to silent memory leaks.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: asyncio_task_manipulation.py

## Description
This program runs higher-level asynchronous task scheduling by wrapping coroutines inside formal Asyncio Task objects. 
It fires up three mathematical routines—a factorial engine, a Fibonacci counter, and a binomial coefficient calculator—and steps through them concurrently on a single thread using non-blocking delays.

## When to Execute
Execute this routine when building application dashboards, concurrent data parsers, or macro-workflows where multiple unrelated workflows need to make progress simultaneously without blocking each other.

## What We Learned
- Promoting raw coroutines into standalone execution nodes using the asyncio.Task interface.
- Pausing execution context safely to let other tasks run by yielding control via asyncio.sleep().
- Bundling collections of tasks together and awaiting their group completion via asyncio.wait().

## Advantages
- Allows you to track, monitor, or cancel active asynchronous tasks on the fly while the main loop continues running smoothly.
- Gives a highly readable layout of true concurrent execution, making it obvious when and how tasks yield control to their peers.
- Simplifies bulk execution operations by accepting standard Python lists of tasks and running them all through a single gatekeeper call.

## Disadvantages
- Like other legacy scripts, it relies on the old @asyncio.coroutine decorators, which requires refactoring to modern async def syntax for production use.
- Provides no built-in mechanism to balance task priority, meaning a long task with short sleep intervals can starve out other tasks in the array.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: asyncio_coroutine.py

## Description
This script simulates a random finite state machine by linking multiple coroutines together into an asynchronous chain. 
The code passes control from a start state through various intermediary state steps based on random rolls, demonstrating how asynchronous code can jump around complex logic smoothly.

## When to Execute
Execute this script to analyze asynchronous control flow, observe state transition mechanics, or test how non-blocking yield statements pass execution context between functions.

## What We Learned
- Constructing highly fluid, interconnected program paths by chaining multiple coroutines together.
- Using yield from statements to pause a state process and wait for a downstream state routine to resolve and pass back its string data.
- Observing how execution context hops back and forth between different functions while keeping all state variables perfectly intact.

## Advantages
- Perfect for modeling asynchronous behaviors like network protocols, gaming logic bots etc.
- Retains local variables and execution history within each state, which removes the need to build a massive global state-tracking object.
- Highly modular design allows you to add or modify individual states without breaking or restructuring the rest of the machine.

## Disadvantages
- The code uses standard blocking time.sleep(1) inside its loops, which breaks async best practices and completely freezes the runtime thread during evaluation.
- High risk of creating infinite execution loops or stack overflows if states roll numbers that bounce control back and forth indefinitely.
- Hard to trace visually or conceptually since the execution path changes completely on every run due to the randomized transitions.

--------------------------------------------------------------------------------------------------------------------------------------------------

File Name: concurrent_futures_pooling.py

## Description
This script provides a direct, head-to-head performance comparison between running a CPU-heavy math routine sequentially versus using parallel pools. 
It demonstrates how to spin up a ThreadPoolExecutor and a ProcessPoolExecutor from Python’s concurrent.futures module to process a list of numbers concurrently.

## When to Execute
Execute this script to baseline performance metrics when evaluating whether a computational task is bottlenecked by the CPU or I/O, or when migrating from manual thread/process lifecycles to structured executor pools.

## What We Learned
- Spawning worker pools efficiently with the ProcessPoolExecutor and ThreadPoolExecutor context managers.
- Submitting tasks asynchronously using executor.submit() and measuring exact runtime differences against a single-threaded loop.
- Observing how Python’s Global Interpreter Lock (GIL) limits multi-threaded performance on heavy math loops, making process-based pools much faster for CPU-bound tasks.

## Advantages
- Bypasses the complex headache of manually managing process states, allocations, and worker lifecycles by wrapping them in a clean API.
- The context manager syntax safely handles thread and process cleanup behind the scenes, ensuring resources don't leak if something crashes.
- Perfect for prototyping since switching your execution strategy from threading to multi-processing requires changing only a single class name.

## Disadvantages
- Spawning a ProcessPoolExecutor comes with a  memory penalty and setup lag because the operating system has to clone entire memory spaces for every worker.
- The background workers cannot directly update or touch shared global state variables, forcing you to think about how data is serialized.
- It hides low-level tuning knobs, meaning you lose granular control over individual worker priorities or custom process-initialization routines.
