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
    if x < 0 and power%2 ==0:    ##  Or ,assert expressions assert ctr <= 100
        return None
    low = min(-1.0,x)
    high = max(1.0,x)
    ans = (high + low)/2.0
    
    
    while abs(ans**power - x) >= epsilon:
        if ans**power < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    return ans
##Just  Execute It and Using the Function in the Shell.
##Or Using the Function Here.


def testFindRoot():
    epsilon = 0.0001
    for x in (0.25,-0.25,2,-2,8,-8):
        for power in range(1,4):
            print "Testing x = "+ str(x)+"and power = "+ str(power)
            result = findRoot(x,power,epsilon)
            if result == None:
                print "No root"
            else:
                print "  " + str(result**power) + "  " + str(x)

##  PARDON??  Why ??   I couldn't understand.
                
    
       
