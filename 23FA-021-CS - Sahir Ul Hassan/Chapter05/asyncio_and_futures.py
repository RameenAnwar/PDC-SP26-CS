import asyncio
import sys


async def first_coroutine(future, num):
    """Calculate sum of integers from 1 to num"""
    count = 0
    for i in range(1, num + 1):
        count += 1
    await asyncio.sleep(4)
    future.set_result('First coroutine (sum of N ints) result = %s' % count)


async def second_coroutine(future, num):
    """Calculate factorial of num"""
    count = 1
    for i in range(2, num + 1):
        count *= i
    await asyncio.sleep(4)
    future.set_result('Second coroutine (factorial) result = %s' % count)


def got_result(future):
    print(future.result())


async def main(num1, num2):
    future1 = asyncio.Future()
    future2 = asyncio.Future()

    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    tasks = [first_coroutine(future1, num1),
             second_coroutine(future2, num2)]

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    # Use command-line arguments if provided, otherwise use defaults
    if len(sys.argv) < 3:
        print("Usage: python asyncio_and_futures.py <num1> <num2>")
        print("Using default values: num1=10, num2=10")
        num1 = 10
        num2 = 10
    else:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])

    asyncio.run(main(num1, num2))
