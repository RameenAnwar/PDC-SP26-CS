# Simple function used in multiprocessing examples
def myFunc(i):
    print('Function called from process number:', i)

    # Loop to print values up to i
    for j in range(i):
        print('Output:', j)

    return