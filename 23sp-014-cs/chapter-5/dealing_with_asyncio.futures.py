import asyncio

async def set_future_value(future):
    await asyncio.sleep(2)
    future.set_result("Future Result")

async def main():

    loop = asyncio.get_running_loop()

    future = loop.create_future()

    asyncio.create_task(set_future_value(future))

    result = await future

    print(result)

asyncio.run(main())