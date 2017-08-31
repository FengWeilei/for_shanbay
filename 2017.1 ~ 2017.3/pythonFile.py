##nameHandle = open("kids","w")
##for i in range(2):
##    name = raw_input("mengyuan\n230002")
##    nameHandle.write(name + "\n")
##nameHandle.close()   ## aha, it prints the input,why?
    
   
##nameHandle = open("kids","r")
##for line in nameHandle:
##    print line
##nameHandle.close()

##  for example

nameHandle = open("230002","w")
nameHandle.write("MENGYUAN\n")
nameHandle.write('HOW ARE YOU?\n')
nameHandle.close()

nameHandle = open('230002','r')
for line in nameHandle:
    print line[:-1]
nameHandle.close()

    
nameHandle = open('230002','a')
nameHandle = open("230002","w")
nameHandle.write("I'm Fine.\n")
nameHandle.write('Thank You.\n')
nameHandle.close()

nameHandle = open('230002','r')
for line in nameHandle:
    print line[:-1]
nameHandle.close()
