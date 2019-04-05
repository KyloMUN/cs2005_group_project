"""
Interface that contains the Grade and Result class, the Grade can calculate the highest grade of a student, and the 
Result stores the grade objects of all students, so that it can calculate average, summary etc.
"""




class Grade:
    """A class that stores all the grade aspect item of a quiz that a student taken.
       It can check the answers of all attempts of a student and grade it with the highest
       grade. 
    """
    def __init__(self, dictionaryofstudentanswer, studentnameORid, pointList, correctAnswer):
        """ dictionaryofstudentanswer -- a dictionary which key is studentname/id (str)
                                                            value is answer (str)
            studentnameORid -- a student name/id (str) which is one of the key in the above dictionary
            pointList -- a list that stores the points for each question of the quiz. 
            correctAnswer --  a list stores the correct answer of the quiz
        """
        self.point_list = pointList   
        self.allattemptGrade = []
        self.highestgrade = 0
        self.student = studentnameORid
        self.answer = dictionaryofstudentanswer.get(self.student)
        self.gradelist = []   # example [[1,2,1,0,1],[],[]] means the student only try attempt 1, the sublist indicate the corresponding points
        self.number_attempt = 0
        self.participate = True
        self.correct_answer = correctAnswer

    def calculate_grade(self):
        """Calculate the grade of all attemps,
        then update the all attemps and the highest grade.
        """
        self.allattemptGrade=[]
        if self.getparticipate() == False:
            self.allattemptGrade=[]
            self.highestgrade = 0
        
        else:
            highest = 0
            for i in self.gradelist:
                s = 0
                for j in i:
                    s = s + j
                self.allattemptGrade.append(s)
                if s > highest:
                    highest = s
            self.highestgrade = highest



    def checkParticipate(self):
        """Check if all the answers are null value, if yes, update self.participate to False and update the self.number_attempt """
        if self.answer == []:
            self.participate = False
            self.number_attempt = 0
        else:
            n=0
            for i in self.answer:
                if i != []:
                    n=n+1
            self.number_attempt = n

    def check_answer(self):
        """Compare the answers of each attemps to the correct answer.
        If match, get the corresponding points and append it to a sublist.
        If not, append 0 to the sublist, each attempt will has a correspoinding sublist.
        After all attemps were checked, update the total numbers of attempts,
        and append all the sublists to the self.gradelist.    
        """
        self.gradelist=[]
        self.checkParticipate()
        if self.getparticipate() == True:
            for ans in self.answer:
                attempt=[]
                for i in range(len(self.correct_answer)):
                    if ans[i]==self.correct_answer[i]:
                        attempt.append(self.point_list[i])
                    else:
                        attempt.append(0)
                self.gradelist.append(attempt)
        else:
            self.gradelist=[]

    def getStudent(self):
        """Return the name or id of the student depends on what key word is stored"""
        return self.student

    def getHighestGrade(self):
        """Return the highest grade out of all the attemps."""
        return self.highestgrade

    def getAttemptGrade(self, number):
        """Return the specific number of attempts grade, depends on the number given.
        int number -- the number of the attempt (number = 1 refers to "attempt 1")
        """
        while True:
            try:
                return self.allattemptGrade[number-1]
            
            except ValueError:
                break
    def getNumAttempts(self):
        """Return the total number of attempts that a student taken to the quiz"""
        return self.number_attempt

    def getparticipate(self):
        """Return if the student participate in the quiz (True/False)"""
        return self.participate

class Result:
    """
    Create a result object of all the students who took the quiz.
    self.gradeObjectList - a list that contains each student's the grade objects, by using 
                           this list, each student's highest grade can be retrieved  
    """
    def __init__(self, dictionaryofstudentanswer, pointList, questionList, quizNumber, correctAns):
        self.correct_answer = correctAns
        self.quiz_number = quizNumber
        self.question_list = questionList
        self.point_list = pointList
        self.dict_answer = dictionaryofstudentanswer
        self.fullMark = 0
        self.participation = 0
        self.average = 0
        self.result_dict = dict()
        self.student_list = list(dictionaryofstudentanswer.keys())
        self.gradeObjectList = []
        for i in self.student_list:
            grade = Grade(self.dict_answer, i, self.point_list, self.correct_answer)
            grade.check_answer()
            grade.calculate_grade()
            self.gradeObjectList.append(grade)

    def calculate_fullmark(self):
        """Calculate the full mark of a quiz""" 
        s = 0
        for i in self.point_list:
            s = s + i
        self.fullMark = s

    def get_student_grade_object(self, nameORid):
        """Return the grade object of a given student name or id (str)"""
        for i in self.gradeObjectList:
            if i.getStudent() == nameORid:
                return i

    def make_result_dict(self):
        """Make a dictionary stores the student name/id(depends on login info) as key, 
           stores the highest grade as the value of the quiz. Then update the self.result_dict
        """    
        for i in self.student_list:
            for j in self.gradeObjectList:
                if i == j.getStudent():
                    self.result_dict[i] = j.getHighestGrade()

    def calculate_Average(self):
        """Calculate the average grade for the quiz using the gradeObjectList,
        and then update the average.
        """
        s = 0
        for i in self.gradeObjectList:
            s = s + i.getHighestGrade()
        
        self.average = s/len(self.gradeObjectList)

    def calculate_participation(self):
        """Calculate how many students participate in the quiz."""
        n = 0
        for i in self.gradeObjectList:
            if i.getparticipate() == True:
                n += 1
        self.participation = n

    def createHistogram(self):
        """Create a histogram of the data"""
        return "Hello, World!"
    
    def getAverage(self):
        """Return the average grade of the quiz"""
        return self.average

    def getFullMark(self):
        """Return the total point of the quiz"""
        return self.fullMark

    def get_result_dict(self):
        """Return the result dictionary"""
        return self.result_dict

    def get_question(self):
        """Return the questions of the quiz"""
        return self.question_list

    def get_quiz_number(self):
        """Return the quiz number"""
        return self.quiz_number

    def get_correct_answer(self):
        """Return the correct answer of the quiz"""
        return self.correct_answer

    def get_participation(self):
        """Return the number of participation of the quiz"""
        return self.participation