# asyncio_and_futures.py  --  Chapter 5: Asyncio and Futures
# A FUTURE is a placeholder for a result that isn't ready yet. Two coroutines each
# compute a value and store it in a Future via set_result(). A done-callback
# (got_result) fires automatically when each Future is completed.
# RUN COMMAND:  python asyncio_and_futures.py 5 6     (5 and 6 are command-line args)
#
# ----------------------- CODE (commented out) -----------------------
# import asyncio
# import sys
# @asyncio.coroutine
# def first_coroutine(future, num):
#     count = 0
#     for i in range(1, num + 1):
#         count += 1                       # sum of 1..num (just counts them)
#     yield from asyncio.sleep(4)
#     future.set_result('First coroutine (sum of N ints) result = %s' % count)
# @asyncio.coroutine
# def second_coroutine(future, num):
#     count = 1
#     for i in range(2, num + 1):
#         count *= i                       # factorial of num
#     yield from asyncio.sleep(4)
#     future.set_result('Second coroutine (factorial) result = %s' % count)
# def got_result(future):
#     print(future.result())               # callback prints the finished result
# if __name__ == '__main__':
#     num1 = int(sys.argv[1])
#     num2 = int(sys.argv[2])
#     loop = asyncio.get_event_loop()
#     future1 = asyncio.Future()
#     future2 = asyncio.Future()
#     tasks = [first_coroutine(future1, num1), second_coroutine(future2, num2)]
#     future1.add_done_callback(got_result)
#     future2.add_done_callback(got_result)
#     loop.run_until_complete(asyncio.wait(tasks))
#     loop.close()
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# (run as:  python asyncio_and_futures.py 5 6)
# First coroutine (sum of N ints) result = 5
# Second coroutine (factorial) result = 720
# --------------------------------------------------------------------
