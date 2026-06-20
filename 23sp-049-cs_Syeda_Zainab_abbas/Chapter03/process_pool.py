# process_pool.py
# A PROCESS POOL distributes work across a fixed number of worker processes.
# pool.map() splits the input list among 4 workers and collects the results in order.

import multiprocessing

def function_square(data):
    result = data * data            # the work each item needs: square it
    return result

if __name__ == '__main__':
    inputs = list(range(0, 100))    # numbers 0..99
    pool = multiprocessing.Pool(processes=4)        # 4 worker processes
    pool_outputs = pool.map(function_square, inputs)  # parallel map over inputs

    pool.close()    # no more tasks will be submitted
    pool.join()     # wait for all workers to finish
    print('Pool    :', pool_outputs)   # [0, 1, 4, 9, 16, ... 9801]
