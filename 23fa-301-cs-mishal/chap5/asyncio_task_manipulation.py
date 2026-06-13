"""Asyncio using async/await to execute three math functions in parallel"""

import asyncio

async def factorial(number):
    """Coroutine to compute factorial of number."""
    fact = 1
    for i in range(2, number + 1):
        print('Asyncio.Task: Compute factorial(%s)' % i)
        await asyncio.sleep(1)          # non‑blocking sleep (1 sec)
        fact *= i
    print('Asyncio.Task - factorial(%s) = %s' % (number, fact))

async def fibonacci(number):
    """Coroutine to compute Fibonacci up to number."""
    a, b = 0, 1
    for i in range(number):
        print('Asyncio.Task: Compute fibonacci(%s)' % i)
        await asyncio.sleep(1)
        a, b = b, a + b
    print('Asyncio.Task - fibonacci(%s) = %s' % (number, a))

async def binomial_coefficient(n, k):
    """Coroutine to compute C(n, k) = n!/(k!(n‑k)!)."""
    result = 1
    for i in range(1, k + 1):
        result = result * (n - i + 1) / i
        print('Asyncio.Task: Compute binomial_coefficient(%s)' % i)
        await asyncio.sleep(1)
    print('Asyncio.Task - binomial_coefficient(%s, %s) = %s' % (n, k, result))

async def main():
    """Entry point: create tasks and run them concurrently."""
    tasks = [
        asyncio.create_task(factorial(10)),      # wrap coroutine into Task
        asyncio.create_task(fibonacci(10)),
        asyncio.create_task(binomial_coefficient(20, 10))
    ]
    await asyncio.wait(tasks)                    # wait for all tasks to finish

if __name__ == '__main__':
    asyncio.run(main())                          # start event loop and run main()

    #ouptut
# Asyncio.Task: Compute fibonacci(5)
# Asyncio.Task: Compute binomial_coefficient(6)
# Asyncio.Task: Compute factorial(8)
# Asyncio.Task: Compute fibonacci(6)
# Asyncio.Task: Compute binomial_coefficient(7)
# Asyncio.Task: Compute factorial(9)
# Asyncio.Task: Compute fibonacci(7)
# Asyncio.Task: Compute binomial_coefficient(8)
# Asyncio.Task: Compute factorial(10)
# Asyncio.Task: Compute fibonacci(8)
# Asyncio.Task: Compute binomial_coefficient(9)
# Asyncio.Task - factorial(10) = 3628800
# Asyncio.Task: Compute fibonacci(9)
# Asyncio.Task: Compute binomial_coefficient(10)
# Asyncio.Task - fibonacci(10) = 55
# Asyncio.Task - binomial_coefficient(20, 10) = 184756.0