## Some code about Floats


x = 0.0
for i in range(10):
    x = x + 0.1
if x == 1.0:
    print x,"equals 1.0"
else:
    print x," is not 1.0"


##>>> round(2**0.5,3)
##1.414


##   Newton-Raphson for square root

epsilon = 0.01
i = 0
y = 230002
guess = y/2.0
while abs(guess*guess-y) >= epsilon:
    i = i + 1
    guess = guess - (((guess**2)-y)/(2*guess))
print "square root of ",y,"is about",guess
print "Iterations :",i
