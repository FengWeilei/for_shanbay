##  List and Mutability.

##L =['I did it all',4,'love']
##for i in range(len(L)):
##    print L[i]    ## L[i],not L(i).  Be careful with the details.

Techs = ['MIT','Caltech']
Ivys = ['Harvard','Yale','Brown']

Univs = [Techs,Ivys]
Univsl = [['MIT','Caltech'],['Harvard','Yale','Brown']]

##print "Univs ="  ,Univs
##print "Univsl =" , Univsl
##print Univs == Univsl    ## Looks the same ,but not the same.
##
##print "ID of Univs =",id(Univs)
##print "ID of Univsl =",id(Univsl)


Techs.append('RPI')


##print "Univs =",Univs
##print "Univsl =",Univsl



##for e in Univs:
##    print 'Univs comtains',e
##    print 'which contains'
##    for u in e:
##        print '',u



flat = Techs + Ivys   ##  '+' creat a new list and returns it.
print "flat =",flat


