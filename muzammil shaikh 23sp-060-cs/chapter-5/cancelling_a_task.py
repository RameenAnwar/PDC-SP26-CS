import asyncio

async def work():
    try:
        while True:
            print("Working...")
            await asyncio.sleep(1)

    except asyncio.CancelledError:
        print("Task cancelled")

async def main():
    task = asyncio.create_task(work())

    await asyncio.sleep(3)

    task.cancel()

    await task

asyncio.run(main())