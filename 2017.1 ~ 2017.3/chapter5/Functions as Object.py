##def applyToEach(L,f):
##    """Assumes L a list ,f a function
##       Mutates L by replacing each element,e ,of L by f(e)"""
##    for i in range(len(L)):
##        L[i] = f(L[i])
##
##
##L = [1, -2, 3.33]
##print "L = ",L
##
##print "Apply abs to each element of", L
##applyToEach(L,abs)
##print "L = ",L
##
##print "Apply int to each element of ",L
##applyToEach(L,int)
##print"L = ",L
##
####print "Apply factorial to each element of",L
####applyToEach(L,factl)
####print "L = ",L




s = 'Meng Yuan 2 3 0 0 0 2 '
print s.count('n')
print s.find('g')  ## first occurence of '2'
print s.rfind('M')  ## same as find. r for reverse. and the same occurence
print s.index('M')  ## same as find.but raises an exceptions if "Y" is not int
print s.rindex('M') ## same analogy
print s.lower()
print s.replace('0','zero')
print s.rstrip() ## removes trailing(last) white space
print s.split(' ')
