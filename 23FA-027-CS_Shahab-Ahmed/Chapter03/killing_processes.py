import multiprocessing
import time

# Function to simulate long-running task
def foo():
    print('Starting function')
    for i in range(10):
        print('-->', i)
        time.sleep(1)
    print('Finished function')


if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)

    print('Before execution:', p.is_alive())

    p.start()  # Start process
    print('Running:', p.is_alive())

    p.terminate()  # Forcefully stop process
    print('Terminated:', p.is_alive())

    p.join()  # Wait for process to end

    print('Exit code:', p.exitcode)