import datetime

class Person(object):
    def __init__(self, name):
        """create a person with name name"""
        self.name = name
        try:
            lastBlank = name.rindex(' ')
            self.lastName = name[lastBlank + 1 :]
        except:
            self.lastName = name
        self.birthday = None

    def getlastName(self):
        """return self's last name"""
        return self.lastName

    def setBirthday(self,birthDate):
        """Assumes birthDate is of type datetime.date
           set self's birthday to birthDate"""
        self.birthday = birthDate

    def getAge(self):
        """return self's current age in days"""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days

    def __lt__(self, other):
        """Return True if self's name is lexicographically
           less than other's name, and False otherwise"""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        """return self's name"""
        return self.name





me = Person('Michael Guttag')
him = Person('Barack Hussein Obama')
her = Person('Madonna')

him.getlastName()
him.setBirthday(datetime.date(1961,8,4))
her.setBirthday(datetime.date(1958,8,16))

## can print them.

##>>> me
##<__main__.Person object at 0x01C37C30>
##>>> plist = [me, him, her]
##>>> for p in plist:
##	print p
##
##	
##Michael Guttag
##Barack Hussein Obama
##Madonna
##>>> plist.sort()
##>>> for p in plist:
##	print p
##
##	
##Michael Guttag
##Madonna
##Barack Hussein Obama
##
