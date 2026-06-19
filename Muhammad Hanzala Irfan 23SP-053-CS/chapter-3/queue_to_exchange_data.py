from multiprocessing import Process, Queue

def square(numbers, q):
    for n in numbers:
        q.put(n * n)

if __name__ == "__main__":
    q = Queue()

    numbers = [1, 2, 3, 4]

    p = Process(target=square, args=(numbers, q))

    p.start()
    p.join()

    while not q.empty():
        print(q.get())