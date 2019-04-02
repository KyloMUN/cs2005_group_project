from resultAndgrade import Result, Grade
from persistence import Persistence
from structures import Quiz, Question, QuestionBank, Class
'''manual_grading.py

This module is the main module that is needed to manually grade a quiz/question.
It uses persistence through shelve and collaborates with automatic grading modules as well.

Author: Aidan Langer
'''

class Grading():
    '''
    The main class that holds each requirement method for manual grading.
    Included in most methods is an option to make a note of the changes made.

    Author of modification logging requirement: brown

    Requirement 1.5.5
    '''
    def __init__(self, passGrade: int, quiz: Quiz, questionSet: QuestionBank, students: Class, weight: int):
        '''
        The method to initialize the class.
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
        Changes the grade needed to pass the quiz

        Author: Suren Margaryan

        Requirement 1.5.10
        '''
        self.passGrade = newGrade
        if note:
            self.changeLog.append(note)
        return newGrade
        

    def change_question_grade_for_student(self, question: Question, newGrade: int, studentList, student: str, grading: Grade, note=None):
        '''
        Changes the grade of a specific question for a specific student

        Author: cw1511

        Requirement 1.5.8
        '''
        current_question = self.persist.retrieve(Question, question)

        for y in grading.gradelist:
            for t in y:
                if t == self.questionSet.index(question):
                    t = newGrade
        self.persist.store(current_question)
        self.persist.store(self.questionSet)

        if note:
            self.changeLog.append(note)
        return newGrade

    def change_weight(self, newWeight: int, note=None):
        '''
        Changes the weight of the quiz on the student's overall grade
        
        Author: brown / nj3701

        Requirement 1.5.4 / 1.5.7
        '''
        self.weight = newWeight
        if note:
            self.changeLog.append(note)
        
        return newWeight
    
    def change_answer(self, question: Question, newAnswer: str, note=None):
        '''
        Changes the answer to a question, and re-grades students
        
        Author: brown

        Requirement 1.5.3
        '''
        current_question = self.persist.retrieve(Question, question)
        current_question.answers.append(newAnswer)
        self.persist.store(current_question)
        if note:
            self.changeLog.append(note)
        return newAnswer

    def change_grade(self, question: Question, newGrade: int, result: Result, note=None):
        '''
        Grades student.
        
        Author: brown 
        
        Requirement 1.5.1/1.5.2
        '''
        result.fullMark = newGrade
        if note:
            self.changeLog.append(note)
        return newGrade

