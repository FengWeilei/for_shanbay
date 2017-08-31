def getGrades(fname):
    try:
        gradeFile = open(fname, 'r')  ## open a file for reading
    except IOError:
        raise ValueError('getGrades could not open ' + fname)
    grades = []
    for line in gradeFile:
        try:
            grade.append(float(line))
        except:
            raise ValueError('Unable to convert line to float.')
    return grades

try:
    grades = getGrades('quizlgrades.txt')
    grades.sort()
    median = grades[len(grade)/2]
    print 'Median grade is', median
except ValueError, errorMsg:
    print "Whoops.",errorMsg
        
