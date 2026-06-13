import multiprocessing

# Custom process class that overrides the run() method
class MyProcess(multiprocessing.Process):

    def run(self):
        print ('called run method in %s' %self.name)  # Print process name when run() is called
        return

if __name__ == '__main__':
    # Create and start 10 processes one after another (not parallel)
    for i in range(10):
        process = MyProcess()  # Create a new instance of MyProcess
        process.start()  # Start the process (calls run() automatically)
        process.join()  # Wait for this process to finish before creating next one