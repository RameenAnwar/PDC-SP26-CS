import asyncio
import sys


async def first_coroutine(future, num):
    count = 0

    for i in range(1, num + 1):
        count += 1

    await asyncio.sleep(4)

    future.set_result(
        'First coroutine (sum of N ints) result = %s' % count
    )


async def second_coroutine(future, num):
    count = 1

    for i in range(2, num + 1):
        count *= i

    await asyncio.sleep(4)

    future.set_result(
        'Second coroutine (factorial) result = %s' % count
    )


def got_result(future):
    print(future.result())


async def main():
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[2])

    future1 = asyncio.Future()
    future2 = asyncio.Future()

    tasks = [
        first_coroutine(future1, num1),
        second_coroutine(future2, num2)
    ]

    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)

    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())