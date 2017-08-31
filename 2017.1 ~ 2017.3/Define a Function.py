def printName(firstName,lastName,reverse):
    if reverse :
        print lastName + "," + firstName
    else :
        print firstName +"," + lastName

printName("Meng","Yuan",False)
printName("Yuan","Meng",reverse = True)



def f(x):
    y = 2
    x = x + y
    print "x = ",x
    return x
x = 3
y = 1
z = f(x)
print "z = ",z
print "x = ",x
print "y = ",y
