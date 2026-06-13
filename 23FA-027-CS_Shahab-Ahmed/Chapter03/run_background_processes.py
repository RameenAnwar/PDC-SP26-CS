import multiprocessing
import time

# Function executed by processes
def foo():
    name = multiprocessing.current_process().name
    print("Starting", name)

    # Different behavior based on process name
    if name == 'background_process':
        for i in range(5):
            print('--->', i)
        time.sleep(1)
    else:
        for i in range(5, 10):
            print('--->', i)
        time.sleep(1)

    print("Exiting", name)


if __name__ == '__main__':
    # Daemon process (background process)
    background_process = multiprocessing.Process(
        name='background_process', target=foo
    )
    background_process.daemon = True  # Will stop when main program exits

    # Non-daemon process
    NO_background_process = multiprocessing.Process(
        name='NO_background_process', target=foo
    )
    NO_background_process.daemon = False

    background_process.start()
    NO_background_process.start()