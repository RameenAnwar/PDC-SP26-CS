# concurrent_futures_pooling.py  --  Chapter 5: concurrent.futures Pooling
# Runs the SAME CPU-heavy job 3 ways and times each: (1) sequentially,
# (2) with a ThreadPool, (3) with a ProcessPool. The ProcessPool is usually
# fastest for CPU-bound work because it uses multiple cores (no GIL).
# RUN COMMAND:  python concurrent_futures_pooling.py
# NOTE: time.clock() was REMOVED in Python 3.8 - replace it with time.perf_counter().
#
# ----------------------- CODE (commented out) -----------------------
# import concurrent.futures
# import time
# number_list = list(range(1, 11))
# def count(number):
#     for i in range(0, 10000000):        # busy work to keep the CPU loaded
#         i += 1
#     return i * number
# def evaluate(item):
#     result_item = count(item)
#     print('Item %s, result %s' % (item, result_item))
# if __name__ == '__main__':
#     # Sequential Execution
#     start_time = time.clock()
#     for item in number_list:
#         evaluate(item)
#     print('Sequential Execution in %s seconds' % (time.clock() - start_time))
#     # Thread Pool Execution
#     start_time = time.clock()
#     with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
#         for item in number_list:
#             executor.submit(evaluate, item)
#     print('Thread Pool Execution in %s seconds' % (time.clock() - start_time))
#     # Process Pool Execution
#     start_time = time.clock()
#     with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
#         for item in number_list:
#             executor.submit(evaluate, item)
#     print('Process Pool Execution in %s seconds' % (time.clock() - start_time))
# --------------------------------------------------------------------
#
# ----------------------------- OUTPUT -------------------------------
# (exact item order and times vary by machine)
# Item 1, result 10000000
# Item 2, result 20000000
# ... up to Item 10, result 100000000 ...
# Sequential Execution in 6.8 seconds
# Item 1, result 10000000
# ...
# Thread Pool Execution in 6.9 seconds     (no speed-up: GIL blocks CPU-bound threads)
# Item 1, result 10000000
# ...
# Process Pool Execution in 1.9 seconds    (faster: real parallelism across cores)
# --------------------------------------------------------------------
