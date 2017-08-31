class inSet(object):
    """An inSet is a set of intergers
       The value is represented by a list of ints, self.vals.
       Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of intergers"""
        self.vals = []

    def inset(self, e):
        """Assumes e is interger and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an interger and removes e from self
           Return True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an interger and remove e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e)+'not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        result.vals.sort()
        result = ''
        for e in self.vals:
            result = result + str(e) + ','
        return '{' + result[:-1] + '}' ## -1 omits trailing comma
