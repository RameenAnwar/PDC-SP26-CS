# Import asyncio for event loop and scheduling functions
import asyncio
# Import time for time.time() and blocking sleep (not recommended, but we comment as‑is)
import time
# Import random for generating random sleep durations
import random

# Function that represents task A
def task_A(end_time, loop):
    # Print a message indicating task A has started
    print("task_A called")
    # Block the entire thread for a random time between 0 and 5 seconds
    # (This blocks the event loop – not ideal, but the original code uses it)
    time.sleep(random.randint(0, 5))
    # Check if the current loop time + 1 second is still before the end_time
    if (loop.time() + 1.0) < end_time:
        # If yes, schedule task_B to run after 1 second (non‑blocking schedule)
        loop.call_later(1, task_B, end_time, loop)
    else:
        # Otherwise stop the event loop (terminate the program)
        loop.stop()

# Function that represents task B
def task_B(end_time, loop):
    print("task_B called ")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        # Schedule task_C next
        loop.call_later(1, task_C, end_time, loop)
    else:
        loop.stop()

# Function that represents task C
def task_C(end_time, loop):
    print("task_C called")
    time.sleep(random.randint(0, 5))
    if (loop.time() + 1.0) < end_time:
        # Schedule task_A next – creating a cycle A → B → C → A → ...
        loop.call_later(1, task_A, end_time, loop)
    else:
        loop.stop()

# Get the default asyncio event loop
loop = asyncio.get_event_loop()
# Set the end time to 60 seconds from now (loop runs for 60 seconds max)
end_loop = loop.time() + 60
# Schedule task_A to run as soon as possible (at the next iteration of the event loop)
loop.call_soon(task_A, end_loop, loop)
# Run the event loop forever – will stop only when loop.stop() is called
loop.run_forever()
# Close the loop to clean up resources (this line runs after loop.stop())
loop.close()

#output
#  loop = asyncio.get_event_loop()
# task_A called
# task_B called 
# task_C called
# task_A called
# task_B called 
# task_C called
# task_A called
# task_B called 
# task_C called
# task_A called
# task_B called 
# task_C called
# task_A called
# task_B called 
# task_C called
# task_A called
# task_B called 