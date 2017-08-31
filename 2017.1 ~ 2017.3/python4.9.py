def isPalindrome(s):
    """Assume s is an string
       Returns True if s is a palindrome and False otherwise.
       Punctuation marks, blanks, and capitalization are ignored."""

    def toChars(s):
        s = s.lower()
        letters = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letters = letters + c
                return letters

    def isPal(s):
        print "isPal called with",s
        if len(s) <= 1:
            print "About to return True from base case"
            return True
        else:
            answer = s[0] == s[-1] and isPal(s[1:-1])  ## Got trouble here
            print "About to return",answer,"for",s
            return answer

    return isPal(toChars(s))



##def testIsPalindrome():
    
print 'Try doggod'
print isPalindrome('dogGod')
print "Try dogood"
print isPalindrome('doGood')
