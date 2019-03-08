class Grade:
    """A class that stores all the grade aspect item of a quiz that a student taken."""
    def __init__(self, dictionaryofstudentanswer, studentnameORid):
        self.allattemptGrade = []
        self.highestgrade = 0
        self.student = studentnameORid
        self.answer = dictionaryofstudentanswer.get(self.student)
        self.gradelist = []
        self.number_attempt = 0
        self.participate = True

    def calulate_grade(self):
        """Calculate the grade of all attemps,
        then update the all attemps and the highest grade.
        """
        pass

    def check_answer(self,correctAnswer):
        """Compare the answers of each attemps to the correct answer.

        If match, get the corresponding points and append it to a list.
        If not, append 0 to a list, each attempt will has a correspoinding list.

        After all attemps were checked, update the total numbers of attempts,
        and append all the lists to the gradelist argument.

        correctAnswer -- a list contains the correct answers for the quiz
        """
        pass

    def getHighestGrade(self):
        """Return the highest grade out of all the attemps."""
        return self.highestgrade

    def getAttemptGrade(self, number):
        """Return the specific number of attempts grade, depends on the number given.

        number -- the number of the attempt (number = 1 refers to "attempt 1")
        """
        return self.allattemptGrade[number-1]

    def getNumAttemps(self):
        """Return the total number of attempts that a student taken to the quiz"""
        return self.numberAttempts

    def getparticipate(self):
        """Return if the student participate in the quiz (True/False)"""
        return self.participate

class Result:
    """Create a result object of all the students who took the quiz."""
    def __init__(self, dictionaryofstudentanswer, correctAnswer):
        self.participation = 0
        self.average = 0
        self.studentlist = dictionaryofstudentanswer.key()
        self.gradeObjectList = []
        for i in self.studentlist:
            grade = GRADE(dictionaryofstudentanswer, i)
            grade.checkAnswer(correctAnswer)
            grade.calgrade()
            self.gradeObjectList.append(grade)

    def calAverage(self):
        """Calculate the average grade for the quiz using the gradeObjectList,
        and then update the average.
        """
        s = 0
        count = 0
        for i in self.gradeObjectList:
            s = s + i.getHighestGrade
            count = count + 1
        self.average = s/count

    def calparticipation(self):
        """Calculate how many students participate in the quiz."""
        n = 0
        for i in self.gradeObjectList:
            if i.getparticipate() == True:
                n += 1
        self.participation = n

    def createHistogram(self):
        """Create a histogram of the data"""
        pass

