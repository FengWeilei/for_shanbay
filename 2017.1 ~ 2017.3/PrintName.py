def printName(firstName,lastName,reverse):
    if reverse :
        print lastName + "," + firstName
    else :
        print firstName +"," + lastName

printName("Meng","Yuan",False)
printName("Yuan","Meng",reverse = True)
