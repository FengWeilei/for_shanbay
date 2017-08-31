def getRatios(vect1, vect2):
    """Assumes: vect1 and vect2 are lists of equal length of numbers.
       Returns: a list containing the meaningful values of vect[i]/vect[i]"""

    ratios = []
    for index in range(len(vect1)):
        try:
            ratios.append(vect1[index]/float(vect2[index]))
        except ZeroDivisionError:
            ratios.append(float("nan"))  ##nan =Not a number
        except:
            raise ValueError('getRatios called with bad args')

    return ratios

try:
    print getRatios([1,23,4,567,89],[2,3,4,5,6])

    print getRatios([],[])
    print getRatios([0,2],[2])
except ValueError, msg:
    print msg


## without using a try-except
## less efficiency and better not.

##def getRatios(vec1,vec2):
##    """Assumes: vect1 and vec2 are lists of equal length of numbers
##       Returns: a list containing the meaningful values of vec[i]/vec[2]"""
##
##    ratios = []
##    if len(vec1) != len(vec2):
##        raise ValueError("getRatios called with bad args")
##    for index in range(len(vec1)):
##        vec1Elem = vec1[index]
##        vec2Elem = vec2[index]
##        if (type(vec1Elem) not in (int, float)) or (type(vec2Elem) not in (int, float)):
##                raise ValueError("getRatios called with bad args")
##        if vec2Elem == 0.0:
##            ratios.append(float('NaN'))
##        else:
##            ratios.append(vec1Elem/vec2Elem)
##            
##    return ratios
##
##print getRatios([1,23,4,567,89],[2,3,4,5,6])
##
##print getRatios([],[])
##print getRatios([0,2],[2])
