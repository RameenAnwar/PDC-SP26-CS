# process_in_subclass.py
# Defining a process by SUBCLASSING multiprocessing.Process and overriding run(),
# exactly like we did with threads in Chapter 2.

import multiprocessing

class MyProcess(multiprocessing.Process):
    def run(self):                       # code that runs inside the new process
        print('called run method in %s' % self.name)
        return

if __name__ == '__main__':
    for i in range(10):
        process = MyProcess()
        process.start()
        process.join()
