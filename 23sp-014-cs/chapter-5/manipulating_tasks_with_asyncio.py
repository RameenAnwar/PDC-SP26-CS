import asyncio

async def work():
    print("Task running")
    await asyncio.sleep(2)
    print("Task finished")

async def main():
    task = asyncio.create_task(work())

    print("Doing something else")

    await task

asyncio.run(main())