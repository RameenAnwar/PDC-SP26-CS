import multiprocessing
from myFunc import myFunc  # Import function from another file

if __name__ == '__main__':
    for i in range(6):
        process = multiprocessing.Process(
            target=myFunc, args=(i,)
        )
        process.start()
        process.join()