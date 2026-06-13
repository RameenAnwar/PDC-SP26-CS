import asyncio
import sys

# Create the first asynchronous function
async def first_coroutine(num):
    count = 0
    # Loop from 1 up to the number provided to calculate the sum
    for i in range(1, num + 1):
        count += 1

    # Pause this task for 4 seconds so the CPU can do other things
    await asyncio.sleep(4)
    # Return the final sum formatted as a string
    return f"First coroutine (sum of N ints) result = {count}"


# Create the second asynchronous function
async def second_coroutine(num):
    count = 1
    # Loop from 2 up to the number provided to calculate the factorial
    for i in range(2, num + 1):
        count *= i

    # Pause this task for 4 seconds as well
    await asyncio.sleep(4)
    # Return the final factorial result formatted as a string
    return f"Second coroutine (factorial) result = {count}"


# A standard function that acts as our "callback"
def got_result(task):
    # This grabs the final string from the finished task and prints it to the screen
    print(task.result())


# The main async function that starts our tasks
async def main():
    # Grab the first number typed in the terminal and turn it into an integer
    num1 = int(sys.argv[1])
    # Grab the second number typed in the terminal and turn it into an integer
    num2 = int(sys.argv[2])

    # Instantly schedule both coroutines to run in the background as "Tasks"
    task1 = asyncio.create_task(first_coroutine(num1))
    task2 = asyncio.create_task(second_coroutine(num2))

    # Tell task1: "When you finish running, automatically trigger the 'got_result' function."
    task1.add_done_callback(got_result)
    # Tell task2 to do the exact same thing when it finishes
    task2.add_done_callback(got_result)

    # Group both tasks together and wait here until both of them are 100% finished
    await asyncio.gather(task1, task2)


# Check if the user is running this file directly
if __name__ == "__main__":
    # Start the asyncio event loop manager, run the 'main' function, and clean up at the end
    asyncio.run(main())