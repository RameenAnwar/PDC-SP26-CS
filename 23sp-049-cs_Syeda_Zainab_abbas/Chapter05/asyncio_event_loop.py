# asyncio_event_loop.py  --  Chapter 5: Using the Event Loop
# Shows the asyncio EVENT LOOP scheduling work. task_A schedules task_B, which
# schedules task_C, which schedules task_A again, every 1 second, until 60s pass.
# call_later() and call_soon() ask the loop to run a function later.
# RUN COMMAND:  python asyncio_event_loop.py   (press Ctrl+C to stop early)
#
# ----------------------- CODE (commented out) -----------------------
# import asyncio
# import time
# import random
# def task_A(end_time, loop):
#     print("task_A called")
#     time.sleep(random.randint(0, 5))
#     if (loop.time() + 1.0) < end_time:
#         loop.call_later(1, task_B, end_time, loop)   # schedule task_B in 1s
#     else:
#         loop.stop()
# def task_B(end_time, loop):
#     print("task_B called ")
#     time.sleep(random.randint(0, 5))
#     if (loop.time() + 1.0) < end_time:
#         loop.call_later(1, task_C, end_time, loop)
#     else:
#         loop.stop()
# def task_C(end_time, loop):
#     print("task_C called")
#     time.sleep(random.randint(0, 5))
#     if (loop.time() + 1.0) < end_time:
#         loop.call_later(1, task_A, end_time, loop)
#     else:
#         loop.stop()
# loop = asyncio.get_event_loop()
# end_loop = loop.time() + 60          # run for about 60 seconds
# loop.call_soon(task_A, end_loop, loop)   # kick off task_A as soon as possible
# loop.run_forever()
# loop.close()
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# task_A called
# task_B called
# task_C called
# task_A called
# task_B called
# task_C called
# ... (keeps cycling A -> B -> C until ~60 seconds elapse, then the loop stops) ...
# --------------------------------------------------------------------
