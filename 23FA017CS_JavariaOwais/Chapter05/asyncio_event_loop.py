import asyncio
import random


async def task_A(end_time):
    print("task_A called")

    await asyncio.sleep(random.randint(0, 5))

    if (asyncio.get_running_loop().time() + 1.0) < end_time:
        asyncio.get_running_loop().call_later(
            1,
            lambda: asyncio.create_task(task_B(end_time))
        )
    else:
        asyncio.get_running_loop().stop()


async def task_B(end_time):
    print("task_B called")

    await asyncio.sleep(random.randint(0, 5))

    if (asyncio.get_running_loop().time() + 1.0) < end_time:
        asyncio.get_running_loop().call_later(
            1,
            lambda: asyncio.create_task(task_C(end_time))
        )
    else:
        asyncio.get_running_loop().stop()


async def task_C(end_time):
    print("task_C called")

    await asyncio.sleep(random.randint(0, 5))

    if (asyncio.get_running_loop().time() + 1.0) < end_time:
        asyncio.get_running_loop().call_later(
            1,
            lambda: asyncio.create_task(task_A(end_time))
        )
    else:
        asyncio.get_running_loop().stop()


async def main():

    loop = asyncio.get_running_loop()

    end_loop = loop.time() + 60

    loop.call_soon(
        lambda: asyncio.create_task(task_A(end_loop))
    )

    while True:
        await asyncio.sleep(1)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except RuntimeError:
        pass