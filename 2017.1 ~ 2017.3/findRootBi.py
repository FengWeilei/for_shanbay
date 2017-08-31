def findRoot(x,power,epsilon):
    """x and epsilon int or float,power an int,
          epsilon >0 & power >= 1
       returns float y such that y**power is within epsilon of x.
          If such a float does not exist,it returns None
          And I could type more.
          When I type help(findRoot) in the Shell.
          They all appears.
          MengYuan ,Happy New Year!
          Wish You Happy & Safe!"""
    
    assert x >= 0   ##  Or ,assert expressions assert ctr <= 10
    assert epsilon > 0
    low = min(-1.0,x)
    high = max(1.0,x)
    ans = (high + low)/2.0
    i = 1
    
    while abs(ans**power - x) >= epsilon and i <= 100:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
        i += 1
    return ans

print findRoot(0,2,0.00001),i

