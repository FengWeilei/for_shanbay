from chapter8_2 import Person

##import chapter8_2  Opps

class MITPerson(Person):
    nextidNum = 0
    def __init__(self, name):
        Person.__init__(self, name)
        self.idNum = MITPerson.nextidNum
        MITPerson.nextidNum += 1

    def getidNum(self):
        return self.idNum
    def __it__(self, other):
        return self.idNum < other.idNum

p1 = MITPerson('Mark Guttag')
p2 = MITPerson('Billy Bob Beaver')
p3 = MITPerson('Billy Bob Beaver')
p4 = Person('Billy Bob Beaver')

## and do some comparison
## p1 < P2 etc


## and Mutiple Levels of Inheritance
## Person -> MITPerson -> Student ->UG & G

class Student(MITPerson):
    pass
class UG(Student):
    def __init__(self, name,classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
    def getClass(self):
        return self.year
class Grad(Student):
    pass

p5 = MITPerson
