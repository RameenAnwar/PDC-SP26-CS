import multiprocessing

def worker():
    print("Process running")

if __name__ == "__main__":
    p = multiprocessing.Process(target=worker, name="MyProcess")

    print("Process Name:", p.name)

    p.start()
    p.join()