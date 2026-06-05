import concurrent.futures
import time
import sys

number = [5, 10, 15, 20, 25]

def sum_of_n(n):
    count = 0
    for i in range(1, n+1):
        count = count + i
    print(f"Sum of {n} = {count}")
    return count

def main():
    # Replace time.clock() with time.perf_counter()
    start_time = time.perf_counter()
    
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        results = executor.map(sum_of_n, number)
    
    # Replace time.clock() with time.perf_counter()
    end_time = time.perf_counter()
    
    print(f"Total time taken: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()
# output:

# C:\Users\LAPTOP LAB>"C:/Users/LAPTOP LAB/AppData/Local/Programs/Python/Python310/python.exe" "c:/Users/LAPTOP LAB/OneDrive - Higher Education Commission/Desktop/Python-Parallel-Programming-Cookbook-Second-Edition/Chapter05/concurrent_futures_pooling.py"
# Sum of 5 = 15
# Sum of 10 = 55
# Sum of 15 = 120
# Sum of 20 = 210
# Sum of 25 = 325
# Total time taken: 0.30301460018381476 seconds

# C:\Users\LAPTOP LAB>


