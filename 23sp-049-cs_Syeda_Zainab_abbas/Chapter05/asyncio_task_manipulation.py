# asyncio_task_manipulation.py  --  Chapter 5: Asynchronous Programming
# Uses asyncio.Task to run THREE math coroutines "in parallel" on one thread.
# While one task awaits (asyncio.sleep), the event loop runs another -> their
# output interleaves. (NOTE: @asyncio.coroutine / yield from is old syntax; on
# Python 3.8+ use `async def` and `await`.)
# RUN COMMAND:  python asyncio_task_manipulation.py
#
# ----------------------- CODE (commented out) -----------------------
# import asyncio
# @asyncio.coroutine
# def factorial(number):
#     fact = 1
#     for i in range(2, number + 1):
#         print('Asyncio.Task: Compute factorial(%s)' % i)
#         yield from asyncio.sleep(1)          # give control back to the loop
#         fact *= i
#     print('Asyncio.Task - factorial(%s) = %s' % (number, fact))
# @asyncio.coroutine
# def fibonacci(number):
#     a, b = 0, 1
#     for i in range(number):
#         print('Asyncio.Task: Compute fibonacci(%s)' % i)
#         yield from asyncio.sleep(1)
#         a, b = b, a + b
#     print('Asyncio.Task - fibonacci(%s) = %s' % (number, a))
# @asyncio.coroutine
# def binomial_coefficient(n, k):
#     result = 1
#     for i in range(1, k + 1):
#         result = result * (n - i + 1) / i
#         print('Asyncio.Task: Compute binomial_coefficient(%s)' % i)
#         yield from asyncio.sleep(1)
#     print('Asyncio.Task - binomial_coefficient(%s, %s) = %s' % (n, k, result))
# if __name__ == '__main__':
#     task_list = [asyncio.Task(factorial(10)),
#                  asyncio.Task(fibonacci(10)),
#                  asyncio.Task(binomial_coefficient(20, 10))]
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(asyncio.wait(task_list))
#     loop.close()
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# Asyncio.Task: Compute factorial(2)
# Asyncio.Task: Compute fibonacci(0)
# Asyncio.Task: Compute binomial_coefficient(1)
# Asyncio.Task: Compute factorial(3)
# Asyncio.Task: Compute fibonacci(1)
# Asyncio.Task: Compute binomial_coefficient(2)
# ... (the three tasks keep interleaving once per second) ...
# Asyncio.Task - fibonacci(10) = 55
# Asyncio.Task - factorial(10) = 3628800
# Asyncio.Task - binomial_coefficient(20, 10) = 184756.0
# --------------------------------------------------------------------
