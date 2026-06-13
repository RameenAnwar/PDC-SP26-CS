import multiprocessing

# Function executed by each process
def myFunc(i):
    print('Process number:', i)
    for j in range(i):
        print('Output:', j)


if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(
            target=myFunc, args=(i,)
        )
        process.start()  # Start process
        process.join()   # Wait for completion