def myFunc(i):
    # Print a message showing which process number is calling this function
    print('calling myFunc from process n°: %s' %i)
    # Run a loop 'i' times
    for j in range(0,i):
        # Print the current step of the loop
        print('output from myFunc is :%s' %j)
    # End the function
    return