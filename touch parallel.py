from multiprocessing import Pool

def square(n):
    return n*n

if __name__ == "__main__":
    numbers = [1,2,3,4]
    p = Pool(2)
    result = p.map(square, numbers)
    print(result)
