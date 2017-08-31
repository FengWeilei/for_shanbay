def readint():
    while True:
        val = raw_input("Enter an integer:")
        try:
            val =  int(val)
            return val
        except ValueError:
            print(val + "is not an interger")

def readVal(valType,requestMsg,errorMsg):
    while True:
        val = raw_input(requestMsg + " ")
        try:
            val = valType(val)
            return val
        except ValueError:
            print val + " " + errorMsg

## readVal(int,"Enter an interger: ","is not an interger.")
            
## Execute either try block or except block.
