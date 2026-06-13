import multiprocessing

# Function to square numbers
def function_square(data):
    return data * data


if __name__ == '__main__':
    inputs = list(range(100))  # Numbers 0–99

    # Create pool with 4 processes
    pool = multiprocessing.Pool(processes=4)

    # Apply function in parallel
    pool_outputs = pool.map(function_square, inputs)

    pool.close()  # Stop new tasks
    pool.join()   # Wait for completion

    print('Pool:', pool_outputs)