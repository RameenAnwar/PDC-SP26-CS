import multiprocessing

class MyProcess(multiprocessing.Process):

    def run(self):
        print("Process subclass is running")

if __name__ == "__main__":
    p = MyProcess()

    p.start()
    p.join()