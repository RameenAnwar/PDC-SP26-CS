# myFunc.py
# A standalone helper module containing myFunc(), imported by
# spawning_processes_namespace.py to show how to spawn a function from another module.

def myFunc(i):
    print('calling myFunc from process n°: %s' % i)
    for j in range(0, i):
        print('output from myFunc is :%s' % j)
    return
