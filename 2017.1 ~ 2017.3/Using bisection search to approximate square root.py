##  Using bisection search to approximate square root

x = 230002
epsilon = 0.01
numGuess = 0
low = 0.0
high = max(1.0,x)
ans = (low + high)/2
while abs(ans**2 - x) >= epsilon:
    numGuess += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print ans, "is the square root of",x
print "numGuess = ",numGuess


## Compared with Newton-Raphson

##   Newton-Raphson for square root

epsilon = 0.01
i = 0
y = 230002
guess = y/2.0
while abs(guess*guess-y) >= epsilon:
    i = i + 1
    guess = guess - (((guess**2)-y)/(2*guess))
print "square root of ",y,"is about",guess
print "NUM of Iterations = ",i
