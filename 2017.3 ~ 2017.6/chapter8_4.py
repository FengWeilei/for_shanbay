from chapter8_3 import Student
class Grades(object):
    """A mapping from students to a list of grade"""

    def __init__(self):
        """Create empty grade book"""
        self.students = []
        self.grades = {}
        self.isSorted = True

    def addStudent(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.getidNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade): 
        """Assumes: grade is a float
           Add grade to the list of grades for student"""
        try:
            self.grades[student.getidNum()].append(grade)
        except:
            raise ValueError('Stusent not in mapping')

    def getGrades(self, student):
        """Return a list of grades for student"""
        try:  ##return copy of student's grades
            return self.grades[student.getidNum()][:]
        except:
            raise ValueError('Student not in mapping')

    def allStudents(self):
        """Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        return self.students[:] ##return copy of list of students
