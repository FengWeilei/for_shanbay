##  Iterative and recursive implementations of factorial


def factl(n):
    """Assumes that n is an int >0
       returns n!"""
    res = 1
    while n > 1:
        res = res*n
        n -= 1
    return res
##  Be Careful about the format.
##  Say,return should be in the same col as while   ,and so on.

def factR(n):
    """Assumes that n is an int > 0
       returns n!a"""
    if n==1:
        return n
    return n*factR(n-1)
