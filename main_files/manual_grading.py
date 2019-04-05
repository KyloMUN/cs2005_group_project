from resultAndgrade import Result, Grade
from persistence import Persistence
from structures import Quiz, Question, QuestionBank, Class
'''manual_grading.py

This module is the main module that is needed to manually grade a quiz/question. It is used for the processes in which
the grading may need to be changed outside of traditional methods. For example, this module has a method to retrieve a
previously calculated grade to a question, and change it's grade to a grade you provide it. This means you can give students
bonus points, or completely disregard a question who's programming might be faulty, or it may be unclear. There are many other
applications of this module as well as other methods to help professors properly edit their student's grades. 
It uses the persistence module provided, which itself operates through shelve to store and retreive quizzes and questions from a database, 
and it also takes from the provided automatic grading module to access quiz results and edits those accordingly.

Author: Aidan Langer
'''

class Grading():
    '''
    The main class that holds each requirement method for manual grading.

    Author of modification logging requirement: brown

    Requirement 1.5.5
    '''
    def __init__(self, passGrade: int, quiz: Quiz, questionSet: QuestionBank, students: Class, weight: int):
        '''
        The method to initialize the class. Upon being initialized, it sets up the persistence
        service, and grabs the quiz you'd like to edit, as well as the question set you'd like to access, and the class of students
        who's quiz you're editing. It also initializes an empty list, changeLog, which is used in every method to provide a list of
        'notes' of changes you've made so other professors or assistants can look at them and see recent changes.

        passGrade: int
        quiz : Quiz
        questionSet: QuestionBank
        students : Class
        weight: int
        '''
        self.passGrade = 50
        self.changeLog = []
        self.weight = 5
        self.persist = Persistence()
        self.quiz = self.persist.retrieve(Quiz, quiz)
        self.questionSet = self.persist.retrieve(QuestionBank, questionSet)
        self.students = self.persist.retrieve(Class, students)
    
    def change_pass_grade(self, newGrade: int, note=None):
        '''
        This method takes in an integer named newGrade, as well as an optional note, and uses this newGrade to edit the
        class Grading's passGrade value. This passGrade value defines the grade (in percentage) that is needed to pass the quiz.
        This passing grade value does not affect the automatic grading process and is used to define something arbitrary, therefore
        it does not need to interact with the automatic grading or persistence modules. 

        newGrade: int
        note: str

        Author of requirement: Suren Margaryan

        Requirement 1.5.10
        '''
        self.passGrade = newGrade
        log = "Grade for passing quiz changed to: " + newGrade + "Note: " + note
        self.changeLog.append(log)
        return newGrade
        

    def change_question_grade_for_student(self, question: Question, newGrade: int, studentList: Class, student: str, grading: Grade, newAnswer=None, note=None):
        '''
        This method changes the grade of a specific question for a specific student by take in the Question value of which question you're dealing with,
        the integer value of newGrade, the Class value of your studentList of which you will pull students, and the string value of which student you would like to edit,
        along with the Grade value to look for that student's grade on the question, and an optional note string to document your change.
        Then, this module pulls the question from the persistence system, finds the question in the questionSet, edits it to change
        the current grade of the question into your provided newGrade value, and stores that question back into the persistence system.
        It also gives you the option to change a student's answer to a question if the function is provided a newAnswer value, where the
        function will overwrite the current answer with the given newAnswer.

        question: Question
        newGrade: int
        studentList: Class
        student: str
        grading: Grade
        newAnswer: str
        note: str
        
        Author of requirement: cw1511

        Requirement 1.5.8
        '''
        current_question = self.persist.retrieve(Question, question)

        if newAnswer:
            grading.answer = newAnswer

        for y in grading.gradelist:
            for t in y:
                if t == self.questionSet.index(question):
                    t = newGrade
        self.persist.store(current_question)
        self.persist.store(self.questionSet)

        log = "Grade for student on question changed to: " + newGrade + "Note: " + note
        self.changeLog.append(log)
        return newGrade

    def change_weight(self, newWeight: int, note=None):
        '''
        This method changes the weight of the quiz on the student's overall grade simply by taking in a newWeight integer value and
        and optional note string value to document changes made. Since this method does not affect the automatic grading, it simply edits
        the weight value of the grading class attached to the quiz.

        newWeight: int
        note: str
        
        Authors of requirements: brown / nj3701

        Requirement 1.5.4 / 1.5.7
        '''
        self.weight = newWeight

        log = "Weight of quiz changed to: " + newWeight + "Note: " + note
        self.changeLog.append(log)
        
        return newWeight
    
    def change_answer(self, question: Question, newAnswer: str, note=None):
        '''
        This method changes one of the pre-existing answers in a question, and upon changing it, re-grades all students to fix their marks.
        This is done by taking in a Question value and a newAnswer string value. A little work around to be fair to the students, however,
        is that instead of erasing an answer, we simply append the newAnswer value to the question's list of answers. That way,
        if a student had already gotten it right the first time they wouldn't lose marks when fixing the answer. After this, you simply run
        the automatic grading process over the improved answer list to get all student's new, correct grade.

        question: Question
        newAnswer: str
        note: str
        
        Author of requirement: brown

        Requirement 1.5.3
        '''
        current_question = self.persist.retrieve(Question, question)
        current_question.answers.append(newAnswer)
        self.persist.store(current_question)

        log = "Answer added: " + newAnswer + "Note: " + note
        self.changeLog.append(log)
        return newAnswer

    def change_grade(self, newGrade: int, result: Result, note=None):
        '''
        This method is to change a student's grade on the surface level, say if they recieved bonus marks for a different assignment.
        This is done by taking in a newGrade integer value and a Result value, and an optional note value for logging purposes.
        First the method grabs the Result structure from persistence, and changes it's fullMark attribute to the newGrade value provided to the method.
        Then it stores the result back in persistence, finalizing the change.

        newGrade: int
        result: Result
        note: str

        Author of requirement: brown 
        
        Requirement 1.5.1/1.5.2
        '''
        res = self.persist.retrieve(Result, result)
        res.fullMark = newGrade
        self.persist.store(res)

        log = "Grade for student changed to: " + newGrade + "Note: " + note
        self.changeLog.append(log)

        return newGrade

