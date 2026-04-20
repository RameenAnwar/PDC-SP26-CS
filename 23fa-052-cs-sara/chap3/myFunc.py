# Simple call
myFunc(5)

# Or with multiprocessing
from multiprocessing import Process

p = Process(target=myFunc, args=(5,))
p.start()
p.join()