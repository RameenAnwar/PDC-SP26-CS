import concurrent.futures
import time

number_list = list(range(1, 11))


def count(number):
    for i in range(0,10000000):
        i += 1
    return i*number


def evaluate(item):
    result_item = count(item)
    print('Item %s, result %s' % (item, result_item))

if __name__ == '__main__':
    # Sequential Execution
    start_time = time.clock()
    for item in number_list:
        evaluate(item)
    print('Sequential Execution in %s seconds' % (time.clock() - start_time))

   
    # Thread Pool Execution
    start_time = time.clock()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print('Thread Pool Execution in %s seconds' % (time.clock() - start_time))

      
    # Process Pool Execution
    start_time = time.clock()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in number_list:
            executor.submit(evaluate, item)
    print('Process Pool Execution in %s seconds' % (time.clock() - start_time))

#output
#Item 1, result 10000000
#Item 2, result 20000000
#Item 3, result 30000000
#Item 4, result 40000000
#Item 5, result 50000000
#Item 6, result 60000000
#Item 7, result 70000000
#Item 8, result 80000000
#Item 9, result 90000000
#Item 10, result 100000000
#Sequential Execution in 1.23 seconds
#
#Item 1, result 10000000
#Item 2, result 20000000
#Item 3, result 30000000
#Item 4, result 40000000
#Item 5, result 50000000
#Item 6, result 60000000
#Item 7, result 70000000
#Item 8, result 80000000
#Item 9, result 90000000
#Item 10, result 100000000
#Thread Pool Execution in 0.78 seconds
#
#Item 1, result 10000000
#Item 2, result 20000000
#Item 3, result 30000000
#Item 4, result 40000000
#Item 5, result 50000000
#Item 6, result 60000000
#Item 7, result 70000000
#Item 8, result 80000000
#Item 9, result 90000000
#Item 10, result 100000000
#Process Pool Execution in 0.52 seconds