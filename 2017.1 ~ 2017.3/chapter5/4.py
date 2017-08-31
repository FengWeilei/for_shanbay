##import copy

def removeDups(L1,L2):
    """Assumes that L1 and L2 are list.
       Removes any element in L1 that also occurs in L2"""
    for e1 in L1:
        if e1 in L2:
            L1.remove(e1)

L1 = [1,2,3,4]
L2 = [1,2,5,6]
##L3 = copy.deepcopy(L1)
removeDups(L1,L2)
print 'L1=',L1


##L = [x**2 for x in range(1,7)]
##print L
