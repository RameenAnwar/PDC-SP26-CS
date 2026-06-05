import concurrent.futures
import time

number_list = list(range(1, 11))


def count(number):
    """Compute intensive operation"""
    for i in range(0, 10000000):
        i += 1
    return i * number


def evaluate(item):
    """Evaluate a single item"""
    result_item = count(item)
    print('Item %s, result %s' % (item, result_item))

if __name__ == '__main__':
    # Sequential Execution
    start_time = time.perf_counter()
    for item in number_list:
        evaluate(item)
    elapsed = time.perf_counter() - start_time
    print('Sequential Execution in %s seconds' % elapsed)


    # Thread Pool Execution
    start_time = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    elapsed = time.perf_counter() - start_time
    print('Thread Pool Execution in %s seconds' % elapsed)

      
    # Process Pool Execution
    start_time = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    elapsed = time.perf_counter() - start_time
    print('Process Pool Execution in %s seconds' % elapsed)
