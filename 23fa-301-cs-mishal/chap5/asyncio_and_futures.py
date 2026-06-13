import asyncio
import sys

# First coroutine: calculates "count" as the number of integers from 1 to num
# (so result = num, because count increments once per loop iteration)
async def first_coroutine(future, num):
    count = 0
    for i in range(1, num + 1):
        count += 1          # adds 1 for each i, so final count == num
    await asyncio.sleep(4)  # simulate non‑blocking wait (4 seconds)
    future.set_result('First coroutine (sum of N ints) result = %s' % count)

# Second coroutine: calculates factorial of num
async def second_coroutine(future, num):
    count = 1
    for i in range(2, num + 1):
        count *= i          # multiply sequentially to compute factorial
    await asyncio.sleep(4)
    future.set_result('Second coroutine (factorial) result = %s' % count)

# Callback function: called when a Future is done; prints its result
def got_result(future):
    print(future.result())

if __name__ == '__main__':
    # Read two integer arguments from the command line
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    # Get the current event loop (the "scheduler" for async tasks)
    loop = asyncio.get_event_loop()

    # Create two Future objects – they will hold the results of the coroutines
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    # Convert each coroutine into a Task (so the event loop can run them)
    task1 = loop.create_task(first_coroutine(future1, num1))
    task2 = loop.create_task(second_coroutine(future2, num2))
    tasks = [task1, task2]

    # Attach the same callback to both futures – it will print each result
    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    # Run the event loop until all tasks are complete
    loop.run_until_complete(asyncio.wait(tasks))

    # Clean up
    loop.close()

    #output
#     current event loop
#   loop = asyncio.get_event_loop()
# First coroutine (sum of N ints) result = 10
# Second coroutine (factorial) result = 120