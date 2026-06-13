"""Asyncio using Asyncio.Task to execute three math functions in parallel"""

import asyncio


@asyncio.coroutine
def factorial(number):
    fact = 1
    for i in range(2, number + 1):
        print('Asyncio.Task: Compute factorial(%s)' % i)
        yield from asyncio.sleep(1)
        fact *= i
    print('Asyncio.Task - factorial(%s) = %s' % (number, fact))


@asyncio.coroutine
def fibonacci(number):
    a, b = 0, 1
    for i in range(number):
        print('Asyncio.Task: Compute fibonacci(%s)' % i)
        yield from asyncio.sleep(1)
        a, b = b, a + b
    print('Asyncio.Task - fibonacci(%s) = %s' % (number, a))


@asyncio.coroutine
def binomial_coefficient(n, k):
    result = 1
    for i in range(1, k + 1):
        result = result*(n - i + 1)/i
        print('Asyncio.Task: Compute binomial_coefficient(%s)' % i)
        yield from asyncio.sleep(1)
    print('Asyncio.Task - binomial_coefficient(%s, %s) = %s' % (n, k, result))


if __name__ == '__main__':
    task_list = [asyncio.Task(factorial(10)),
                 asyncio.Task(fibonacci(10)),
                 asyncio.Task(binomial_coefficient(20, 10))]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(task_list))
    loop.close()

    #output
#Asyncio.Task: Compute factorial(2)
#Asyncio.Task: Compute fibonacci(0)
#Asyncio.Task: Compute binomial_coefficient(1)
#Asyncio.Task: Compute factorial(3)
#Asyncio.Task: Compute fibonacci(1)
#Asyncio.Task: Compute binomial_coefficient(2)
#Asyncio.Task: Compute factorial(4)
#Asyncio.Task: Compute fibonacci(2)
#Asyncio.Task: Compute binomial_coefficient(3)
#Asyncio.Task: Compute factorial(5)
#Asyncio.Task: Compute fibonacci(3)
#Asyncio.Task: Compute binomial_coefficient(4)
#Asyncio.Task: Compute factorial(6)
#Asyncio.Task: Compute fibonacci(4)
#Asyncio.Task: Compute binomial_coefficient(5)
#Asyncio.Task: Compute factorial(7)
#Asyncio.Task: Compute fibonacci(5)
#Asyncio.Task: Compute binomial_coefficient(6)
#Asyncio.Task: Compute factorial(8)
#Asyncio.Task: Compute fibonacci(6)
#Asyncio.Task: Compute binomial_coefficient(7)
#Asyncio.Task: Compute factorial(9)
#Asyncio.Task: Compute fibonacci(7)
#Asyncio.Task: Compute binomial_coefficient(8)
#Asyncio.Task: Compute factorial(10)
#Asyncio.Task: Compute fibonacci(8)
#Asyncio.Task: Compute binomial_coefficient(9)
#Asyncio.Task: Compute fibonacci(9)
#Asyncio.Task: Compute binomial_coefficient(10)
#
#Asyncio.Task - factorial(10) = 3628800
#Asyncio.Task - fibonacci(10) = 55
#Asyncio.Task - binomial_coefficient(20, 10) = 184756.0
