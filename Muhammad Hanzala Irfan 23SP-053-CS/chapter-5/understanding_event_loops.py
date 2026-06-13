import asyncio

async def task():
    print("Task started")
    await asyncio.sleep(1)
    print("Task completed")

loop = asyncio.get_event_loop()

loop.run_until_complete(task())

loop.close()