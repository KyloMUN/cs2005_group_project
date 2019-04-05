"""
Interface that contains the Grade and Result class, the Grade can calculate the highest grade of a student, and the 
Result stores the grade objects of all students, so that it can calculate average, summary etc.
"""




class Grade:
    """A class that stores all the grade aspect items of a quiz that a student has taken.
       It takes care of all the marking by checking answers against correct answers, adding points and attempts up and comparing
       attempts to ensure the student gets the highest grade possible. 
    """
    def __init__(self, dictionaryofstudentanswer, studentnameORid, pointList, correctAnswer):
        """ dictionaryofstudentanswer -- a dictionary which the key is their studentname/id (str) and the value is their answer (str)
            studentnameORid -- a student name/id (str) which is one of the keys in the above dictionary
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
        """ Calculate the grade of all attempts, then updates the grade to the highest grade possible by comparing every attempt to eachother.
            If an attempt is found to have not been utilized, it will be marked False and will not be used by this method, preventing any possible
            errors that could arrise by adding null values.
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
        """This function checks if all the answers in an attempt are a null value, and if so, updates the participation value of the attempt
         to False, and adds the attempt to the total. This ensures there are no errors when attempting to calculate a grade of an attempt that
         was not utilized, as it will simply be rendered False and unusable.
        """
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
        """Compare the answers of each attempts to the correct answers.
        If they match, get the corresponding points and append it to a sublist.
        If not, append 0 to the sublist, each attempt will have a correspoinding sublist.
        After all attemps are checked, update the total numbers of attempts,
        and append all the sublists to the self.gradelist list object.    
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
        """Return the highest grade out of all the attempts."""
        return self.highestgrade

    def getAttemptGrade(self, number):
        """Return a specific attempt's grade, which attempt is used depends on the number given to the function.

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
    This class creates a result object of all the students who took the quiz. It uses a list of Grades and compares them to eachother in order
    to get a class average, how many students participated, a list of questions, among other things. This is useful mostly to the instructor,
    as they can see how well their class is doing and may choose to keep this information private from their students. It takes in the dictionary
    of student ids compared to answers, a pointList, a questionList, and the specific quizNumber. 

    gradeObjectList: a list that contains each student's the grade objects, by using this list, each student's highest grade can be retrieved
    """
    def __init__(self, dictionaryofstudentanswer, pointList, questionList, quizNumber):
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
        """
        This method calculates the full mark of a quiz by adding up the points given in pointList, and assigns the value to the fullMark
        value of the Result object. 
        """ 
        s = 0
        for i in self.point_list:
            s = s + i
        self.fullMark = s

    def get_student_grade_object(self, nameORid):
        """
        This method returns the grade object of a given student name or id, which is taken in as a string. It searches the gradeObjectList
        for that string and return what grade the student has gotten. This makes it easy for instructors to keep track of certain students if
        need be. 
        """
        for i in self.gradeObjectList:
            if i.getStudent() == nameORid:
                return i

    def make_result_dict(self):
        """
        This function makes a dictionary and stores the student name/id (depends on login info) as a key, 
        and stores the highest grade as the value of the quiz. Then it updates the result_dict value of the Result object for easy accesibility.
        """    
        for i in self.student_list:
            for j in self.gradeObjectList:
                if i == j.getStudent():
                    self.result_dict[i] = j.getHighestGrade()

    def calculate_Average(self):
        """
        This method calculates the average grade of the class on the current quiz using every item in the gradeObjectList,
        and then updates the average value in the Result object, so instructors can see how their class did on the quiz as a whole.
        """
        s = 0
        for i in self.gradeObjectList:
            s = s + i.getHighestGrade()
        
        self.average = s/len(self.gradeObjectList)

    def calculate_participation(self):
        """
        Calculate how many students have participated in the quiz. This can be compared to the overall number of students in the class to see
        how active the students are being, which may inspire grade curving or something akin to that.
        """
        n = 0
        for i in self.gradeObjectList:
            if i.getparticipate() == True:
                n += 1
        self.participation = n

    def createHistogram(self):
        """
        This method creates a histogram of the data given based on the average marks of the students on the quiz related to which students
        achieved which marks.
        """
        return "Hello, World!"
    
    def getAverage(self):
        """Returns the average value of the result object, which represents the average grade of the quiz"""
        return self.average

    def getFullMark(self):
        """Returns the total point value of the quiz, adding every student's marks together"""
        return self.fullMark

    def get_result_dict(self):
        """Returns the result dictionary, a dictionary that holds student names or ids as keys and their marks on the quiz as values."""
        return self.result_dict

    def get_question(self):
        """Returns the questions of the quiz."""
        return self.question_list

    def get_quiz_number(self):
        """Returns the specific number of the quiz."""
        return self.quiz_number

    def get_participation(self):
        """Return the number of students who participated in the quiz"""
        return self.participation