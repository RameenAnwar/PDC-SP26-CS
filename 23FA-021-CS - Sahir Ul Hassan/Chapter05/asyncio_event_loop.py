import asyncio
import random


async def task_A(end_time):
    """Task A - part of event loop demo"""
    print("task_A called")
    await asyncio.sleep(random.randint(0, 5))
    return "Task A completed"


async def task_B(end_time):
    """Task B - part of event loop demo"""
    print("task_B called")
    await asyncio.sleep(random.randint(0, 5))
    return "Task B completed"


async def task_C(end_time):
    """Task C - part of event loop demo"""
    print("task_C called")
    await asyncio.sleep(random.randint(0, 5))
    return "Task C completed"


async def run_tasks(duration=60):
    """Run tasks sequentially with time constraints"""
    start_time = asyncio.get_event_loop().time()
    end_time = start_time + duration

    while asyncio.get_event_loop().time() < end_time:
        await task_A(end_time)
        if asyncio.get_event_loop().time() >= end_time:
            break
        await task_B(end_time)
        if asyncio.get_event_loop().time() >= end_time:
            break
        await task_C(end_time)


if __name__ == '__main__':
    asyncio.run(run_tasks(60))


