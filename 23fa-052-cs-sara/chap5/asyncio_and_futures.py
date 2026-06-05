
import asyncio
import sys

# SUM OF N INTEGERS
async def first_coroutine(future, N):
    count = 0
    for i in range(1, N + 1):
        count = count + i
    await asyncio.sleep(4)
    future.set_result("first coroutine (sum of N integers) result = " + str(count))

# FACTORIAL(N)
async def second_coroutine(future, N):
    count = 1
    for i in range(2, N + 1):
        count *= i
    await asyncio.sleep(3)
    future.set_result("second coroutine (factorial) result = " + str(count))

def got_result(future):
    print(future.result())

async def main():
    N1 = int(sys.argv[1])
    N2 = int(sys.argv[2])
    
    loop = asyncio.get_running_loop()
    future1 = loop.create_future()
    future2 = loop.create_future()
    
    # Create tasks
    task1 = asyncio.create_task(first_coroutine(future1, N1))
    task2 = asyncio.create_task(second_coroutine(future2, N2))
    
    future1.add_done_callback(got_result)
    future2.add_done_callback(got_result)
    
    await asyncio.gather(task1, task2)

if __name__ == "__main__":
    asyncio.run(main())
#output:
#C:\Users\LAPTOP LAB\OneDrive - Higher Education Commission\Desktop\Python-Parallel-Programming-Cookbook-Second-Edition\Chapter05>python asyncio_and_futures.py 5 10
#second coroutine (factorial) result = 3628800
#first coroutine (sum of N integers) result = 15
