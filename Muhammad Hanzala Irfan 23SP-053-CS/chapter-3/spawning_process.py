import multiprocessing

def print_cube(num):
    print("Cube:", num * num * num)

if __name__ == "__main__":
    p = multiprocessing.Process(target=print_cube, args=(5,))
    
    p.start()
    p.join()

    print("Process finished")