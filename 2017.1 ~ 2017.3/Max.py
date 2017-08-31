def max(x,y):
    if x > y:
        return x
    else:
        return y
##print max(2,5)

##  Just a definition.
##  Can be done in the terminal

def f(x):
    def g(x):
        x = 'abc'
        print "x = ",x
    def h(x):
        z = x
        print "z = ",z
    x = x + 1
    print "x = ",x
    h()
    g()
    print "x = ",x
    return g
x = 3
z = f(x)
print "x = ",x
print "z = ",z
z()
    
            



