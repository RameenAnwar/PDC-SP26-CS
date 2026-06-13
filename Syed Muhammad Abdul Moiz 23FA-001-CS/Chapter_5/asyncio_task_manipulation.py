import asyncio

# First asynchronous function: Calculates the factorial of a number.
async def factorial(number):
    fact = 1
    # Loop from 2 up to the provided number.
    for i in range(2, number + 1):
        print(f'Asyncio.Task: Compute factorial({i})')
        
        # Pause for 1 second. This allows the other math functions to run while this one waits!
        await asyncio.sleep(1)
        
        # Multiply to calculate the factorial.
        fact *= i
        
    # Print the final answer when the loop is totally finished.
    print(f'Asyncio.Task - factorial({number}) = {fact}')


# Second asynchronous function: Calculates the Fibonacci sequence.
async def fibonacci(number):
    a, b = 0, 1
    # Loop 'number' amount of times.
    for i in range(number):
        print(f'Asyncio.Task: Compute fibonacci({i})')
        
        # Pause for 1 second to let other tasks take a turn.
        await asyncio.sleep(1)
        
        # Update 'a' and 'b' to the next numbers in the Fibonacci sequence.
        a, b = b, a + b
        
    # Print the final Fibonacci number.
    print(f'Asyncio.Task - fibonacci({number}) = {a}')


# Third asynchronous function: Calculates the binomial coefficient.
async def binomial_coefficient(n, k):
    result = 1
    # Loop 'k' amount of times.
    for i in range(1, k + 1):
        # The math formula for binomial coefficient.
        result = result * (n - i + 1) / i
        
        print(f'Asyncio.Task: Compute binomial_coefficient({i})')
        
        # Pause for 1 second to let the Factorial and Fibonacci tasks run.
        await asyncio.sleep(1)
        
    # Print the final binomial coefficient answer.
    print(f'Asyncio.Task - binomial_coefficient({n}, {k}) = {result}')


# The main function that sets up and starts all the math problems together.
async def main():
    # Create a list containing all three tasks.
    # asyncio.create_task() schedules them to run in the background immediately.
    tasks = [
        asyncio.create_task(factorial(10)),
        asyncio.create_task(fibonacci(10)),
        asyncio.create_task(binomial_coefficient(20, 10))
    ]

    # asyncio.gather() groups the tasks. 'await' makes the program wait here 
    # until all three math problems are 100% complete.
    await asyncio.gather(*tasks)


# Check if the user is running this file directly.
if __name__ == '__main__':
    # Start the asyncio event loop manager, run the 'main' function, and clean up at the end.
    asyncio.run(main())