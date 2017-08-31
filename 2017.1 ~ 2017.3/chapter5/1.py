####  TUPLES
##
##
##t1 = ()
##t2 = (1,'two',3)
##print t1
##print t2
##
##
##t1 = (1,'two',3)
##t2 = (t1,3.25)
##print t2
##print (t1 + t2)
##print (t1 + t2)[3]
##print (t1 + t2)[2:4]


def findDivisors(n1,n2):
    """Assumes that n1 and n2 are positive ints
       returns a tuple containing common divisors of n1 &n2"""
    divisors = ()
    for i in range(1,min(n1,n2) + 1):
        if n1%i ==0 and n2%i ==0:
            divisors = divisors + (i,)
    return divisors   ## FORMAT!!  Be careful with the position of 'return'.

divisors = findDivisors(20,100)
print divisors
total = 0
for d in divisors:
    total += d
print total
