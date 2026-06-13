import multiprocessing
import time

# Function executed by process
def myFunc():
    name = multiprocessing.current_process().name
    print("Starting:", name)
    time.sleep(3)
    print("Exiting:", name)


if __name__ == '__main__':
    # Process with custom name
    process_with_name = multiprocessing.Process(
        name='myFunc process', target=myFunc
    )

    # Process with default name
    process_with_default_name = multiprocessing.Process(target=myFunc)

    process_with_name.start()
    process_with_default_name.start()

    process_with_name.join()
    process_with_default_name.join()