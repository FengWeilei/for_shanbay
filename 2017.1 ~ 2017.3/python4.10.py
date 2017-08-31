numCalls = 0    ##  Maybe it should be added.I don't know.

def fib(x):
    """assumes x is an int >= 0
       Returns Fibonacci of x"""

    global numCalls
    numCalls += 1
    if x == 0 or x == 1 :
        return 1
    else:
        return fib(x-1) + fib(x-2)

def testFib(n):
    for i in range(n+1):
        global numCalls
        numCalls = 0
        print "fib of",i,"=",fib(i)
        print "fib called", numCalls,"times"
