import unittest
from assignment5 import Grading
from structures import Quiz, Question, QuestionBank, Class
from resultAndgrade import *

class TestManualGrading(unittest.TestCase):

    def __init__(self):
        self.quiz = Quiz("quiz1", 1)
        self.questionbank = QuestionBank()
        self.question = Question("question1", 3)
        self.studentClass = Class("class", "brown")
        self.questionbank.questions.append(self.question)
        self.grade = Grade({"student" : "answer"}, "student", [[0,1,2,3,4,5]], "correct answer")
        self.result = Result({"student" : "answer"}, [[0,1,2,3,4,5]], self.questionbank, 1, "answer")

    def good_pass_grade(self):
        grading = Grading(50, self.quiz, self.questionbank, self.studentClass, 5)
        self.assertEqual(60, grading.change_pass_grade(60))
    
    def bad_pass_grade(self):
        grading = Grading(50, self.quiz, self.questionbank, self.studentClass, 5)
        self.assertNotEqual(40, grading.change_pass_grade(60))

    def good_question_grade(self):
        grading = Grading(50, self.quiz, self.questionbank, self.studentClass, 5)
        self.assertEqual(50, grading.change_question_grade_for_student(self.question, 50, self.studentClass, "charles", self.grade))
    
    def bad_question_grade(self):
        grading = Grading(50, self.quiz, self.questionbank, self.studentClass, 5)
        self.assertNotEqual(50, grading.change_question_grade_for_student(self.question, 40, self.studentClass, "charles", self.grade))
    
    def good_weight(self):
        grading = Grading(50, self.quiz, self.questionbank, self.studentClass, 5)
        self.assertEqual(50, grading.change_weight(50))
    
    def bad_weight(self):
        grading = Grading(50, self.quiz, self.questionbank, self.studentClass, 5)
        self.assertNotEqual(40, grading.change_weight(50))
    
    def good_answer(self):
        grading = Grading(50, self.quiz, self.questionbank, self.studentClass, 5)
        self.assertEqual("hello", grading.change_answer(self.question, "hello"))
    
    def bad_answer(self):
        grading = Grading(50, self.quiz, self.questionbank, self.studentClass, 5)
        self.assertNotEqual("goodbye", grading.change_answer(self.question, "hello"))
    
    def good_grade(self):
        grading = Grading(50, self.quiz, self.questionbank, self.studentClass, 5)
        self.assertEqual(100, grading.change_grade(self.question, 100, self.result))
    
    def bad_grade(self):
        grading = Grading(50, self.quiz, self.questionbank, self.studentClass, 5)
        self.assertNotEqual(100, grading.change_grade(self.question, 100, self.result))