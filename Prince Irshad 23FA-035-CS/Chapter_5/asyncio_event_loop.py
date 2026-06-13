import asyncio
import random

# The first task in the chain.
async def task_A(end_time, loop):
    print("task_A called")
    # Pause this task for a random time between 0 and 2 seconds.
    await asyncio.sleep(random.randint(0, 2))

    # Check the current clock time. If adding 1 second is still less than the end time...
    if loop.time() + 1.0 < end_time:
        # ...then it is safe to schedule the next task (task_B) in the background.
        asyncio.create_task(task_B(end_time, loop))


# The second task in the chain.
async def task_B(end_time, loop):
    print("task_B called")
    # Pause for a random time between 0 and 2 seconds.
    await asyncio.sleep(random.randint(0, 2))

    # Check if there is still enough time left before the deadline.
    if loop.time() + 1.0 < end_time:
        # Schedule the next task (task_C) to run in the background.
        asyncio.create_task(task_C(end_time, loop))


# The third task in the chain.
async def task_C(end_time, loop):
    print("task_C called")
    # Pause for a random time between 0 and 2 seconds.
    await asyncio.sleep(random.randint(0, 2))

    # Check if there is still enough time left before the deadline.
    if loop.time() + 1.0 < end_time:
        # Schedule the first task (task_A) again to keep the cycle going!
        asyncio.create_task(task_A(end_time, loop))


# The main function that sets up the time limit and starts the cycle.
async def main():
    # Get the current active event loop (the manager that handles the time).
    loop = asyncio.get_running_loop()
    
    # Set a strict deadline: the exact current time plus 5 seconds.
    end_time = loop.time() + 5

    # Start the cycle by triggering task_A.
    asyncio.create_task(task_A(end_time, loop))

    # The tasks are running in the background. We need to keep the main program alive 
    # so they have time to run. We wait for 6 seconds (1 second past the deadline).
    await asyncio.sleep(6)


# Check if the user is running this file directly.
if __name__ == "__main__":
    # Start the asyncio event loop manager, run the 'main' function, and clean up at the end.
    asyncio.run(main())