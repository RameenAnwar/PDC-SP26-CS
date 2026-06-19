import asyncio

async def first():
    print("First coroutine")
    await asyncio.sleep(1)
    print("First completed")

async def second():
    print("Second coroutine")
    await asyncio.sleep(2)
    print("Second completed")

async def main():
    await first()
    await second()

asyncio.run(main())