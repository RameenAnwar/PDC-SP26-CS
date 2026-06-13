import asyncio

async def add(a, b):
    await asyncio.sleep(1)
    return a + b

async def main():
    result = await add(5, 10)
    print("Result:", result)

asyncio.run(main())